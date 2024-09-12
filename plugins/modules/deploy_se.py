#!/usr/bin/python
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: deploy_se
author: shubhamavi (@shubhamavi) <shubhamavi@vmware.com>
short_description: Module for deploying se
description:
    - This module is used to deploy an se
options:
    ovftool_path:
        description:
            - The path of ovftool.
        required: true
        type: str
    vcenter_host:
        description:
            - VMWare host IP.
        required: true
        type: str
    vcenter_user:
        description:
            - VMWare user name.
        required: true
        type: str
    vcenter_password:
        description:
            - VMWare password.
        required: true
        type: str
    ssl_verify:
        description:
            - ovftool sslverify option.
        required: false
        default: false
        type: bool
    state:
        description:
            - The state that should be applied on the entity.
        required: false
        default: present
        type: str
    se_vmw_host:
        description:
            - Name of VMWare host.
        required: false
        type: str
    se_vmw_datacenter:
        description:
            - Name of VMWare datacenter.
        required: false
        type: str
    se_vmw_cluster:
        description:
            - Name of a cluster in the datacenter.
        required: false
        type: str
    se_vmw_datastore:
        description:
            - Name of datastore on which VM to be deployed.
        required: false
        type: str
    se_vmw_ovf_networks:
        description:
            - Key-Value object for specifying OVF network names.
        required: false
        type: dict
    se_vmw_disk_mode:
        description:
            - Deployment disk mode.
        required: false
        default: thin
        type: str
    se_vmw_ova_path:
        description:
            - Relative or absolute location of the SE ova (includes ova filename). If specified the OVA file will not be downloaded.
        required: true
        type: str
    se_vmw_vm_name:
        description:
            - Name of a controller VM on VMWare.
        required: true
        type: str
    se_vmw_power_on:
        description:
            - VM to be powered on after provisioning.
        required: false
        default: true
        type: bool
    se_vmw_vcenter_folder:
        description:
            - Folder path to deploy VM.
        required: false
        type: str
    se_vmw_mgmt_ip:
        description:
            - Static IP for the controller.
        required: false
        type: str
    se_vmw_mgmt_mask:
        description:
            - Management IP Mask.
        required: false
        type: str
    se_vmw_default_gw:
        description:
            - Default gateway of management network.
        required: false
        type: str
    se_vmw_sysadmin_public_key:
        description:
            - Public key file path.
        required: false
        type: str
    se_auth_token:
        description:
            - If defined it will be the token used to register the service engine to the controller.
        required: true
        type: str
    se_cluster_uuid:
        description:
            - If defined it will be the cluster UUID used to register the service engine to the controller.
        required: true
        type: str
    se_leader_ctl_ip:
        description:
            - The IP address of the controller.
        required: true
        type: str
    se_vmw_number_of_cpus:
        description:
            - Number of CPUs for controller.
        required: false
        type: int
    se_vmw_cpu_reserved:
        description:
            - CPU reservation in megahertz.
        required: false
        type: int
    se_vmw_memory:
        description:
            - Controller memory in MB.
        required: false
        type: int
    se_vmw_memory_reserved:
        description:
            - Controller memory reservation in MB.
        required: false
        type: int
    se_vmw_disk_size:
        description:
            - Controller disk size in GB.
        required: false
        type: int
    se_vmw_ovf_properties:
        description:
            - Other Controller ovf properties in key value format.
        required: false
        type: dict
'''

EXAMPLES = """

- name: Avi SE | VMware | Deploy SE VM
  deploy_se:
    ovftool_path: '{{ ovftool_path }}'
    vcenter_host: '{{ vcenter_host }}'
    vcenter_user: '{{ vcenter_user }}'
    vcenter_password: '{{ vcenter_password }}'
    ssl_verify: '{{ ssl_verify }}'
    state: '{{ state }}'
    se_vmw_datacenter: '{{ se_vmw_datacenter }}'
    se_vmw_cluster: '{{ se_vmw_cluster }}'
    se_vmw_datastore: '{{ se_vmw_datastore }}'
    se_vmw_ovf_networks: '{{ se_vmw_ovf_networks }}'
    se_vmw_disk_mode: '{{ se_vmw_disk_mode }}'
    se_vmw_ova_path: '{{ se_vmw_ova_path }}'
    se_vmw_vm_name: '{{ se_vmw_vm_name }}'
    se_vmw_power_on: '{{ se_vmw_power_on }}'
    se_vmw_vcenter_folder: '{{ se_vmw_vcenter_folder }}'
    se_vmw_mgmt_ip: '{{ se_vmw_mgmt_ip }}'
    se_vmw_mgmt_mask: '{{ se_vmw_mgmt_mask }}'
    se_vmw_default_gw: '{{ se_vmw_default_gw }}'
    se_vmw_sysadmin_public_key: '{{ se_vmw_sysadmin_public_key }}'
    se_auth_token: '{{ se_auth_token }}'
    se_cluster_uuid: '{{ se_cluster_uuid }}'
    se_leader_ctl_ip: '{{ se_leader_ctl_ip }}'
    se_vmw_number_of_cpus: '{{ se_vmw_number_of_cpus }}'
    se_vmw_cpu_reserved: '{{ se_vmw_cpu_reserved }}'
    se_vmw_memory: '{{ se_vmw_memory }}'
    se_vmw_memory_reserved: '{{ se_vmw_memory_reserved }}'
    se_vmw_disk_size: '{{ se_vmw_disk_size }}'
    se_vmw_ovf_properties: '{{ se_vmw_ovf_properties }}'
"""

RETURN = '''
obj:
    description: Deployed SE object
    returned: success, changed
    type: dict
