#!/usr/bin/python
# module_check: supported

# Copyright 2021 VMware, Inc.  All rights reserved. VMware Confidential
# SPDX-License-Identifier: Apache License 2.0

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: avi_nsxtsegmentruntime
author: Gaurav Rastogi (@grastogi23) <grastogi@avinetworks.com>
short_description: Module for setup of NsxtSegmentRuntime Avi RESTful Object
description:
    - This module is used to configure NsxtSegmentRuntime object
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
    cloud_ref:
        description:
            - Nsxt segment belongs to cloud.
            - It is a reference to an object of type cloud.
            - Field introduced in 20.1.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    dhcp6_ranges:
        description:
            - V6 dhcp ranges configured in nsxt.
            - Field introduced in 20.1.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: list
        elements: str
    dhcp_enabled:
        description:
            - Ip address management scheme for this segment associated network.
            - Field introduced in 20.1.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as True.
        type: bool
    dhcp_ranges:
        description:
            - Dhcp ranges configured in nsxt.
            - Field introduced in 20.1.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: list
        elements: str
    name:
        description:
            - Segment object name.
            - Field introduced in 20.1.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    nw_name:
        description:
            - Network name.
            - Field introduced in 20.1.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    nw_ref:
        description:
            - Corresponding network object in avi.
            - It is a reference to an object of type network.
            - Field introduced in 20.1.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    opaque_network_id:
        description:
            - Opaque network id.
            - Field introduced in 20.1.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    origin_id:
        description:
            - Origin id applicable to security only cloud.
            - Field introduced in 22.1.2.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: str
    security_only_nsxt:
        description:
            - Nsxt segment belongs to security only cloud.
            - Field introduced in 22.1.2.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    segment_gw:
        description:
            - Segment gateway.
            - Field introduced in 20.1.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    segment_gw6:
        description:
            - V6 segment gateway.
            - Field introduced in 20.1.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    segment_id:
        description:
            - Segment id.
            - Field introduced in 20.1.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    segname:
        description:
            - Segment name.
            - Field introduced in 20.1.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    subnet:
        description:
            - Segment cidr.
            - Field introduced in 20.1.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    subnet6:
        description:
            - V6 segment cidr.
            - Field introduced in 20.1.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    tenant_ref:
        description:
            - Nsxt segment belongs to tenant.
            - It is a reference to an object of type tenant.
            - Field introduced in 20.1.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    tier1_id:
        description:
            - Tier1 router id.
            - Field introduced in 20.1.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    url:
        description:
            - Avi controller URL of the object.
        type: str
    uuid:
        description:
            - Uuid.
            - Field introduced in 20.1.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    vlan_ids:
        description:
            - Segment vlan ids.
            - Field introduced in 20.1.5.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: list
        elements: str
    vrf_context_ref:
        description:
            - Corresponding vrf context object in avi.
            - It is a reference to an object of type vrfcontext.
            - Field introduced in 20.1.1.
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

- name: Example to create NsxtSegmentRuntime object
  vmware.alb.avi_nsxtsegmentruntime:
    avi_credentials: "{{ avi_credentials }}"
    state: present
    name: sample_nsxtsegmentruntime
"""

RETURN = '''
obj:
    description: NsxtSegmentRuntime (api/nsxtsegmentruntime) object
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
        cloud_ref=dict(type='str',),
        dhcp6_ranges=dict(type='list', elements='str',),
        dhcp_enabled=dict(type='bool',),
        dhcp_ranges=dict(type='list', elements='str',),
        name=dict(type='str',),
        nw_name=dict(type='str',),
        nw_ref=dict(type='str',),
        opaque_network_id=dict(type='str',),
        origin_id=dict(type='str',),
        security_only_nsxt=dict(type='bool',),
        segment_gw=dict(type='str',),
        segment_gw6=dict(type='str',),
        segment_id=dict(type='str',),
        segname=dict(type='str',),
        subnet=dict(type='str',),
        subnet6=dict(type='str',),
        tenant_ref=dict(type='str',),
        tier1_id=dict(type='str',),
        url=dict(type='str',),
        uuid=dict(type='str',),
        vlan_ids=dict(type='list', elements='str',),
        vrf_context_ref=dict(type='str',),
    )
    argument_specs.update(avi_common_argument_spec())
    module = AnsibleModule(
        argument_spec=argument_specs, supports_check_mode=True)
    if not HAS_REQUESTS:
        return module.fail_json(msg=(
            'Python requests package is not installed. '
            'For installation instructions, visit https://pypi.org/project/requests.'))
    return avi_ansible_api(module, 'nsxtsegmentruntime',
                           set())


if __name__ == '__main__':
    main()
