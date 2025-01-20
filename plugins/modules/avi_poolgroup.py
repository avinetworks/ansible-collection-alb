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
module: avi_poolgroup
author: Gaurav Rastogi (@grastogi23) <grastogi@avinetworks.com>
short_description: Module for setup of PoolGroup Avi RESTful Object
description:
    - This module is used to configure PoolGroup object
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
            - Checksum of cloud configuration for poolgroup.
            - Internally set by cloud connector.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    cloud_ref:
        description:
            - It is a reference to an object of type cloud.
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
            - Name of the user who created the object.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    deactivate_primary_pool_on_down:
        description:
            - Deactivate primary pool for selection when down until it is activated by user via clear poolgroup command.
            - Field introduced in 20.1.7, 21.1.2, 21.1.3.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    deployment_policy_ref:
        description:
            - When setup autoscale manager will automatically promote new pools into production when deployment goals are met.
            - It is a reference to an object of type poolgroupdeploymentpolicy.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: str
    description:
        description:
            - Description of pool group.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    fail_action:
        description:
            - Enable an action - close connection, http redirect, or local http response - when a pool group failure happens.
            - By default, a connection will be closed, in case the pool group experiences a failure.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: dict
    implicit_priority_labels:
        description:
            - Whether an implicit set of priority labels is generated.
            - Field introduced in 17.1.9,17.2.3.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    markers:
        description:
            - List of labels to be used for granular rbac.
            - Field introduced in 20.1.5.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: list
        elements: dict
    members:
        description:
            - List of pool group members object of type poolgroupmember.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: list
        elements: dict
    min_servers:
        description:
            - The minimum number of servers to distribute traffic to.
            - Allowed values are 1-65535.
            - Special values are 0 - disable.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Allowed in essentials (allowed values- 0), basic (allowed values- 0) edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 0.
        type: int
    name:
        description:
            - The name of the pool group.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        required: true
        type: str
    priority_labels_ref:
        description:
            - Uuid of the priority labels.
            - If not provided, pool group member priority label will be interpreted as a number with a larger number considered higher priority.
            - It is a reference to an object of type prioritylabels.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: str
    service_metadata:
        description:
            - Metadata pertaining to the service provided by this poolgroup.
            - In openshift/kubernetes environments, app metadata info is stored.
            - Any user input to this field will be overwritten by avi vantage.
            - Field introduced in 17.2.14,18.1.5,18.2.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
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
            - Uuid of the pool group.
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

- name: Example to create PoolGroup object
  vmware.alb.avi_poolgroup:
    avi_credentials: "{{ avi_credentials }}"
    state: present
    name: sample_poolgroup
"""

RETURN = '''
obj:
    description: PoolGroup (api/poolgroup) object
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
        cloud_ref=dict(type='str',),
        configpb_attributes=dict(type='dict',),
        created_by=dict(type='str',),
        deactivate_primary_pool_on_down=dict(type='bool',),
        deployment_policy_ref=dict(type='str',),
        description=dict(type='str',),
        fail_action=dict(type='dict',),
        implicit_priority_labels=dict(type='bool',),
        markers=dict(type='list', elements='dict',),
        members=dict(type='list', elements='dict',),
        min_servers=dict(type='int',),
        name=dict(type='str', required=True),
        priority_labels_ref=dict(type='str',),
        service_metadata=dict(type='str',),
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
    return avi_ansible_api(module, 'poolgroup',
                           set())


if __name__ == '__main__':
    main()
