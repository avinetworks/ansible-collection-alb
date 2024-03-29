#!/usr/bin/python
# SPDX-License-Identifier: Apache License 2.0

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = '''
---
module: avi_deploy_controller
author: chaitanyaavi (@chaitanyaavi) <chaitanya.deshpande@avinetworks.com>

short_description: Module is to deploy vm on vcenter
description:
    - This module is used to deploy Vm

options:
    state:
        description:
            - The state that should be applied on the entity.
        default: present
        choices: ["absent", "present"]
        type: str
    ovftool_path:
        description:
            - Path of the ovftool where it is installed.
        required: true
        type: str
    vcenter_host:
        description:
            - Host name or IP of the Vcenter.
        required: true
        type: str
    vcenter_user:
        description:
            - Username of the Vcenter.
        required: true
        type: str
    vcenter_password:
        description:
            - Password of the Vcenter.
        required: true
        type: str
    ssl_verify:
        description:
            - Flag to set ssl Verification while deploying the VM.
        default: false
        type: bool
    con_datacenter:
        description:
            - Destination datacenter for the deploy operation.
        type: str
    con_cluster:
        description:
            - The cluster name where the virtual machine will run.
        type: str
    con_datastore:
        description:
            - Datastore to provision virtual machine.
        type: str
    con_mgmt_network:
        description:
            - Name of the object.
        required: true
        type: str
    con_disk_mode:
        description:
            - Type of disk mode.
        default: thin
        choices: ["thin", "thick", "eagerzeroedthick"]
        type: str
    con_ova_path:
        description:
            - OVF template path to deploy VM using that.
        required: true
        type: str
    con_vm_name:
        description:
            - Name of the virtual machine.
        required: true
        type: str
    con_power_on:
        description:
            - State of the virtual machine to power on and power off.
        default: true
        type: bool
    con_vcenter_folder:
        description:
            - Destination folder, absolute path to find an existing VM or create the new VM.
        type: str
    con_mgmt_ip:
        description:
            - Static IPV4 address.
        type: str
    con_mgmt_ip_v6:
        description:
            - Static IPV6 address.
        type: str
    con_mgmt_mask:
        description:
            - Static netmask required for con_mgmt_ip.
        type: str
    con_mgmt_mask_v6:
        description:
            - Static netmask required for con_mgmt_ip_v6.
        type: str
    con_default_gw:
        description:
            - Getway for the con_mgmt_ip.
        type: str
    con_default_gw_v6:
        description:
            - Getway for the con_mgmt_ip_v6.
        type: str
    con_mgmt_ip_v4_enable:
        description:
            - Flag to spin up IPV4 controller.
        default: true
        type: bool
    con_mgmt_ip_v6_enable:
        description:
            - Flag to spin up IPV6 controller.
        default: false
        type: bool
    con_sysadmin_public_key:
        description:
            - File path of sysadmin public key file.
        type: str
    con_number_of_cpus:
        description:
            - Number of CPUs.
        type: int
    con_cpu_reserved:
        description:
            - Number of CPUs to be reserved.
        type: int
    con_memory:
        description:
            - Amount of memory in MB.
        type: int
    con_memory_reserved:
        description:
            - Amount of memory to be reserved.
        type: int
    con_disk_size:
        description:
            - Disk storage size in gb.
        type: int
    con_ovf_properties:
        description:
            - Object of ovf properties.
        type: dict
    con_wait_time:
        description:
            - Define a timeout (in seconds) to wait for Ip address.
        default: 3600
        type: int
    round_wait:
        description:
            - Round wait to wait for given rounds.
        default: 10
        type: int
'''

EXAMPLES = """
- hosts: localhost
  connection: local
  collections:
    - vmware.alb
  tasks:
    - name: Avi Controller | VMware | Configure VMware controller
      import_role:
        name: avicontroller_vmware
      vars:
        ovftool_path: /usr/lib/vmware-ovftool
        vcenter_host: '{{ vcenter_host }}'
        vcenter_user: '{{ vcenter_user }}'
        vcenter_password: '{{ vcenter_password }}'
        con_datacenter: 10GTest
        con_cluster: Arista
        con_mgmt_network: Mgmt_Ntwk_3
        con_ova_path: ./controller.ova
        con_vm_name: ansible-test-controller
        con_power_on: true
        con_vcenter_folder: network/avi
"""

