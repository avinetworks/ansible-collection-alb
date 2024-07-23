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
module: avi_upgradestatusinfo
author: Gaurav Rastogi (@grastogi23) <grastogi@avinetworks.com>
short_description: Module for setup of UpgradeStatusInfo Avi RESTful Object
description:
    - This module is used to configure UpgradeStatusInfo object
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
    after_reboot_rollback_fnc:
        description:
            - Backward compatible abort function name.
            - Field introduced in 18.2.10, 20.1.1.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: str
    after_reboot_task_name:
        description:
            - Backward compatible task dict name.
            - Field introduced in 18.2.10, 20.1.1.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: str
    clean:
        description:
            - Flag for clean installation.
            - Field introduced in 18.2.10, 20.1.1.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: bool
    duration:
        description:
            - Duration of upgrade operation in seconds.
            - Field introduced in 18.2.6.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: int
    enable_patch_rollback:
        description:
            - Check if the patch rollback is possible on this node.
            - Field introduced in 18.2.6.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    enable_rollback:
        description:
            - Check if the rollback is possible on this node.
            - Field introduced in 18.2.6.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    end_time:
        description:
            - End time of upgrade operation.
            - Field introduced in 18.2.6.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: str
    enqueue_time:
        description:
            - Enqueue time of upgrade operation.
            - Field introduced in 18.2.6.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: str
    fips_mode:
        description:
            - Fips mode for the entire system.
            - Field introduced in 20.1.5.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
        type: bool
    history:
        description:
            - Record of past operations on this node.
            - Field introduced in 20.1.4.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
        type: list
        elements: dict
    image_path:
        description:
            - Image path of current base image.
            - Field introduced in 18.2.10, 20.1.1.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: str
    image_ref:
        description:
            - Image uuid for identifying the current base image.
            - It is a reference to an object of type image.
            - Field introduced in 18.2.6.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: str
    name:
        description:
            - Name of the system such as cluster name, se group name and se name.
            - Field introduced in 18.2.6.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: str
    node_type:
        description:
            - Type of the system such as controller_cluster, se_group or se.
            - Enum options - NODE_CONTROLLER_CLUSTER, NODE_SE_GROUP, NODE_SE_TYPE.
            - Field introduced in 18.2.6.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: str
    obj_cloud_ref:
        description:
            - Cloud that this object belongs to.
            - It is a reference to an object of type cloud.
            - Field introduced in 18.2.6.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: str
    obj_state:
        description:
            - Current status of the upgrade operation.
            - Field introduced in 18.2.6.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: dict
    params:
        description:
            - Parameters associated with the upgrade operation.
            - Field introduced in 18.2.6.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: dict
    patch_image_path:
        description:
            - Image path of current patch image.
            - Field introduced in 18.2.10, 20.1.1.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: str
    patch_image_ref:
        description:
            - Image uuid for identifying the current patch.example  base-image is 18.2.6 and a patch 6p1 is applied, then this field will indicate the 6p1
            - value.
            - It is a reference to an object of type image.
            - Field introduced in 18.2.6.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: str
    patch_list:
        description:
            - List of patches applied to this node.
            - Example  base-image is 18.2.6 and a patch 6p1 is applied, then a patch 6p5 applied.
            - This field will indicate the [{'6p1', '6p1_image_uuid'}, {'6p5', '6p5_image_uuid'}] value.
            - Field introduced in 18.2.8, 20.1.1.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: list
        elements: dict
    patch_reboot:
        description:
            - Flag for patch op with reboot.
            - Field introduced in 18.2.10, 20.1.1.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: bool
    patch_version:
        description:
            - Current patch version applied to this node.
            - Example  base-image is 18.2.6 and a patch 6p1 is applied, then this field will indicate the 6p1 value.
            - Field introduced in 18.2.6.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: str
    prev_image_path:
        description:
            - Image path of previous base image.
            - Field introduced in 18.2.10, 20.1.1.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: str
    prev_patch_image_path:
        description:
            - Image path of previous patch image.
            - Field introduced in 18.2.10, 20.1.1.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: str
    prev_remote_image_ref:
        description:
            - Remote image reference of previous base image.
            - Field introduced in 30.1.1.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
        type: str
    previous_image_ref:
        description:
            - Image uuid for identifying previous base image.example  base-image was 18.2.5 and an upgrade was done to 18.2.6, then this field will indicate
            - the 18.2.5 value.
            - It is a reference to an object of type image.
            - Field introduced in 18.2.6.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: str
    previous_patch_image_ref:
        description:
            - Image uuid for identifying previous patch.example  base-image was 18.2.6 with a patch 6p1.
            - Upgrade was initiated to 18.2.8 with patch 8p1.
            - The previous_image field will contain 18.2.6 and this field will indicate the 6p1 value.
            - It is a reference to an object of type image.
            - Field introduced in 18.2.6.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: str
    previous_patch_list:
        description:
            - List of patches applied to this node on previous major version.
            - Field introduced in 18.2.8, 20.1.1.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: list
        elements: dict
    previous_patch_version:
        description:
            - Previous patch version applied to this node.example  base-image was 18.2.6 with a patch 6p1.
            - Upgrade was initiated to 18.2.8 with patch 8p1.
            - The previous_image field will contain 18.2.6 and this field will indicate the 6p1 value.
            - Field introduced in 18.2.6.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: str
    previous_version:
        description:
            - Previous version prior to upgrade.example  base-image was 18.2.5 and an upgrade was done to 18.2.6, then this field will indicate the 18.2.5
            - value.
            - Field introduced in 18.2.6.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: str
    progress:
        description:
            - Upgrade operations progress which holds value between 0-100.
            - Allowed values are 0-100.
            - Field introduced in 18.2.8, 20.1.1.
            - Unit is percent.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 0.
        type: int
    reason:
        description:
            - Descriptive reason for the upgrade state.
            - Field introduced in 22.1.3.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
        type: str
    remote_image_ref:
        description:
            - Remote image reference of current base image.
            - Field introduced in 30.1.1.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
        type: str
    se_patch_image_path:
        description:
            - Image path of se patch image.(required in case of reimage and upgrade + patch).
            - Field introduced in 18.2.10, 20.1.1.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: str
    se_patch_image_ref:
        description:
            - Image uuid for identifying the current se patch required in case of system upgrade(re-image) with se patch.
            - It is a reference to an object of type image.
            - Field introduced in 18.2.10, 20.1.1.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: str
    se_upgrade_events:
        description:
            - Serviceenginegroup upgrade errors.
            - Field introduced in 18.2.6.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: list
        elements: dict
    seg_params:
        description:
            - Se_patch may be different from the controller_patch.
            - It has to be saved in the journal for subsequent consumption.
            - The segroup params will be saved in the controller entry as seg_params.
            - Field introduced in 18.2.10, 20.1.1.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: dict
    seg_status:
        description:
            - Detailed segroup status.
            - Field introduced in 18.2.6.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: dict
    start_time:
        description:
            - Start time of upgrade operation.
            - Field introduced in 18.2.6.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: str
    statediff_ref:
        description:
            - Record of pre/post snapshot captured for current upgrade operation.
            - It is a reference to an object of type statediffoperation.
            - Field introduced in 21.1.3.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
        type: str
    system:
        description:
            - Flag is set only in the cluster if the upgrade is initiated as a system-upgrade.
            - Field introduced in 18.2.6.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: bool
    system_report_refs:
        description:
            - Tracks the list of reports created for node.
            - It is a reference to an object of type systemreport.
            - Field introduced in 22.1.6, 30.2.1.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
        type: list
        elements: str
    tasks_completed:
        description:
            - Completed set of tasks in the upgrade operation.
            - Field introduced in 18.2.6.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: int
    tenant_ref:
        description:
            - Tenant that this object belongs to.
            - It is a reference to an object of type tenant.
            - Field introduced in 18.2.6.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: str
    total_tasks:
        description:
            - Total number of tasks in the upgrade operation.
            - Field introduced in 18.2.6.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: int
    upgrade_events:
        description:
            - Events performed for upgrade operation.
            - Field introduced in 18.2.6.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: list
        elements: dict
    upgrade_ops:
        description:
            - Upgrade operations requested.
            - Enum options - UPGRADE, PATCH, ROLLBACK, ROLLBACKPATCH, SEGROUP_RESUME, EVAL_UPGRADE, EVAL_PATCH, EVAL_ROLLBACK, EVAL_ROLLBACKPATCH,
            - EVAL_SEGROUP_RESUME, EVAL_RESTORE, RESTORE.
            - Field introduced in 18.2.6.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: str
    upgrade_readiness:
        description:
            - Upgrade readiness check execution detail.
            - Field introduced in 22.1.3.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
        type: dict
    url:
        description:
            - Avi controller URL of the object.
        type: str
    uuid:
        description:
            - Uuid identifier for the system such as cluster, se group and se.
            - Field introduced in 18.2.6.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: str
    version:
        description:
            - Current base image applied to this node.
            - Field introduced in 18.2.6.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
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

