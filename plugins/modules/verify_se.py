#!/usr/bin/python
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: verify_se
author: shubhamavi (@shubhamavi) <shubhamavi@vmware.com>
short_description: Module for verifying se is connected to controller
description:
    - This module is used to verify that the se is connected to controller
options:
    se_leader_ctl_ip:
        description:
            - The IP address of the controller.
        required: true
        type: str
    se_leader_ctl_username:
        description:
            - The username to login into controller api.
        required: true
        type: str
    se_leader_ctl_password:
        description:
            -The passowrd to login into the controller api.
        required: true
        type: str
    se_leader_ctl_version:
        description:
            - The version of the controller.
        required: true
        type: str
    se_cloud_name:
        description:
            - Name of cloud the SE should auto-register with.
        required: true
        type: str
    se_group_name:
        description:
            - Name of SE group the SE should reside in.
        required: true
        type: str
    se_tenant:
        description:
            - Name of se_tenant the SE should auto-register with.
        required: true
        type: str
    se_vmw_vm_name:
        description:
            - Name of a controller VM on VMWare.
        required: true
        type: str
    se_vmw_mgmt_ip:
        description:
            - Static IP for the controller.
        required: false
        type: str
    se_vmw_ovf_networks:
        description:
            - Key-Value object for specifying OVF network names.
        required: false
        type: dict
    vcenter_host:
        description:
            - Key-Value object for specifying OVF network names.
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
    max_se_up_wait:
        description:
            - max time to wait for the se to come up.
        required: false
        default: 600
        type: int
'''

EXAMPLES = """
- name: Avi SE | Verify SE Deployment
  verify_se:
    se_leader_ctl_ip: '{{ se_leader_ctl_ip }}'
    se_leader_ctl_username: '{{ se_leader_ctl_username }}'
    se_leader_ctl_password: '{{ se_leader_ctl_password }}'
    se_leader_ctl_version: '{{ se_leader_ctl_version }}'
    se_cloud_name: '{{ se_cloud_name }}'
    se_group_name: '{{ se_group_name }}'
    se_tenant: '{{ se_tenant }}'
    se_vmw_vm_name: '{{ se_vmw_vm_name }}'
    se_vmw_mgmt_ip: '{{ se_vmw_mgmt_ip }}'
    se_vmw_ovf_networks: '{{ se_vmw_ovf_networks }}'
    vcenter_host: '{{ vcenter_host }}'
    vcenter_user: '{{ vcenter_user }}'
    vcenter_password: '{{ vcenter_password }}'
    max_se_up_wait: '{{ max_se_up_wait }}'
"""

RETURN = '''
obj:
    description: Deployed and verified SE object
    returned: success, changed
    type: dict
