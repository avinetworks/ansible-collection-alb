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
module: avi_poolgroupdeploymentpolicy
author: Gaurav Rastogi (@grastogi23) <grastogi@avinetworks.com>
short_description: Module for setup of PoolGroupDeploymentPolicy Avi RESTful Object
description:
    - This module is used to configure PoolGroupDeploymentPolicy object
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
    auto_disable_old_prod_pools:
        description:
            - It will automatically disable old production pools once there is a new production candidate.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as True.
        type: bool
    configpb_attributes:
        description:
            - Protobuf versioning for config pbs.
            - Field introduced in 21.1.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: dict
    description:
        description:
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    evaluation_duration:
        description:
            - Duration of evaluation period for automatic deployment.
            - Allowed values are 60-86400.
            - Unit is sec.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 300.
        type: int
    markers:
        description:
            - List of labels to be used for granular rbac.
            - Field introduced in 20.1.5.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: list
        elements: dict
    name:
        description:
            - The name of the pool group deployment policy.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        required: true
        type: str
    rules:
        description:
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: list
        elements: dict
    scheme:
        description:
            - Deployment scheme.
            - Enum options - BLUE_GREEN, CANARY.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as BLUE_GREEN.
        type: str
    target_test_traffic_ratio:
        description:
            - Target traffic ratio before pool is made production.
            - Allowed values are 1-100.
            - Unit is ratio.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 100.
        type: int
    tenant_ref:
        description:
            - It is a reference to an object of type tenant.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    test_traffic_ratio_rampup:
        description:
            - Ratio of the traffic that is sent to the pool under test.
            - Test ratio of 100 means blue green.
            - Allowed values are 1-100.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 100.
        type: int
    url:
        description:
            - Avi controller URL of the object.
        type: str
    uuid:
        description:
            - Uuid of the pool group deployment policy.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    webhook_ref:
        description:
            - Webhook configured with url that avi controller will pass back information about pool group, old and new pool information and current deployment
            - rule results.
            - It is a reference to an object of type webhook.
            - Field introduced in 17.1.1.
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

- name: Example to create PoolGroupDeploymentPolicy object
  vmware.alb.avi_poolgroupdeploymentpolicy:
    avi_credentials: "{{ avi_credentials }}"
    state: present
    name: sample_poolgroupdeploymentpolicy
"""

RETURN = '''
obj:
    description: PoolGroupDeploymentPolicy (api/poolgroupdeploymentpolicy) object
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
        auto_disable_old_prod_pools=dict(type='bool',),
        configpb_attributes=dict(type='dict',),
        description=dict(type='str',),
        evaluation_duration=dict(type='int',),
        markers=dict(type='list', elements='dict',),
        name=dict(type='str', required=True),
        rules=dict(type='list', elements='dict',),
        scheme=dict(type='str',),
        target_test_traffic_ratio=dict(type='int',),
        tenant_ref=dict(type='str',),
        test_traffic_ratio_rampup=dict(type='int',),
        url=dict(type='str',),
        uuid=dict(type='str',),
        webhook_ref=dict(type='str',),
    )
    argument_specs.update(avi_common_argument_spec())
    module = AnsibleModule(
        argument_spec=argument_specs, supports_check_mode=True)
    if not HAS_REQUESTS:
        return module.fail_json(msg=(
            'Python requests package is not installed. '
            'For installation instructions, visit https://pypi.org/project/requests.'))
    return avi_ansible_api(module, 'poolgroupdeploymentpolicy',
                           set())


if __name__ == '__main__':
    main()
