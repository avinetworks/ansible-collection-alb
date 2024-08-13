#!/usr/bin/python
# module_check: supported

# Copyright 2021 VMware, Inc. All rights reserved. VMware Confidential
# SPDX-License-Identifier: Apache License 2.0


from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: avi_update_se_data_vnics
author: Shrikant Chaudhari (@gitshrikant) <shrikant.chaudhari@avinetworks.com>
short_description: Avi API Module for update data vnics and vlan interfaces.
description:
    - Module to update Service Engine's data vnics/vlans configurations.
options:
    se_name:
        description:
            - Name of the Service Engine for which data vnics to be updated
        required: true
        type: str
    data_vnics_config:
        description:
            - Placeholder for description of property data_vnics of obj type ServiceEngine field.
              Here you can specify configuration for data_vnics property of a service engine.
              For more details you can refer to swagger specs https://{controller_ip}/swagger/
              From above link you can find configurable fields under data_vnics property of a service engine.
        type: list
        elements: dict
extends_documentation_fragment:
    - vmware.alb.avi
'''

EXAMPLES = '''
  - name: Update data vnics and vlan interfaces
    vmware.alb.avi_update_se_data_vnics:
      avi_credentials:
        controller: "{{ controller }}"
        username: "{{ username }}"
        password: "{{ password }}"
        api_version: "{{ api_version }}"
      se_name: "10.10.20.30"
      data_vnics_config:
      - if_name: "eth1"
        is_asm: false
        can_se_dp_takeover: true
        is_hsm: false
        is_avi_internal_network: false
        enabled: true
        dhcp_enabled: false
        del_pending: false
        linux_name: "eth3"
        is_mgmt: false
        connected: true
        vlan_interfaces:
          - dhcp_enabled: true
            if_name: "eth3"
            ip6_autocfg_enabled: false
            is_mgmt: false
            vlan_id: 0
            vnic_networks:
              - ip:
                  ip_addr:
                    addr: "10.161.56.155"
                    type: "V4"
                  mask: 24
                mode: "STATIC"
                ctlr_alloc: false
            vrf_ref: "https://10.10.28.102/api/vrfcontext/vrfcontext-47f8a632-3ab4-427d-9084-433bc06da26d"
        vnic_networks:
          - ip:
              ip_addr:
                addr: "10.161.56.154"
                type: "V4"
              mask: 24
            mode: "STATIC"
            ctlr_alloc: false
        vrf_id: 0
        aggregator_chgd: false
        mtu: 1500
        vrf_ref: "https://10.10.28.102/api/vrfcontext/vrfcontext-47f8a632-3ab4-427d-9084-433bc06da26d"
        ip6_autocfg_enabled: false
        vlan_id: 0
        is_portchannel: false
'''

RETURN = '''
obj:
    description: Avi REST resource
    returned: success, changed
    type: dict
'''

from ansible.module_utils.basic import AnsibleModule
try:
    from ansible_collections.vmware.alb.plugins.module_utils.utils.ansible_utils import (
        avi_common_argument_spec, ansible_return, avi_ansible_api, avi_obj_cmp,
        cleanup_absent_fields)
    from ansible_collections.vmware.alb.plugins.module_utils.avi_api import (
        ApiSession, AviCredentials)
    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False


def main():
    argument_specs = dict(
        data_vnics_config=dict(type='list', elements='dict',),
        se_name=dict(type='str', required=True),
    )
    argument_specs.update(avi_common_argument_spec())
    module = AnsibleModule(
        argument_spec=argument_specs, supports_check_mode=True)
    if not HAS_REQUESTS:
        return module.fail_json(msg=(
            'Python requests package is not installed. '
            'For installation instructions, visit https://pypi.org/project/requests.'))
    # Create controller session
    api_creds = AviCredentials()
    api_creds.update_from_ansible_module(module)
    api = ApiSession.get_session(
        api_creds.controller, api_creds.username, password=api_creds.password,
        timeout=api_creds.timeout, tenant=api_creds.tenant,
        tenant_uuid=api_creds.tenant_uuid, token=api_creds.token,
        port=api_creds.port)
    path = 'serviceengine'
    # Get existing SE object
    se_obj = api.get_object_by_name(
        path, module.params['se_name'], api_version=api_creds.api_version)
    data_vnics_config = module.params['data_vnics_config']
    for d_vnic in se_obj['data_vnics']:
        for obj in data_vnics_config:
            config_for = obj.get('if_name', None)
            if not config_for:
                return module.fail_json(msg=(
                    "if_name in a configuration is mandatory. Please provide if_name i.e. vnic's interface name."))
            if config_for == d_vnic['if_name']:
                # modify existing object
                for key, val in obj.items():
                    d_vnic[key] = val
            if config_for == d_vnic['if_name']:
                for key, val in obj.items():
                    d_vnic[key] = val
    module.params.update(se_obj)
    module.params.update(
        {
            'avi_api_update_method': 'put',
            'state': 'present'
        }
    )
    module.params.pop('data_vnics_config')
    return avi_ansible_api(module, 'serviceengine',
                           set([]))


if __name__ == '__main__':
    main()