from ansible.module_utils.basic import AnsibleModule
try:
    import atexit
    import json
    try:
        from urllib import quote
    except ImportError:
        from urllib.parse import quote
    import os
    import requests
    import time
    import ipaddress
    from pyVim.connect import SmartConnect, Disconnect
    from pyVim.task import WaitForTasks
    from pyVmomi import vim, vmodl
    HAS_IMPORT = True
except ImportError:
    HAS_IMPORT = False


def is_vm_exist(si, cl, vm_name):
    container = si.content.viewManager.CreateContainerView(cl, [vim.VirtualMachine], True)
    for managed_object_ref in container.view:
        if managed_object_ref.name == vm_name:
            return True
    return False


def get_vm_by_name(si, vm_name):
    container = si.content.viewManager.CreateContainerView(si.content.rootFolder,
                                                           [vim.VirtualMachine], True)
    for vm in container.view:
        if vm.name == vm_name:
            return vm
    return None


def get_dc(si, name):
    """
    Get a datacenter by its name.
    """
    for dc in si.content.rootFolder.childEntity:
        if dc.name == name:
            return dc
    raise Exception('Failed to find datacenter named %s' % name)


def compile_folder_path_for_object(vobj):
    """ make a /vm/foo/bar/baz like folder path for an object """
    paths = []
    if isinstance(vobj, vim.Folder):
        paths.append(vobj.name)

    thisobj = vobj
    while hasattr(thisobj, 'parent'):
        thisobj = thisobj.parent
        if isinstance(thisobj, vim.Folder):
            paths.append(thisobj.name)
    paths.reverse()
    if paths[0] == 'Datacenters':
        paths.remove('Datacenters')
    return '/' + '/'.join(paths)


def get_folder_by_path(si, dc, path):
    container = si.content.viewManager.CreateContainerView(
        dc, [vim.Folder], True)
    for managed_object_ref in container.view:
        if managed_object_ref.name == path.split("/")[-1:][0]:
            if path in compile_folder_path_for_object(managed_object_ref):
                return managed_object_ref
    return None


def get_cluster(si, dc, name):
    """
    Get a cluster in the datacenter by its names.
    """
    view_manager = si.content.viewManager
    container_view = view_manager.CreateContainerView(
        dc, [vim.ClusterComputeResource], True)
    try:
        for rp in container_view.view:
            if rp.name == name:
                return rp
    finally:
        container_view.Destroy()
    raise Exception("Failed to find cluster %s in datacenter %s" %
                    (name, dc.name))


def get_first_cluster(si, dc):
    """
    Get the first cluster in the list.
    """
    view_manager = si.content.viewManager
    container_view = view_manager.CreateContainerView(
        dc, [vim.ClusterComputeResource], True)
    try:
        first_cluster = container_view.view[0]
    finally:
        container_view.Destroy()
    if first_cluster is None:
        raise Exception("Failed to find a resource pool in dc %s" % dc.name)
    return first_cluster


def get_ds(dc, name):
    """
    Pick a datastore by its name.
    """
    for ds in dc.datastore:
        try:
            if ds.name == name:
                return ds
        except:  # Ignore datastores that have issues
            pass
    raise Exception("Failed to find %s on datacenter %s" % (name, dc.name))


def get_sysadmin_key(keypath):
    if os.path.exists(keypath):
        with open(keypath, 'r') as keyfile:
            data = keyfile.read().rstrip('\n')
            return data
    raise Exception('Failed to find sysadmin public key file at %s\n' % keypath)


def get_largest_free_ds(cl):
    """
    Pick the datastore that is accessible with the largest free space.
    """
    largest = None
    largest_free = 0
    for ds in cl.datastore:
        try:
            free_space = ds.summary.freeSpace
            if free_space > largest_free and ds.summary.accessible:
                largest_free = free_space
                largest = ds
        except:  # Ignore datastores that have issues
            pass
    if largest is None:
        raise Exception('Failed to find any free datastores on %s' % cl.name)
    return largest


