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
module: avi_serverautoscalepolicy
author: Gaurav Rastogi (@grastogi23) <grastogi@avinetworks.com>
short_description: Module for setup of ServerAutoScalePolicy Avi RESTful Object
description:
    - This module is used to configure ServerAutoScalePolicy object
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
            - Field introduced in 21.1.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: dict
    delay_for_server_garbage_collection:
        description:
            - Delay in minutes after which a down server will be removed from pool.
            - Value 0 disables this functionality.
            - Field introduced in 20.1.3.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 0.
        type: int
    description:
        description:
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    intelligent_autoscale:
        description:
            - Use avi intelligent autoscale algorithm where autoscale is performed by comparing load on the pool against estimated capacity of all the servers.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    intelligent_scalein_margin:
        description:
            - Maximum extra capacity as percentage of load used by the intelligent scheme.
            - Scale-in is triggered when available capacity is more than this margin.
            - Allowed values are 1-99.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 40.
        type: int
    intelligent_scaleout_margin:
        description:
            - Minimum extra capacity as percentage of load used by the intelligent scheme.
            - Scale-out is triggered when available capacity is less than this margin.
            - Allowed values are 1-99.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 20.
        type: int
    markers:
        description:
            - List of labels to be used for granular rbac.
            - Field introduced in 20.1.5.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: list
        elements: dict
    max_scalein_adjustment_step:
        description:
            - Maximum number of servers to scale-in simultaneously.
            - The actual number of servers to scale-in is chosen such that target number of servers is always more than or equal to the min_size.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 1.
        type: int
    max_scaleout_adjustment_step:
        description:
            - Maximum number of servers to scale-out simultaneously.
            - The actual number of servers to scale-out is chosen such that target number of servers is always less than or equal to the max_size.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 1.
        type: int
    max_size:
        description:
            - Maximum number of servers after scale-out.
            - Allowed values are 0-400.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: int
    min_size:
        description:
            - No scale-in happens once number of operationally up servers reach min_servers.
            - Allowed values are 0-400.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: int
    name:
        description:
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        required: true
        type: str
    scalein_alertconfig_refs:
        description:
            - Trigger scale-in when alerts due to any of these alert configurations are raised.
            - It is a reference to an object of type alertconfig.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: list
        elements: str
    scalein_cooldown:
        description:
            - Cooldown period during which no new scale-in is triggered to allow previous scale-in to successfully complete.
            - Unit is sec.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 300.
        type: int
    scaleout_alertconfig_refs:
        description:
            - Trigger scale-out when alerts due to any of these alert configurations are raised.
            - It is a reference to an object of type alertconfig.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: list
        elements: str
    scaleout_cooldown:
        description:
            - Cooldown period during which no new scale-out is triggered to allow previous scale-out to successfully complete.
            - Unit is sec.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 300.
        type: int
    scheduled_scalings:
        description:
            - Scheduled-based scale-in/out policy.
            - During scheduled intervals, metrics based autoscale is not enabled and number of servers will be solely derived from schedulescale policy.
            - Field introduced in 21.1.1.
            - Maximum of 1 items allowed.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
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
    use_predicted_load:
        description:
            - Use predicted load rather than current load.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
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

- name: Example to create ServerAutoScalePolicy object
  vmware.alb.avi_serverautoscalepolicy:
    avi_credentials: "{{ avi_credentials }}"
    state: present
    name: sample_serverautoscalepolicy
"""

RETURN = '''
obj:
    description: ServerAutoScalePolicy (api/serverautoscalepolicy) object
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
        delay_for_server_garbage_collection=dict(type='int',),
        description=dict(type='str',),
        intelligent_autoscale=dict(type='bool',),
        intelligent_scalein_margin=dict(type='int',),
        intelligent_scaleout_margin=dict(type='int',),
        markers=dict(type='list', elements='dict',),
        max_scalein_adjustment_step=dict(type='int',),
        max_scaleout_adjustment_step=dict(type='int',),
        max_size=dict(type='int',),
        min_size=dict(type='int',),
        name=dict(type='str', required=True),
        scalein_alertconfig_refs=dict(type='list', elements='str',),
        scalein_cooldown=dict(type='int',),
        scaleout_alertconfig_refs=dict(type='list', elements='str',),
        scaleout_cooldown=dict(type='int',),
        scheduled_scalings=dict(type='list', elements='dict',),
        tenant_ref=dict(type='str',),
        url=dict(type='str',),
        use_predicted_load=dict(type='bool',),
        uuid=dict(type='str',),
    )
    argument_specs.update(avi_common_argument_spec())
    module = AnsibleModule(
        argument_spec=argument_specs, supports_check_mode=True)
    if not HAS_REQUESTS:
        return module.fail_json(msg=(
            'Python requests package is not installed. '
            'For installation instructions, visit https://pypi.org/project/requests.'))
    return avi_ansible_api(module, 'serverautoscalepolicy',
                           set())


if __name__ == '__main__':
    main()