- name: Example to create UpgradeStatusInfo object
  vmware.alb.avi_upgradestatusinfo:
    avi_credentials: "{{ avi_credentials }}"
    state: present
    name: sample_upgradestatusinfo
"""

RETURN = '''
obj:
    description: UpgradeStatusInfo (api/upgradestatusinfo) object
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
        after_reboot_rollback_fnc=dict(type='str',),
        after_reboot_task_name=dict(type='str',),
        clean=dict(type='bool',),
        duration=dict(type='int',),
        enable_patch_rollback=dict(type='bool',),
        enable_rollback=dict(type='bool',),
        end_time=dict(type='str',),
        enqueue_time=dict(type='str',),
        fips_mode=dict(type='bool',),
        history=dict(type='list', elements='dict',),
        image_path=dict(type='str',),
        image_ref=dict(type='str',),
        name=dict(type='str',),
        node_type=dict(type='str',),
        obj_cloud_ref=dict(type='str',),
        obj_state=dict(type='dict',),
        params=dict(type='dict',),
        patch_image_path=dict(type='str',),
        patch_image_ref=dict(type='str',),
        patch_list=dict(type='list', elements='dict',),
        patch_reboot=dict(type='bool',),
        patch_version=dict(type='str',),
        prev_image_path=dict(type='str',),
        prev_patch_image_path=dict(type='str',),
        prev_remote_image_ref=dict(type='str',),
        previous_image_ref=dict(type='str',),
        previous_patch_image_ref=dict(type='str',),
        previous_patch_list=dict(type='list', elements='dict',),
        previous_patch_version=dict(type='str',),
        previous_version=dict(type='str',),
        progress=dict(type='int',),
        reason=dict(type='str',),
        remote_image_ref=dict(type='str',),
        se_patch_image_path=dict(type='str',),
        se_patch_image_ref=dict(type='str',),
        se_upgrade_events=dict(type='list', elements='dict',),
        seg_params=dict(type='dict',),
        seg_status=dict(type='dict',),
        start_time=dict(type='str',),
        statediff_ref=dict(type='str',),
        system=dict(type='bool',),
        system_report_refs=dict(type='list', elements='str',),
        tasks_completed=dict(type='int',),
        tenant_ref=dict(type='str',),
        total_tasks=dict(type='int',),
        upgrade_events=dict(type='list', elements='dict',),
        upgrade_ops=dict(type='str',),
        upgrade_readiness=dict(type='dict',),
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
    return avi_ansible_api(module, 'upgradestatusinfo',
                           set())


if __name__ == '__main__':
    main()