def wait_for_tasks(service_instance, tasks):
    """Given the service instance si and tasks, it returns after all the
   tasks are complete
   """
    property_collector = service_instance.content.propertyCollector
    task_list = [str(task) for task in tasks]
    # Create filter
    obj_specs = [vmodl.query.PropertyCollector.ObjectSpec(obj=task)
                 for task in tasks]
    property_spec = vmodl.query.PropertyCollector.PropertySpec(type=vim.Task,
                                                               pathSet=[],
                                                               all=True)
    filter_spec = vmodl.query.PropertyCollector.FilterSpec()
    filter_spec.objectSet = obj_specs
    filter_spec.propSet = [property_spec]
    pcfilter = property_collector.CreateFilter(filter_spec, True)
    try:
        version, state = None, None
        # Loop looking for updates till the state moves to a completed state.
        while len(task_list):
            update = property_collector.WaitForUpdates(version)
            for filter_set in update.filterSet:
                for obj_set in filter_set.objectSet:
                    task = obj_set.obj
                    for change in obj_set.changeSet:
                        if change.name == 'info':
                            state = change.val.state
                        elif change.name == 'info.state':
                            state = change.val
                        else:
                            continue

                        if not str(task) in task_list:
                            continue

                        if state == vim.TaskInfo.State.success:
                            # Remove task from taskList
                            task_list.remove(str(task))
                        elif state == vim.TaskInfo.State.error:
                            raise task.info.error
            # Move to next version
            version = update.version
    finally:
        if pcfilter:
            pcfilter.Destroy()


def get_vm_ips(target_vm):
    ip_address = []
    for nic in target_vm.guest.net:
        addresses = nic.ipConfig.ipAddress
        for adr in addresses:
            ip_address.append(adr.ipAddress)
    return ip_address


def get_vm_ip_by_network(target_vm, network):
    ip_address = []
    for nic in target_vm.guest.net:
        if nic.network == network:
            addresses = nic.ipConfig.ipAddress
            for adr in addresses:
                ip_address.append(adr.ipAddress)
    return ip_address


def is_update_cpu(module):
    return ('con_number_of_cpus' in module.params and
            module.params['con_number_of_cpus'] is not None)


def is_update_memory(module):
    return ('con_memory' in module.params and
            module.params['con_memory'] is not None)


def is_reserve_memory(module):
    return ('con_memory_reserved' in module.params and
            module.params['con_memory_reserved'] is not None)


def is_reserve_cpu(module):
    return ('con_cpu_reserved' in module.params and
            module.params['con_cpu_reserved'] is not None)


def is_resize_disk(module):
    return ('con_disk_size' in module.params and
            module.params['con_disk_size'] is not None)


def is_reconfigure_vm(module):
    return (is_update_cpu(module) or is_update_memory(module) or
            is_reserve_memory(module) or is_reserve_cpu(module) or
            is_resize_disk(module))

def is_ipv6_address(controller_ip):
        IPV6 = 6
        try:
            ip = ipaddress.ip_address(controller_ip)
            return ip.version == IPV6
        except ValueError as ve:
            return False

def controller_wait(controller_ip, round_wait=10, wait_time=3600):
    """
    It waits for controller to come up for a given wait_time (default 1 hour).
    :return: controller_up: Boolean value for controller up state.
    """
    count = 0
    max_count = wait_time / round_wait
    is_ipv6 = is_ipv6_address(controller_ip)
    if is_ipv6:
        path = "https://[" + str(controller_ip) + "]/api/cluster/runtime"
    else:
        path = "https://" + str(controller_ip) + "/api/cluster/runtime"
    ctrl_status = False
    r = None
    while True:
        if count >= max_count:
            break
        try:
            r = requests.get(path, timeout=10, verify=False)
            # Check for controller response for login URI.
            if r.status_code in (500, 502, 503) and count < max_count:
                time.sleep(10)
            else:
                if r:
                    data = r.json()
                    cluster_state = data.get('cluster_state', '')
                    if cluster_state:
                        if cluster_state['state'] == 'CLUSTER_UP_NO_HA':
                            ctrl_status = True
                            break
        except (requests.Timeout, requests.exceptions.ConnectionError) as e:
            time.sleep(10)
        count += 1
    return ctrl_status


