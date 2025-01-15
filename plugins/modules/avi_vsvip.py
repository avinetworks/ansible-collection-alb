#!/usr/bin/python
# module_check: supported

# Avi Version: 17.1.2
# Copyright 2021 VMware, Inc.  All rights reserved. VMware Confidential
# SPDX-License-Identifier: Apache License 2.0

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: avi_vsvip
author: Gaurav Rastogi (@grastogi23) <grastogi@avinetworks.com>
short_description: Module for setup of VsVip Avi RESTful Object
description:
    - This module is used to configure VsVip object
    - more examples at U(https://github.com/avinetworks/devops)
options:
    state:
        description:
            - The state that should be applied on the entity.
        default: present
        choices: ["absent", "present"]
        type: str
    avi_api_update_method:
        description:
            - Default method for object update is HTTP PUT.
            - Setting to patch will override that behavior to use HTTP PATCH.
        default: put
        choices: ["put", "patch"]
        type: str
    avi_api_patch_op:
        description:
            - Patch operation to use when using avi_api_update_method as patch.
        choices: ["add", "replace", "delete", "remove"]
        type: str
    avi_patch_path:
        description:
            - Patch path to use when using avi_api_update_method as patch.
        type: str
    avi_patch_value:
        description:
            - Patch value to use when using avi_api_update_method as patch.
        type: str
    bgp_local_preference:
        description:
            - Local_pref to be used for vsvip advertised.
            - Applicable only over ibgp.
            - Field introduced in 30.2.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: int
    bgp_num_as_path_prepend:
        description:
            - Number of times the local as should be prepended additionally to vsvip.
            - Applicable only over ebgp.
            - Allowed values are 1-10.
            - Field introduced in 30.2.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: int
    bgp_peer_labels:
        description:
            - Select bgp peers, using peer label, for vsvip advertisement.
            - Field introduced in 20.1.5.
            - Maximum of 128 items allowed.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: list
        elements: str
    cloud_ref:
        description:
            - It is a reference to an object of type cloud.
            - Field introduced in 17.1.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    configpb_attributes:
        description:
            - Protobuf versioning for config pbs.
            - Field introduced in 21.1.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: dict
    dns_info:
        description:
            - Service discovery specific data including fully qualified domain name, type and time-to-live of the dns record.
            - This takes effect only if dns profile isassociated with cloud.
            - Field introduced in 17.1.1.
            - Maximum of 1000 items allowed.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: list
        elements: dict
    east_west_placement:
        description:
            - Force placement on all service engines in the service engine group (container clouds only).
            - Field introduced in 17.1.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Allowed in essentials (allowed values- false), basic (allowed values- false) edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    ipam_selector:
        description:
            - Determines the set of ipam networks to use for this vsvip.
            - Selector type must be selector_ipam and only one label is supported.
            - Field introduced in 20.1.3.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: dict
    markers:
        description:
            - List of labels to be used for granular rbac.
            - Field introduced in 20.1.5.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: list
        elements: dict
    name:
        description:
            - Name for the vsvip object.
            - Field introduced in 17.1.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        required: true
        type: str
    tenant_ref:
        description:
            - It is a reference to an object of type tenant.
            - Field introduced in 17.1.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    tier1_lr:
        description:
            - This sets the placement scope of virtualservice to given tier1 logical router in nsx-t.
            - Field introduced in 20.1.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    url:
        description:
            - Avi controller URL of the object.
        type: str
    use_standard_alb:
        description:
            - This overrides the cloud level default and needs to match the se group value in which it will be used if the se group use_standard_alb value is
            - set.
            - This is only used when fip is used for vs on azure cloud.
            - Field deprecated in 31.1.1.
            - Field introduced in 18.2.3.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: bool
    uuid:
        description:
            - Uuid of the vsvip object.
            - Field introduced in 17.1.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    vip:
        description:
            - List of virtual service ips and other shareable entities.
            - Field introduced in 17.1.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: list
        elements: dict
    vrf_context_ref:
        description:
            - Virtual routing context that the virtual service is bound to.
            - This is used to provide the isolation of the set of networks the application is attached to.
            - It is a reference to an object of type vrfcontext.
            - Field introduced in 17.1.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    vsvip_cloud_config_cksum:
        description:
            - Checksum of cloud configuration for vsvip.
            - Internally set by cloud connector.
            - Field introduced in 17.2.9, 18.1.2.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
extends_documentation_fragment:
    - vmware.alb.avi
'''

EXAMPLES = """
- hosts: all
  vars:
    avi_credentials:
      username: "admin"
      password: "something"
      controller: "192.168.15.18"
      api_version: "21.1.1"

- name: Create vsvip for virtualservice for newtestvs
  vmware.alb.avi_vsvip:
    name: vsvip-newtestvs-Default-Cloud
    avi_credentials: "{{ avi_credentials }}"
    api_context: '{{avi_api_context | default(omit)}}'
    vrf_context_ref: /api/vrfcontext/?name=global
    tenant_ref: /api/tenant/?name=admin
    cloud_ref: /api/cloud/?name=Default-Cloud
    vip:
    - vip_id: '1'
      avi_allocated_fip: false
      auto_allocate_ip: false
      enabled: true
      auto_allocate_floating_ip: false
      avi_allocated_vip: false
      auto_allocate_ip_type: V4_ONLY
      ip_address:
        type: V4
        addr: 192.168.138.18
"""

RETURN = '''
obj:
    description: VsVip (api/vsvip) object
    returned: success, changed
    type: dict
'''

from ansible.module_utils.basic import AnsibleModule
try:
    from ansible_collections.vmware.alb.plugins.module_utils.utils.ansible_utils import (
        avi_common_argument_spec, avi_ansible_api)
    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False


def main():
    argument_specs = dict(
        state=dict(default='present',
                   choices=['absent', 'present']),
        avi_api_update_method=dict(default='put',
                                   choices=['put', 'patch']),
        avi_api_patch_op=dict(choices=['add', 'replace', 'delete', 'remove']),
        avi_patch_path=dict(type='str',),
        avi_patch_value=dict(type='str',),
        bgp_local_preference=dict(type='int',),
        bgp_num_as_path_prepend=dict(type='int',),
        bgp_peer_labels=dict(type='list', elements='str',),
        cloud_ref=dict(type='str',),
        configpb_attributes=dict(type='dict',),
        dns_info=dict(type='list', elements='dict',),
        east_west_placement=dict(type='bool',),
        ipam_selector=dict(type='dict',),
        markers=dict(type='list', elements='dict',),
        name=dict(type='str', required=True),
        tenant_ref=dict(type='str',),
        tier1_lr=dict(type='str',),
        url=dict(type='str',),
        use_standard_alb=dict(type='bool',),
        uuid=dict(type='str',),
        vip=dict(type='list', elements='dict',),
        vrf_context_ref=dict(type='str',),
        vsvip_cloud_config_cksum=dict(type='str',),
    )
    argument_specs.update(avi_common_argument_spec())
    module = AnsibleModule(
        argument_spec=argument_specs, supports_check_mode=True)
    if not HAS_REQUESTS:
        return module.fail_json(msg=(
            'Python requests package is not installed. '
            'For installation instructions, visit https://pypi.org/project/requests.'))
    return avi_ansible_api(module, 'vsvip',
                           set())


if __name__ == '__main__':
    main()