'''


import json
import atexit
try:
    import requests
    import time
    from pyVim.connect import SmartConnectNoSSL, Disconnect
    from pyVmomi import vim
    HAS_IMPORT = True
except ImportError:
    HAS_IMPORT = False

try:
    from pkg_resources import parse_version
    import avi.sdk
    from avi.sdk.avi_api import (ApiSession, ObjectNotFound, APIError, ApiResponse,
                                 avi_timedelta, sessionDict)

    sdk_version = getattr(avi.sdk, '__version__', None)
    if ((sdk_version is None) or
            (sdk_version and
             (parse_version(sdk_version) < parse_version('17.1')))):
        # It allows the __version__ to be '' as that value is used in development builds
        raise ImportError
    HAS_AVI = True
except ImportError:
    HAS_AVI = False
from ansible.module_utils.basic import AnsibleModule


def get_vm_by_name(si, vm_name):
    '''
    Get vm instance by name
    :param si: vcenter conection instance
    :param vm_name: name of the vm
    :return: vm instance
    '''
    container = si.content.viewManager.CreateContainerView(
        si.content.rootFolder, [vim.VirtualMachine], True)
    for vm in container.view:
        if vm.name == vm_name:
            return vm
    return None


def get_vm_ip_by_network(target_vm, network):
    '''
    Try to get the IP for the network on target_vm
    :param target_vm: vm instance
    :param network: VM network name
    :return: IP address for the network if found otherwise empty string
    '''
    ip_address = ''
    for nic in target_vm.guest.net:
        if nic.network == network:
            addresses = nic.ipConfig.ipAddress
            for adr in addresses:
                if adr.state == 'preferred':
                    ip_address = adr.ipAddress
                    break
    return ip_address


def main():
    module = AnsibleModule(
        argument_spec=dict(
            se_leader_ctl_ip=dict(required=True, type='str'),
            se_leader_ctl_username=dict(required=True, type='str'),
            se_leader_ctl_password=dict(required=True, type='str', no_log=True),
            se_leader_ctl_version=dict(required=True, type='str'),
            se_cloud_name=dict(required=True, type='str'),
            se_group_name=dict(required=True, type='str'),
            se_tenant=dict(required=True, type='str'),
            se_vmw_vm_name=dict(required=True, type='str'),
            se_vmw_mgmt_ip=dict(required=False, type='str'),
            se_vmw_ovf_networks=dict(required=False, type='dict'),
            vcenter_host=dict(required=True, type='str'),
            vcenter_user=dict(required=True, type='str'),
            vcenter_password=dict(required=True, type='str', no_log=True),
            max_se_up_wait=dict(required=False, type='int', default=600),
        ),
        supports_check_mode=False,
    )

    if not HAS_AVI:
        return module.fail_json(msg=(
            'Avi python API SDK (avisdk>=17.1) is not installed. '
            'For more details visit https://github.com/avinetworks/sdk.'))

    se_mgmt_ip = ''
    se_vm_name = module.params['se_vmw_vm_name']
    my_deployed_se = None
    mgmt_network = None
    se_vm = None

    if module.params.get('se_vmw_mgmt_ip', None):
        se_mgmt_ip = module.params['se_vmw_mgmt_ip']
    elif module.params.get("se_vmw_ovf_networks", None):
        # If there is no  se_vmw_mgmt_ip provided and only se_vmw_ovf_networks is available then
        # get the SE VM instance to find DHCP IP
        ovf_networks = module.params.get("se_vmw_ovf_networks")
        if "Management" in ovf_networks:
            mgmt_network = ovf_networks["Management"]
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
            se_vm = get_vm_by_name(si, se_vm_name)
            if not se_vm:
                module.fail_json(msg='No Vm with name %s found' % se_vm)

    api = ApiSession.get_session(
        module.params['se_leader_ctl_ip'],
        module.params['se_leader_ctl_username'],
        password=module.params['se_leader_ctl_password'],
        tenant=module.params['se_tenant'])

    path = 'serviceengine'
    gparams = {
        'cloud_ref.name': module.params['se_cloud_name']
    }

    interval = 5
    retries = module.params.get("max_se_up_wait") / interval
    initial_interval = 10
    step = 0
    time.sleep(initial_interval)
    while step < retries:
        if mgmt_network and not se_mgmt_ip:
            # try to get the mgmt IP(DHCP as no se_vmw_mgmt_ip provided) for the SE if it's not present
            # If no IP found try to get the SE from controller by its name for current iteration
            se_mgmt_ip = get_vm_ip_by_network(se_vm, mgmt_network)
        rsp = api.get(path, tenant=module.params['se_tenant'],
                      params=gparams, api_version=module.params['se_leader_ctl_version'])
        rsp_data = rsp.json()
        for item in rsp_data['results']:
            if (item['name'] == se_vm_name or item['name'] == se_mgmt_ip) and item['se_connected']:
                my_deployed_se = item
                break
        if my_deployed_se is not None:
            mymsg = 'Service Engine \'%s\' is deployed and is connected to the Controller %s' % (
                my_deployed_se['name'], module.params['se_leader_ctl_ip'])
            return module.exit_json(changed=True, msg=(mymsg), se_details=my_deployed_se)
        time.sleep(interval)
        step += 1

    return module.fail_json(msg='Could not verify SE connection to the controller!')


if __name__ == "__main__":
    main()