def main():
    module = AnsibleModule(
        argument_spec=dict(
            ovftool_path=dict(required=True, type='str'),
            vcenter_host=dict(required=True, type='str'),
            vcenter_user=dict(required=True, type='str'),
            vcenter_password=dict(required=True, type='str', no_log=True),
            ssl_verify=dict(required=False, type='bool', default=False),
            state=dict(required=False, type='str', default='present', choices=['absent', 'present']),
            con_datacenter=dict(required=False, type='str'),
            con_cluster=dict(required=False, type='str'),
            con_datastore=dict(required=False, type='str'),
            con_mgmt_network=dict(required=True, type='str'),
            con_disk_mode=dict(required=False, type='str', default='thin',
                               choices=['thin', 'thick', 'eagerzeroedthick']),
            con_ova_path=dict(required=True, type='str'),
            con_vm_name=dict(required=True, type='str'),
            con_power_on=dict(required=False, type='bool', default=True),
            con_vcenter_folder=dict(required=False, type='str'),
            con_mgmt_ip=dict(required=False, type='str'),
            con_mgmt_ip_v6=dict(required=False, type='str'),
            con_mgmt_mask=dict(required=False, type='str'),
            con_mgmt_mask_v6=dict(required=False, type='str'),
            con_default_gw=dict(required=False, type='str'),
            con_default_gw_v6=dict(required=False, type='str'),
            con_mgmt_ip_v4_enable=dict(required=False, type='bool', default=True),
            con_mgmt_ip_v6_enable=dict(required=False, type='bool', default=False),
            con_sysadmin_public_key=dict(required=False, type='str'),
            con_number_of_cpus=dict(required=False, type='int'),
            con_cpu_reserved=dict(required=False, type='int'),
            con_memory=dict(required=False, type='int'),
            con_memory_reserved=dict(required=False, type='int'),
            con_disk_size=dict(required=False, type='int'),
            con_ovf_properties=dict(required=False, type='dict'),
            # Max time to wait for controller up state
            con_wait_time=dict(required=False, type='int', default=3600),
            # Retry after every rount_wait time to check for controller state.
            round_wait=dict(required=False, type='int', default=10),
        ),
        supports_check_mode=True,
    )
    if not HAS_IMPORT:
        return module.fail_json(msg=(
            'Some of the python package is not installed. please install the requirements from requirements.txt'))
    try:
        si = SmartConnect(disableSslCertValidation=True,
                               host=module.params['vcenter_host'],
                               user=module.params['vcenter_user'],
                               pwd=module.params['vcenter_password'])
        atexit.register(Disconnect, si)
    except vim.fault.InvalidLogin:
        return module.fail_json(
            msg='exception while connecting to vCenter, login failure, '
                'check username and password')
    except requests.exceptions.ConnectionError:
        return module.fail_json(
            msg='exception while connecting to vCenter, check hostname, '
                'FQDN or IP')
    check_mode = module.check_mode
    if module.params['state'] == 'absent':
        vm = get_vm_by_name(si, module.params['con_vm_name'])

        if vm is None:
            return module.exit_json(msg='A VM with the name %s not found' % (
                module.params['con_vm_name']))

        if check_mode:
            return module.exit_json(msg='A VM with the name %s found' % (
                module.params['con_vm_name']), changed=True)

        if vm.runtime.powerState == vim.VirtualMachinePowerState.poweredOn:
            task = vm.PowerOffVM_Task()
            wait_for_tasks(si, [task])

        task = vm.Destroy_Task()
        wait_for_tasks(si, [task])

        return module.exit_json(msg='A VM with the name %s deleted successfully'
                                    % (module.params['con_vm_name']))

    if module.params.get('con_datacenter', None):
        dc = get_dc(si, module.params['con_datacenter'])
    else:
        dc = si.content.rootFolder.childEntity[0]

    if module.params.get('con_cluster', None):
        cl = get_cluster(si, dc, module.params['con_cluster'])
    else:
        cl = get_first_cluster(si, dc)

    if module.params.get('con_datastore', None):
        ds = get_ds(cl, module.params['con_datastore'])
    else:
        ds = get_largest_free_ds(cl)

    if is_vm_exist(si, cl, module.params['con_vm_name']):
        vm = get_vm_by_name(si, module.params['con_vm_name'])
        vm_path = compile_folder_path_for_object(vm)
        folder = get_folder_by_path(si, dc, module.params['con_vcenter_folder'])
        folder_path = compile_folder_path_for_object(folder)
        changed = False
        if vm_path != folder_path:
            # migrate vm to new folder
            if not check_mode:
                folder.MoveInto([vm])
            changed = True
        if (not module.params['con_power_on']) and \
                vm.runtime.powerState == vim.VirtualMachinePowerState.poweredOn:
            if not check_mode:
                task = vm.PowerOffVM_Task()
                wait_for_tasks(si, [task])
            changed = True
        if module.params['con_power_on'] and vm.runtime.powerState == \
                vim.VirtualMachinePowerState.poweredOff:
            if not check_mode:
                task = vm.PowerOnVM_Task()
                wait_for_tasks(si, [task])
            changed = True

        if module.params.get('con_datastore', None):
            ds_names = []
            for datastore in vm.datastore:
                ds_names.append(datastore.name)
            if ds.name not in ds_names:
                module.fail_json(msg='VM datastore cant be modified')

        if module.params.get('con_mgmt_ip', None) and not module.params['con_mgmt_ip_v6_enable']:
            ip_addresses = get_vm_ips(vm)
            if (ip_addresses and
                    not module.params['con_mgmt_ip'] in ip_addresses):
                module.fail_json(msg='VM static ip address cant be modified')

        if module.params.get('con_mgmt_ip_v6', None) and module.params['con_mgmt_ip_v6_enable']:
            ip_addresses = get_vm_ips(vm)
            if (ip_addresses and
                    not module.params['con_mgmt_ip_v6'] in ip_addresses):
                module.fail_json(msg='VM static ip address cant be modified')

        if is_reconfigure_vm(module):
            if not check_mode:
                vmSummary = vm.summary.config
                cspec = vim.vm.ConfigSpec()

                if is_resize_disk(module):
                    disk = None
                    for device in vm.config.hardware.device:
                        if isinstance(device, vim.vm.device.VirtualDisk):
                            disk = device
                            break

                if vmSummary.numCpu != module.params['con_number_of_cpus'] or \
                        vmSummary.memorySizeMB != module.params['con_memory'] or \
                        vmSummary.memoryReservation != module.params['con_memory_reserved'] or \
                        vmSummary.cpuReservation != module.params['con_cpu_reserved'] or \
                        (disk is not None and disk.capacityInKB != module.params['con_disk_size'] * 1024 * 1024):
                    if vm.runtime.powerState == vim.VirtualMachinePowerState.poweredOn:
                        task = vm.PowerOffVM_Task()
                        wait_for_tasks(si, [task])
                    if is_update_cpu(module):
                        if vmSummary.numCpu != module.params['con_number_of_cpus']:
                            cspec.numCPUs = module.params['con_number_of_cpus']
                            changed = True
                    if is_update_memory(module):
                        if vmSummary.memorySizeMB != module.params['con_memory']:
                            cspec.memoryMB = module.params['con_memory']
                            changed = True
                    if is_reserve_memory(module):
                        if vmSummary.memoryReservation != module.params['con_memory_reserved']:
                            cspec.memoryAllocation = vim.ResourceAllocationInfo(
                                reservation=module.params['con_memory_reserved'])
                            changed = True
                    if is_reserve_cpu(module):
                        if vmSummary.cpuReservation != module.params['con_cpu_reserved']:
                            cspec.cpuAllocation = vim.ResourceAllocationInfo(
                                reservation=module.params['con_cpu_reserved'])
                            changed = True
                    if is_resize_disk(module):
                        if disk.capacityInKB != module.params['con_disk_size'] * 1024 * 1024:
                            disk.capacityInKB = module.params['con_disk_size'] * 1024 * 1024
                            devSpec = vim.vm.device.VirtualDeviceSpec(
                                device=disk, operation="edit")
                            cspec.deviceChange.append(devSpec)
                            changed = True
                    WaitForTasks([vm.Reconfigure(cspec)], si=si)

                    if module.params['con_power_on']:
                        task = vm.PowerOnVM_Task()
                        WaitForTasks([task], si=si)

        if changed and not check_mode:
            module.exit_json(msg='A VM with the name %s updated successfully' %
                                 (module.params['con_vm_name']), changed=True)
        if changed and check_mode:
            module.exit_json(changed=True)
        else:
            module.exit_json(
                msg='A VM with the name %s is already present' % (
                    module.params['con_vm_name']))

    if (module.params['con_ova_path'].startswith('http')):
        if (requests.head(module.params['con_ova_path'], verify=module.params['ssl_verify']).status_code != 200):
            module.fail_json(msg='Controller OVA not found or readable from specified URL path')
    else:
        if (not os.path.isfile(module.params['con_ova_path']) or
                not os.access(module.params['con_ova_path'], os.R_OK)):
            module.fail_json(msg='Controller OVA not found or not readable')

    ovftool_exec = '%s/ovftool' % module.params['ovftool_path']
    ova_file = module.params['con_ova_path']
    quoted_vcenter_user = quote(module.params['vcenter_user'])
    quoted_vcenter_pass = quote(module.params['vcenter_password'])
    if is_ipv6_address(module.params['vcenter_host']):
        vi_string = 'vi://%s:%s@[%s]' % (
            quoted_vcenter_user, quoted_vcenter_pass,
            module.params['vcenter_host'])
    else:
        vi_string = 'vi://%s:%s@%s' % (
            quoted_vcenter_user, quoted_vcenter_pass,
            module.params['vcenter_host'])
    vi_string += '/%s%s/%s' % (dc.name, compile_folder_path_for_object(cl),
                               cl.name)
    command_tokens = [ovftool_exec]

    if module.params['con_power_on'] and not is_reconfigure_vm(module):
        command_tokens.append('--powerOn')
    if not module.params['ssl_verify']:
        command_tokens.append('--noSSLVerify')
    if check_mode:
        command_tokens.append('--verifyOnly')
    command_tokens.extend([
        '--acceptAllEulas',
        '--skipManifestCheck',
        '--allowExtraConfig',
        '--diskMode=%s' % module.params['con_disk_mode'],
        '--datastore=%s' % ds.name,
        '--name=%s' % module.params['con_vm_name']
    ])

    if ('ovf_network_name' in module.params.keys() and
            module.params['ovf_network_name'] is not None and
            len(module.params['ovf_network_name']) > 0):
        try:
            d = json.loads(
                module.params['ovf_network_name'].replace("'", "\""))
            for key, network_item in d.items():
                command_tokens.append('--net:%s=%s' % (key, network_item))
        except ValueError:
            command_tokens.append('--net:%s=%s' % (
                module.params['ovf_network_name'],
                module.params['con_mgmt_network']))
    else:
        command_tokens.append(
            '--network=%s' % module.params['con_mgmt_network'])

    if module.params.get('con_mgmt_ip_v6', None):
        command_tokens.append('--prop:%s=%s' % (
            'avi.mgmt-ip-v6.CONTROLLER', module.params['con_mgmt_ip_v6']))

    if module.params.get('con_mgmt_ip', None) and not module.params['con_mgmt_ip_v6_enable']:
        command_tokens.append('--prop:%s=%s' % (
            'avi.mgmt-ip.CONTROLLER', module.params['con_mgmt_ip']))

    if module.params.get('con_mgmt_mask_v6', None):
        command_tokens.append('--prop:%s=%s' % (
            'avi.mgmt-mask-v6.CONTROLLER', module.params['con_mgmt_mask_v6']))

    if module.params.get('con_mgmt_mask', None) and not module.params['con_mgmt_ip_v6_enable']:
        command_tokens.append('--prop:%s=%s' % (
            'avi.mgmt-mask.CONTROLLER', module.params['con_mgmt_mask']))

    if module.params.get('con_default_gw_v6', None):
        command_tokens.append('--prop:%s=%s' % (
            'avi.default-gw-v6.CONTROLLER', module.params['con_default_gw_v6']))

    if module.params.get('con_default_gw', None) and not module.params['con_mgmt_ip_v6_enable']:
        command_tokens.append('--prop:%s=%s' % (
            'avi.default-gw.CONTROLLER', module.params['con_default_gw']))

    if module.params.get('con_mgmt_ip_v6_enable', None):
        command_tokens.append('--prop:%s=%s' % (
            'avi.mgmt-ip-v6-enable.CONTROLLER', module.params['con_mgmt_ip_v6_enable']))

    if module.params.get('con_mgmt_ip_v4_enable', None) and not module.params['con_mgmt_ip_v6_enable']:
        command_tokens.append('--prop:%s=%s' % (
            'avi.mgmt-ip-v4-enable.CONTROLLER', module.params['con_mgmt_ip_v4_enable']))

    if module.params.get('con_sysadmin_public_key', None):
        command_tokens.append('--prop:%s=%s' % (
            'avi.sysadmin-public-key.CONTROLLER',
            get_sysadmin_key(module.params['con_sysadmin_public_key'])))

    if module.params.get('con_ovf_properties', None):
        for key in module.params['con_ovf_properties'].keys():
            command_tokens.append(
                '--prop:%s=%s' % (
                    key, module.params['con_ovf_properties'][key]))

    if ('con_vcenter_folder' in module.params and
            module.params['con_vcenter_folder'] is not None):
        command_tokens.append(
            '--vmFolder=%s' % module.params['con_vcenter_folder'])

    command_tokens.extend([ova_file, vi_string])
    ova_tool_result = module.run_command(command_tokens)

    if ova_tool_result[0] != 0:
        return module.fail_json(
            msg='Failed to deploy OVA, error message from ovftool is: %s '
                'for command %s' % (ova_tool_result[1], command_tokens))

    vm = None
    if is_reconfigure_vm(module):
        vm = get_vm_by_name(si, module.params['con_vm_name'])
        cspec = vim.vm.ConfigSpec()
        if is_update_cpu(module):
            cspec.numCPUs = module.params['con_number_of_cpus']
        if is_update_memory(module):
            cspec.memoryMB = module.params['con_memory']
        if is_reserve_memory(module):
            cspec.memoryAllocation = vim.ResourceAllocationInfo(
                reservation=module.params['con_memory_reserved'])
        if is_reserve_cpu(module):
            cspec.cpuAllocation = vim.ResourceAllocationInfo(
                reservation=module.params['con_cpu_reserved'])
        if is_resize_disk(module):
            disk = None
            for device in vm.config.hardware.device:
                if isinstance(device, vim.vm.device.VirtualDisk):
                    disk = device
                    break
            if disk is not None:
                disk.capacityInKB = module.params['con_disk_size'] * 1024 * 1024
                devSpec = vim.vm.device.VirtualDeviceSpec(
                    device=disk, operation="edit")
                cspec.deviceChange.append(devSpec)
        WaitForTasks([vm.Reconfigure(cspec)], si=si)

        task = vm.PowerOnVM_Task()
        WaitForTasks([task], si=si)

    if not vm:
        vm = get_vm_by_name(si, module.params['con_vm_name'])

    if not module.params['con_mgmt_ip'] and not module.params['con_mgmt_ip_v6']:
        interval = 15
        timeout = 300
        controller_ip = None
        while timeout > 0:
            controller_ip = get_vm_ip_by_network(vm, module.params['con_mgmt_network'])
            if controller_ip:
                controller_ip = controller_ip[0]
                break
            time.sleep(interval)
            timeout -= interval
    elif module.params['con_mgmt_ip_v6_enable']:
        controller_ip = module.params['con_mgmt_ip_v6']
    else:
        controller_ip = module.params['con_mgmt_ip']

    # Wait for controller tcontroller_waito come up for given con_wait_time
    if controller_ip:
        controller_up = controller_wait(controller_ip, module.params['round_wait'],
                                        module.params['con_wait_time'])
        if not controller_up:
            return module.fail_json(
                msg='Something wrong with the controller. The Controller is not in the up state.')
    return module.exit_json(changed=True, ova_tool_result=ova_tool_result)


if __name__ == "__main__":
    main()
