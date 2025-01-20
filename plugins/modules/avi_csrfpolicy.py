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
module: avi_csrfpolicy
author: Gaurav Rastogi (@grastogi23) <grastogi@avinetworks.com>
short_description: Module for setup of CSRFPolicy Avi RESTful Object
description:
    - This module is used to configure CSRFPolicy object
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
    configpb_attributes:
        description:
            - Protobuf versioning for config pbs.
            - Field introduced in 30.2.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: dict
    cookie_name:
        description:
            - Name of the cookie to be used for csrf token.
            - Field introduced in 30.2.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as X-CSRF-TOKEN.
        type: str
    csrf_file_ref:
        description:
            - The file object that contains csrf javascript content.
            - Must be of type 'csrf'.
            - It is a reference to an object of type fileobject.
            - Field introduced in 31.1.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: str
    description:
        description:
            - Human-readable description of this csrf protection policy.
            - Field introduced in 30.2.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: str
    name:
        description:
            - The name of this csrf protection policy.
            - Field introduced in 30.2.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        required: true
        type: str
    rules:
        description:
            - Rules to control which requests undergo csrf protection.if the client's request doesn't match with any rules matchtarget, bypass_csrf action is
            - applied.
            - Field introduced in 30.2.1.
            - Minimum of 1 items required.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        required: true
        type: list
        elements: dict
    tenant_ref:
        description:
            - The unique identifier of the tenant to which this policy belongs.
            - It is a reference to an object of type tenant.
            - Field introduced in 30.2.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: str
    token_validity_time_min:
        description:
            - A csrf token is rotated when this amount of time has passed.
            - Even after that, tokens will be accepted until twice this amount of time has passed.
            - Note, however, that other timeouts from the underlying session layer also affect how long a given token can be used.
            - A token will be invalidated (rotated or deleted) after one of 'token_validity_time_min' (this value), 'session_establishment_timeout',
            - 'session_idle_timeout', 'session_maximum_timeout' is reached, whichever occurs first.
            - Allowed values are 10-1440.
            - Special values are 0- unlimited.
            - Field introduced in 30.2.1.
            - Unit is min.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 360.
        type: int
    url:
        description:
            - Avi controller URL of the object.
        type: str
    uuid:
        description:
            - A unique identifier to this csrf protection policy.
            - Field introduced in 30.2.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
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

- name: Example to create CSRFPolicy object
  vmware.alb.avi_csrfpolicy:
    avi_credentials: "{{ avi_credentials }}"
    state: present
    name: sample_csrfpolicy
"""

RETURN = '''
obj:
    description: CSRFPolicy (api/csrfpolicy) object
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
        configpb_attributes=dict(type='dict',),
        cookie_name=dict(type='str',),
        csrf_file_ref=dict(type='str',),
        description=dict(type='str',),
        name=dict(type='str', required=True),
        rules=dict(type='list', elements='dict', required=True),
        tenant_ref=dict(type='str',),
        token_validity_time_min=dict(type='int',),
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
    return avi_ansible_api(module, 'csrfpolicy',
                           set())


if __name__ == '__main__':
    main()
