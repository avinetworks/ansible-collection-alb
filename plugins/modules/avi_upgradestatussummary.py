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
module: avi_upgradestatussummary
author: Gaurav Rastogi (@grastogi23) <grastogi@avinetworks.com>
short_description: Module for setup of UpgradeStatusSummary Avi RESTful Object
description:
    - This module is used to configure UpgradeStatusSummary object
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
    enable_patch_rollback:
        description:
            - Check if the patch rollback is possible on this node.
            - Field introduced in 18.2.6.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    enable_rollback:
        description:
            - Check if the rollback is possible on this node.
            - Field introduced in 18.2.6.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    end_time:
        description:
            - End time of upgrade operations.
            - Field introduced in 18.2.6.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    image_ref:
        description:
            - Image uuid for identifying the current base image.
            - It is a reference to an object of type image.
            - Field introduced in 18.2.6.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    name:
        description:
            - Name of the system such as cluster name, se group name and se name.
            - Field introduced in 18.2.6.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    node_type:
        description:
            - Type of the system such as controller_cluster, se_group or se.
            - Enum options - NODE_CONTROLLER_CLUSTER, NODE_SE_GROUP, NODE_SE_TYPE.
            - Field introduced in 18.2.6.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    obj_cloud_ref:
        description:
            - Cloud that this object belongs to.
            - It is a reference to an object of type cloud.
            - Field introduced in 18.2.6.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    obj_state:
        description:
            - Current status of the upgrade operations.
            - Field introduced in 18.2.6.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: dict
    patch_image_ref:
        description:
            - Image uuid for identifying the current patch.
            - It is a reference to an object of type image.
            - Field introduced in 18.2.6.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    start_time:
        description:
            - Start time of upgrade operations.
            - Field introduced in 18.2.6.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    tasks_completed:
        description:
            - Upgrade tasks completed.
            - Field introduced in 18.2.6.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: int
    tenant_ref:
        description:
            - Tenant that this object belongs to.
            - It is a reference to an object of type tenant.
            - Field introduced in 18.2.6.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    total_tasks:
        description:
            - Total upgrade tasks.
            - Field introduced in 18.2.6.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: int
    upgrade_ops:
        description:
            - Upgrade operations requested.
            - Enum options - UPGRADE, PATCH, ROLLBACK, ROLLBACKPATCH, SEGROUP_RESUME, EVAL_UPGRADE, EVAL_PATCH, EVAL_ROLLBACK, EVAL_ROLLBACKPATCH,
            - EVAL_SEGROUP_RESUME, EVAL_RESTORE, RESTORE, UPGRADE_DRYRUN.
            - Field introduced in 18.2.6.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    url:
        description:
            - Avi controller URL of the object.
        type: str
    uuid:
        description:
            - Uuid identifier for the system such as cluster, se group and se.
            - Field introduced in 18.2.6.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    version:
        description:
            - Current base image applied to this node.
            - Field introduced in 18.2.6.
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

- name: Example to create UpgradeStatusSummary object
  vmware.alb.avi_upgradestatussummary:
    avi_credentials: "{{ avi_credentials }}"
    state: present
    name: sample_upgradestatussummary
"""

RETURN = '''
obj:
    description: UpgradeStatusSummary (api/upgradestatussummary) object
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
        enable_patch_rollback=dict(type='bool',),
        enable_rollback=dict(type='bool',),
        end_time=dict(type='str',),
        image_ref=dict(type='str',),
        name=dict(type='str',),
        node_type=dict(type='str',),
        obj_cloud_ref=dict(type='str',),
        obj_state=dict(type='dict',),
        patch_image_ref=dict(type='str',),
        start_time=dict(type='str',),
        tasks_completed=dict(type='int',),
        tenant_ref=dict(type='str',),
        total_tasks=dict(type='int',),
        upgrade_ops=dict(type='str',),
        url=dict(type='str',),
        uuid=dict(type='str',),
        version=dict(type='str',),
    )
    argument_specs.update(avi_common_argument_spec())
    module = AnsibleModule(
        argument_spec=argument_specs, supports_check_mode=True)
    if not HAS_REQUESTS:
        return module.fail_json(msg=(
            'Python requests package is not installed. '
            'For installation instructions, visit https://pypi.org/project/requests.'))
    return avi_ansible_api(module, 'upgradestatussummary',
                           set())


if __name__ == '__main__':
    main()
