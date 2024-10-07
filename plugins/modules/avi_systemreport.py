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
module: avi_systemreport
author: Gaurav Rastogi (@grastogi23) <grastogi@avinetworks.com>
short_description: Module for setup of SystemReport Avi RESTful Object
description:
    - This module is used to configure SystemReport object
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
    archive_ref:
        description:
            - Relative path to the report archive file on filesystem.the archive includes exported system configuration and current object as json.
            - Field introduced in 22.1.6, 30.2.1.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
        type: str
    controller_patch_image_ref:
        description:
            - Controller patch image associated with the report.
            - It is a reference to an object of type image.
            - Field introduced in 22.1.6, 30.2.1.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
        type: str
    downloadable:
        description:
            - Indicates whether this report is downloadable as an archive.
            - Field introduced in 22.1.6, 30.2.1.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    dryrun_info:
        description:
            - Dry-run report.
            - Field introduced in 31.1.1.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
        type: dict
    events:
        description:
            - List of events associated with the report.
            - Field introduced in 22.1.6, 30.2.1.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
        type: list
        elements: dict
    image_ref:
        description:
            - System image associated with the report.
            - It is a reference to an object of type image.
            - Field introduced in 22.1.6, 30.2.1.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
        type: str
    name:
        description:
            - Name of the report derived from operation in a readable format.
            - Ex  upgrade_system_1a5c.
            - Field introduced in 22.1.6, 30.2.1.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
        type: str
    obj_state:
        description:
            - Report state combines all applicable states.
            - Ex  readiness_reports.system_readiness.state.
            - Field introduced in 22.1.6, 30.2.1.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
        type: dict
    operation:
        description:
            - Nature of operation.
            - Ex  controller upgrade, system patch, etc.
            - Field introduced in 31.1.1.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
        type: str
    readiness_reports:
        description:
            - Readiness state of the system.
            - Ex  upgrade pre-check results.
            - Field introduced in 22.1.6, 30.2.1.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
        type: list
        elements: dict
    se_patch_image_ref:
        description:
            - Se patch image associated with the report.
            - It is a reference to an object of type image.
            - Field introduced in 22.1.6, 30.2.1.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
        type: str
    summary:
        description:
            - Summary of the report.
            - Field introduced in 22.1.6, 30.2.1.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
        type: dict
    tasks:
        description:
            - List of tasks associated with the report.
            - Field introduced in 30.2.1.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
        type: list
        elements: dict
    tenant_ref:
        description:
            - Tenant uuid associated with the object.
            - It is a reference to an object of type tenant.
            - Field introduced in 22.1.6, 30.2.1.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
        type: str
    type:
        description:
            - Type of report.
            - Pre-checks, dry-run or an upgrade operation.
            - Field introduced in 31.1.1.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
        type: str
    url:
        description:
            - Avi controller URL of the object.
        type: str
    uuid:
        description:
            - Uuid identifier for the report.
            - Field introduced in 22.1.6, 30.2.1.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
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

- name: Example to create SystemReport object
  vmware.alb.avi_systemreport:
    avi_credentials: "{{ avi_credentials }}"
    state: present
    name: sample_systemreport
"""

RETURN = '''
obj:
    description: SystemReport (api/systemreport) object
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
        archive_ref=dict(type='str',),
        controller_patch_image_ref=dict(type='str',),
        downloadable=dict(type='bool',),
        dryrun_info=dict(type='dict',),
        events=dict(type='list', elements='dict',),
        image_ref=dict(type='str',),
        name=dict(type='str',),
        obj_state=dict(type='dict',),
        operation=dict(type='str',),
        readiness_reports=dict(type='list', elements='dict',),
        se_patch_image_ref=dict(type='str',),
        summary=dict(type='dict',),
        tasks=dict(type='list', elements='dict',),
        tenant_ref=dict(type='str',),
        type=dict(type='str',),
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
    return avi_ansible_api(module, 'systemreport',
                           set())


if __name__ == '__main__':
    main()