'''


import atexit
import json
try:
    from urllib import quote
except ImportError:
    from urllib.parse import quote
try:
    import requests
    import os
    import time
    from pyVim.connect import SmartConnectNoSSL, Disconnect
    from pyVmomi import vim, vmodl
    HAS_IMPORT = True
except ImportError:
    HAS_IMPORT = False

from ansible.module_utils.basic import AnsibleModule
__author__ = 'shubhamavi'


def is_vm_exist(si, cl, vm_name):
    container = si.content.viewManager.CreateContainerView(cl, [vim.VirtualMachine], True)
    for managed_object_ref in container.view:
        if managed_object_ref.name == vm_name:
            return True
    return False


def get_vm_by_name(si, vm_name):
    container = si.content.viewManager.CreateContainerView(
        si.content.rootFolder, [vim.VirtualMachine], True)
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


def get_ds(dc, name, inst_type='datacenter'):
    """
    Pick a datastore by its name from datacenter or host.
    :param dc: datacenter or host instance
    :param name: Name of the datastore
    :param inst_type: type of the instance datacenter/host
    :return:
    """
    for ds in dc.datastore:
        try:
            if ds.name == name:
                return ds
        except Exception as e:  # Ignore datastores that have issues
            # pylint: disable=bare-except
            pass
    raise Exception("Failed to find %s on %s %s" % (name, inst_type, dc.name))


def get_host(cl, name):
    """
    Pick a datastore by its name.
    """
    for host in cl.host:
        try:
            if host.name == name:
                return host
        except Exception as e:  # Ignore hosts that have issues
            pass
    raise Exception("Failed to find %s host on cluster %s" % (name, cl.name))


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
        except Exception as e:  # Ignore datastores that have issues
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


def is_update_cpu(module):
    return ('se_vmw_number_of_cpus' in module.params and
            module.params['se_vmw_number_of_cpus'] is not None)


def is_update_memory(module):
    return ('se_vmw_memory' in module.params and
            module.params['se_vmw_memory'] is not None)


def is_reserve_memory(module):
    return ('se_vmw_memory_reserved' in module.params and
            module.params['se_vmw_memory_reserved'] is not None)


def is_reserve_cpu(module):
    return ('se_vmw_cpu_reserved' in module.params and
            module.params['se_vmw_cpu_reserved'] is not None)


def is_resize_disk(module):
    return ('se_vmw_disk_size' in module.params and
            module.params['se_vmw_disk_size'] is not None)


def is_reconfigure_vm(module):
    return (is_update_cpu(module) or is_update_memory(module) or
            is_reserve_memory(module) or is_reserve_cpu(module) or
            is_resize_disk(module))


def main():
    module = AnsibleModule(
        argument_spec=dict(
            ovftool_path=dict(required=True, type='str'),
            vcenter_host=dict(required=True, type='str'),
            vcenter_user=dict(required=True, type='str'),
            vcenter_password=dict(required=True, type='str', no_log=True),
            ssl_verify=dict(required=False, type='bool', default=False),
            state=dict(required=False, type='str', default='present'),
            se_vmw_host=dict(required=False, type='str'),
            se_vmw_datacenter=dict(required=False, type='str'),
            se_vmw_cluster=dict(required=False, type='str'),
            se_vmw_datastore=dict(required=False, type='str'),
            se_vmw_ovf_networks=dict(required=False, type='dict'),
            se_vmw_disk_mode=dict(required=False, type='str', default='thin'),
            se_vmw_ova_path=dict(required=True, type='str'),
            se_vmw_vm_name=dict(required=True, type='str'),
            se_vmw_power_on=dict(required=False, type='bool', default=True),
            se_vmw_vcenter_folder=dict(required=False, type='str'),
            se_vmw_mgmt_ip=dict(required=False, type='str'),
            se_vmw_mgmt_mask=dict(required=False, type='str'),
            se_vmw_default_gw=dict(required=False, type='str'),
            se_vmw_sysadmin_public_key=dict(required=False, type='str'),
            se_auth_token=dict(required=True, type='str'),
            se_cluster_uuid=dict(required=True, type='str'),
            se_leader_ctl_ip=dict(required=True, type='str'),
            se_vmw_number_of_cpus=dict(required=False, type='int'),
            se_vmw_cpu_reserved=dict(required=False, type='int'),
            se_vmw_memory=dict(required=False, type='int'),
            se_vmw_memory_reserved=dict(required=False, type='int'),
            se_vmw_disk_size=dict(required=False, type='int'),
            se_vmw_ovf_properties=dict(required=False, type='dict'),
        ),
        supports_check_mode=True,
    )

    try:
        si = SmartConnectNoSSL(host=module.params['vcenter_host'],
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
        vm = get_vm_by_name(si, module.params['se_vmw_vm_name'])

        if vm is None:
            return module.exit_json(msg='A VM with the name %s not found' % (
                module.params['se_vmw_vm_name']))

        if check_mode:
            return module.exit_json(msg='A VM with the name %s found' % (
                module.params['se_vmw_vm_name']), changed=True)

        if vm.runtime.powerState == vim.VirtualMachinePowerState.poweredOn:
            task = vm.PowerOffVM_Task()
            wait_for_tasks(si, [task])

        task = vm.Destroy_Task()
        wait_for_tasks(si, [task])

        return module.exit_json(msg='A VM with the name %s deleted successfully'
                                    % (module.params['se_vmw_vm_name']),
                                changed=True)

    if module.params.get('se_vmw_datacenter', None):
        dc = get_dc(si, module.params['se_vmw_datacenter'])
    else:
        dc = si.content.rootFolder.childEntity[0]

    if module.params.get('se_vmw_cluster', None):
        cl = get_cluster(si, dc, module.params['se_vmw_cluster'])
    else:
        cl = get_first_cluster(si, dc)

    host_name = module.params.get('se_vmw_host', None)
    datastore_name = module.params.get('se_vmw_datastore', None)
    if host_name and datastore_name:
        host = get_host(cl, host_name)
        ds = get_ds(host, datastore_name, inst_type='host')
    elif host_name:
        host = get_host(cl, host_name)
        ds = get_largest_free_ds(host)
    elif datastore_name:
        ds = get_ds(cl, datastore_name, inst_type="datacenter")
    else:
        ds = get_largest_free_ds(cl)

    if is_vm_exist(si, cl, module.params['se_vmw_vm_name']):
        vm = get_vm_by_name(si, module.params['se_vmw_vm_name'])
        vm_path = compile_folder_path_for_object(vm)
        folder = get_folder_by_path(si, dc, module.params['se_vmw_vcenter_folder'])
        folder_path = compile_folder_path_for_object(folder)
        changed = False
        if vm_path != folder_path:
            # migrate vm to new folder
            if not check_mode:
                folder.MoveInto([vm])
            changed = True
        if (not module.params['se_vmw_power_on']) and \
                vm.runtime.powerState == vim.VirtualMachinePowerState.poweredOn:
            if not check_mode:
                task = vm.PowerOffVM_Task()
                wait_for_tasks(si, [task])
            changed = True
        if module.params['se_vmw_power_on'] and vm.runtime.powerState == \
                vim.VirtualMachinePowerState.poweredOff:
            if not check_mode:
                task = vm.PowerOnVM_Task()
                wait_for_tasks(si, [task])
            changed = True

        if module.params.get('se_vmw_datastore', None):
            ds_names = []
            for datastore in vm.datastore:
                ds_names.append(datastore.name)
            if ds.name not in ds_names:
                module.fail_json(msg='VM datastore cant be modified')

        if module.params.get('se_vmw_mgmt_ip', None):
            ip_addresses = get_vm_ips(vm)
            if (ip_addresses and
                    not module.params['se_vmw_mgmt_ip'] in ip_addresses):
                module.fail_json(msg='VM static ip address cant be modified')
        if changed and not check_mode:
            module.exit_json(msg='A VM with the name %s updated successfully' %
                                 (module.params['se_vmw_vm_name']), changed=True)
        if changed and check_mode:
            module.exit_json(changed=True)
        else:
            module.exit_json(
                msg='A VM with the name %s is already present' % (
                    module.params['se_vmw_vm_name']))

    ova_file = module.params['se_vmw_ova_path']
    if (module.params['se_vmw_ova_path'].startswith('http')):
        if (requests.head(module.params['se_vmw_ova_path']).status_code != 200):
            module.fail_json(msg='SE OVA not found or readable from specified URL path')
    if (not os.path.isfile(ova_file) or
            not os.access(ova_file, os.R_OK)):
        module.fail_json(msg='SE OVA not found or not readable')

    ovftool_exec = '%s/ovftool' % module.params['ovftool_path']
    quoted_vcenter_user = quote(module.params['vcenter_user'])
    quoted_vcenter_password = quote(module.params['vcenter_password'])

    vi_string = 'vi://%s:%s@%s' % (
        quoted_vcenter_user, quoted_vcenter_password,
        module.params['vcenter_host'])
    vi_string += '/%s%s/%s' % (dc.name, compile_folder_path_for_object(cl),
                               cl.name)
    if host_name:
        vi_string += '/' + host_name
    command_tokens = [ovftool_exec]

    if module.params['se_vmw_power_on'] and not is_reconfigure_vm(module):
        command_tokens.append('--powerOn')
    if not module.params['ssl_verify']:
        command_tokens.append('--noSSLVerify')
    if check_mode:
        command_tokens.append('--verifyOnly')
    command_tokens.extend([
        '--acceptAllEulas',
        '--skipManifestCheck',
        '--allowExtraConfig',
        '--diskMode=%s' % module.params['se_vmw_disk_mode'],
        '--datastore=%s' % ds.name,
        '--name=%s' % module.params['se_vmw_vm_name']
    ])
    if ('se_vmw_ovf_networks' in module.params.keys() and module.params['se_vmw_ovf_networks'] is not None):
        d = module.params['se_vmw_ovf_networks']
        for key, network_item in d.items():
            command_tokens.append('--net:%s=%s' % (key, network_item))
    command_tokens.extend([
        '--prop:%s=%s' % ('AVICNTRL', module.params['se_leader_ctl_ip']),
        '--prop:%s=%s' % ('AVICNTRL_AUTHTOKEN', module.params['se_auth_token']),
        '--prop:%s=%s' % ('AVICNTRL_CLUSTERUUID', module.params['se_cluster_uuid'])
    ])

    if module.params.get('se_vmw_mgmt_ip', None):
        command_tokens.append('--prop:%s=%s' % (
            'avi.mgmt-ip.SE', module.params['se_vmw_mgmt_ip']))

    if module.params.get('se_vmw_mgmt_mask', None):
        command_tokens.append('--prop:%s=%s' % (
            'avi.mgmt-mask.SE', module.params['se_vmw_mgmt_mask']))

    if module.params.get('se_vmw_default_gw', None):
        command_tokens.append('--prop:%s=%s' % (
            'avi.default-gw.SE', module.params['se_vmw_default_gw']))

    if module.params.get('se_vmw_sysadmin_public_key', None):
        command_tokens.append('--prop:%s=%s' % (
            'avi.sysadmin-public-key.SE',
            get_sysadmin_key(module.params['se_vmw_sysadmin_public_key'])))

    if module.params.get('se_vmw_ovf_properties', None):
        for key in module.params['se_vmw_ovf_properties'].keys():
            command_tokens.append(
                '--prop:%s=%s' % (
                    key, module.params['se_vmw_ovf_properties'][key]))

    if ('se_vmw_vcenter_folder' in module.params and
            module.params['se_vmw_vcenter_folder'] is not None):
        command_tokens.append(
            '--vmFolder=%s' % module.params['se_vmw_vcenter_folder'])

    command_tokens.extend([ova_file, vi_string])
    ova_tool_result = module.run_command(command_tokens)

    if ova_tool_result[0] != 0:
        return module.fail_json(
            msg='Failed to deploy OVA, error message from ovftool is: %s '
                'for command %s' % (ova_tool_result[1], command_tokens))

    if is_reconfigure_vm(module):
        vm = get_vm_by_name(si, module.params['se_vmw_vm_name'])
        cspec = vim.vm.ConfigSpec()
        if is_update_cpu(module):
            cspec.numCPUs = module.params['se_vmw_number_of_cpus']
        if is_update_memory(module):
            cspec.memoryMB = module.params['se_vmw_memory']
        if is_reserve_memory(module):
            cspec.memoryAllocation = vim.ResourceAllocationInfo(
                reservation=module.params['se_vmw_memory_reserved'])
        if is_reserve_cpu(module):
            cspec.cpuAllocation = vim.ResourceAllocationInfo(
                reservation=module.params['se_vmw_cpu_reserved'])
        if is_resize_disk(module):
            disk = None
            for device in vm.config.hardware.device:
                if isinstance(device, vim.vm.device.VirtualDisk):
                    disk = device
                    break
            if disk is not None:
                disk.capacityInKB = module.params['se_vmw_disk_size'] * 1024 * 1024
                devSpec = vim.vm.device.VirtualDeviceSpec(
                    device=disk, operation="edit")
                cspec.deviceChange.append(devSpec)
        wait_for_tasks(si, [vm.Reconfigure(cspec)])

        task = vm.PowerOnVM_Task()
        wait_for_tasks(si, [task])

    return module.exit_json(changed=True, ova_tool_result=ova_tool_result)


if __name__ == "__main__":
    main()
