#!/usr/bin/python
# module_check: supported

# Avi Version: 17.1.1
# Copyright 2021 VMware, Inc.  All rights reserved. VMware Confidential
# SPDX-License-Identifier: Apache License 2.0

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: avi_networksecuritypolicy
author: Gaurav Rastogi (@grastogi23) <grastogi@avinetworks.com>
short_description: Module for setup of NetworkSecurityPolicy Avi RESTful Object
description:
    - This module is used to configure NetworkSecurityPolicy object
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
    cloud_config_cksum:
        description:
            - Checksum of cloud configuration for network sec policy.
            - Internally set by cloud connector.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    configpb_attributes:
        description:
            - Protobuf versioning for config pbs.
            - Field introduced in 21.1.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: dict
    created_by:
        description:
            - Creator name.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    description:
        description:
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    geo_db_ref:
        description:
            - Geo database.
            - It is a reference to an object of type geodb.
            - Field introduced in 21.1.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: str
    internal:
        description:
            - Network security policy is created and modified by internal modules only.
            - Should not be modified by users.
            - Field introduced in 21.1.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: bool
    ip_reputation_db_ref:
        description:
            - Ip reputation database.
            - It is a reference to an object of type ipreputationdb.
            - Field introduced in 20.1.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: str
    markers:
        description:
            - List of labels to be used for granular rbac.
            - Field introduced in 20.1.5.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: list
        elements: dict
    name:
        description:
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    rules:
        description:
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: list
        elements: dict
    tenant_ref:
        description:
            - It is a reference to an object of type tenant.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    url:
        description:
            - Avi controller URL of the object.
        type: str
    uuid:
        description:
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

- name: Create a network security policy to block clients represented by ip group known_attackers
  vmware.alb.avi_networksecuritypolicy:
    avi_credentials: "{{ avi_credentials }}"
    name: vs-gurutest-ns
    rules:
    - action: NETWORK_SECURITY_POLICY_ACTION_TYPE_DENY
      age: 0
      enable: true
      index: 1
      log: false
      match:
        client_ip:
          group_refs:
          - Demo:known_attackers
          match_criteria: IS_IN
      name: Rule 1
    tenant_ref: /api/tenant?name=Demo
"""

RETURN = '''
obj:
    description: NetworkSecurityPolicy (api/networksecuritypolicy) object
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
        cloud_config_cksum=dict(type='str',),
        configpb_attributes=dict(type='dict',),
        created_by=dict(type='str',),
        description=dict(type='str',),
        geo_db_ref=dict(type='str',),
        internal=dict(type='bool',),
        ip_reputation_db_ref=dict(type='str',),
        markers=dict(type='list', elements='dict',),
        name=dict(type='str',),
        rules=dict(type='list', elements='dict',),
        tenant_ref=dict(type='str',),
        url=dict(type='str',),
        uuid=dict(type='str',),
    )
    argument_specs.update(avi_common_argument_spec())
    module = AnsibleModule(
        argument_spec=argument_specs, supports_check_mode=True)
    if not HAS_REQUESTS:
        return module.fail_json(msg=(
            'Python requests package is not installed. '
            'For installation instructions, visit https://pypi.org/project/requests.'))
    return avi_ansible_api(module, 'networksecuritypolicy',
                           set())


if __name__ == '__main__':
    main()
