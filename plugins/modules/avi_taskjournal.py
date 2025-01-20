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
module: avi_taskjournal
author: Gaurav Rastogi (@grastogi23) <grastogi@avinetworks.com>
short_description: Module for setup of TaskJournal Avi RESTful Object
description:
    - This module is used to configure TaskJournal object
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
    errors:
        description:
            - List of errors in the process.
            - Field introduced in 30.2.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: list
        elements: dict
    image_ref:
        description:
            - Image uuid for identifying the current base image.
            - It is a reference to an object of type image.
            - Field introduced in 30.2.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: str
    info:
        description:
            - Detailed information of journal.
            - Field introduced in 30.2.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: dict
    name:
        description:
            - Name for the task journal.
            - Field introduced in 30.2.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: str
    obj_cloud_ref:
        description:
            - Cloud that this object belongs to.
            - It is a reference to an object of type cloud.
            - Field introduced in 30.2.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: str
    operation:
        description:
            - Operation for which the task journal created.
            - Field introduced in 30.2.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: str
    patch_image_ref:
        description:
            - Image uuid for identifying the current patch.
            - It is a reference to an object of type image.
            - Field introduced in 30.2.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: str
    summary:
        description:
            - Summary of journal.
            - Field introduced in 30.2.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        required: true
        type: dict
    tasks:
        description:
            - List of all the tasks executed with details.
            - For example, details of tasks to be executed for upgrade filecopy.
            - Field introduced in 31.1.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: list
        elements: dict
    tenant_ref:
        description:
            - Tenant uuid associated with the object.
            - It is a reference to an object of type tenant.
            - Field introduced in 30.2.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: str
    url:
        description:
            - Avi controller URL of the object.
        type: str
    uuid:
        description:
            - Uuid identifier for the task journal.
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

- name: Example to create TaskJournal object
  vmware.alb.avi_taskjournal:
    avi_credentials: "{{ avi_credentials }}"
    state: present
    name: sample_taskjournal
"""

RETURN = '''
obj:
    description: TaskJournal (api/taskjournal) object
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
        errors=dict(type='list', elements='dict',),
        image_ref=dict(type='str',),
        info=dict(type='dict',),
        name=dict(type='str',),
        obj_cloud_ref=dict(type='str',),
        operation=dict(type='str',),
        patch_image_ref=dict(type='str',),
        summary=dict(type='dict', required=True),
        tasks=dict(type='list', elements='dict',),
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
    return avi_ansible_api(module, 'taskjournal',
                           set())


if __name__ == '__main__':
    main()
