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
module: avi_upgradeprofile
author: Gaurav Rastogi (@grastogi23) <grastogi@avinetworks.com>
short_description: Module for setup of UpgradeProfile Avi RESTful Object
description:
    - This module is used to configure UpgradeProfile object
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
    controller:
        description:
            - List of controller upgrade related configurable parameters.
            - Field introduced in 31.1.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: dict
    dry_run:
        description:
            - List of dryrun related configurable parameters.
            - Field introduced in 31.1.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: dict
    image:
        description:
            - List of image related configurable parameters.
            - Field introduced in 31.1.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: dict
    pre_checks:
        description:
            - List of upgrade pre-checks related configurable parameters.
            - Field introduced in 31.1.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: dict
    service_engine:
        description:
            - List of service engine upgrade related configurable parameters.
            - Field introduced in 31.1.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: dict
    url:
        description:
            - Avi controller URL of the object.
        type: str
    uuid:
        description:
            - Uuid identifier for the upgradeprofile object.
            - Field introduced in 31.1.1.
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

- name: Example to create UpgradeProfile object
  vmware.alb.avi_upgradeprofile:
    avi_credentials: "{{ avi_credentials }}"
    state: present
    name: sample_upgradeprofile
"""

RETURN = '''
obj:
    description: UpgradeProfile (api/upgradeprofile) object
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
        controller=dict(type='dict',),
        dry_run=dict(type='dict',),
        image=dict(type='dict',),
        pre_checks=dict(type='dict',),
        service_engine=dict(type='dict',),
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
    return avi_ansible_api(module, 'upgradeprofile',
                           set())


if __name__ == '__main__':
    main()
