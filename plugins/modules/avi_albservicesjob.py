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
module: avi_albservicesjob
author: Gaurav Rastogi (@grastogi23) <grastogi@avinetworks.com>
short_description: Module for setup of ALBServicesJob Avi RESTful Object
description:
    - This module is used to configure ALBServicesJob object
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
    command:
        description:
            - The command to be triggered by the albservicesjob.
            - Field introduced in 21.1.3.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        required: true
        type: str
    configpb_attributes:
        description:
            - Protobuf versioning for config pbs.
            - Field introduced in 21.1.3.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: dict
    end_time:
        description:
            - Time at which the albservicesjob ended.
            - Field introduced in 21.1.3.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: dict
    name:
        description:
            - The name of the albservicesjob.
            - Field introduced in 21.1.3.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        required: true
        type: str
    params:
        description:
            - Job params.
            - Field introduced in 22.1.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: list
        elements: dict
    pulse_job_id:
        description:
            - A unique identifier for this job entry on the pulse cloud services.
            - Field introduced in 21.1.3.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: str
    pulse_sync_status:
        description:
            - Status of sync to pulse cloud services(result uploads/state updates).
            - Field introduced in 22.1.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: bool
    result:
        description:
            - Job result.
            - Field introduced in 22.1.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: str
    start_time:
        description:
            - Time at which the albservicesjob started.
            - Field introduced in 21.1.3.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: dict
    status:
        description:
            - The status of the albservicesjob.
            - Enum options - UNDETERMINED, PENDING, IN_PROGRESS, COMPLETED, FAILED, NOT_ENABLED.
            - Field introduced in 21.1.3.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as PENDING.
        type: str
    status_update_time:
        description:
            - Time at which the status of albservicesjob updated.
            - Field introduced in 22.1.6.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: dict
    tenant_ref:
        description:
            - The unique identifier of the tenant to which this albservicesjob belongs.
            - It is a reference to an object of type tenant.
            - Field introduced in 21.1.3.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: str
    token:
        description:
            - Job token.
            - Field introduced in 22.1.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: str
    url:
        description:
            - Avi controller URL of the object.
        type: str
    uuid:
        description:
            - A unique identifier for this albservicesjob entry.
            - Field introduced in 21.1.3.
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

- name: Example to create ALBServicesJob object
  vmware.alb.avi_albservicesjob:
    avi_credentials: "{{ avi_credentials }}"
    state: present
    name: sample_albservicesjob
"""

RETURN = '''
obj:
    description: ALBServicesJob (api/albservicesjob) object
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
        command=dict(type='str', required=True),
        configpb_attributes=dict(type='dict',),
        end_time=dict(type='dict',),
        name=dict(type='str', required=True),
        params=dict(type='list', elements='dict',),
        pulse_job_id=dict(type='str',),
        pulse_sync_status=dict(type='bool',),
        result=dict(type='str',),
        start_time=dict(type='dict',),
        status=dict(type='str',),
        status_update_time=dict(type='dict',),
        tenant_ref=dict(type='str',),
        token=dict(type='str',),
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
    return avi_ansible_api(module, 'albservicesjob',
                           set())


if __name__ == '__main__':
    main()
