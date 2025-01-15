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
module: avi_image
author: Gaurav Rastogi (@grastogi23) <grastogi@avinetworks.com>
short_description: Module for setup of Image Avi RESTful Object
description:
    - This module is used to configure Image object
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
    cloud_info_values:
        description:
            - This field describes the cloud info specific to the base image.
            - Field introduced in 20.1.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: list
        elements: dict
    controller_info:
        description:
            - Controller package details.
            - Field introduced in 18.2.6.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: dict
    controller_patch_name:
        description:
            - Mandatory controller patch name that is applied along with this base image.
            - Field introduced in 18.2.10, 20.1.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    controller_patch_ref:
        description:
            - It references the controller-patch associated with the uber image.
            - It is a reference to an object of type image.
            - Field introduced in 18.2.8, 20.1.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    duration:
        description:
            - Time taken to upload the image in seconds.
            - Field introduced in 21.1.3.
            - Unit is sec.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: int
    end_time:
        description:
            - Image upload end time.
            - Field introduced in 21.1.3.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: str
    events:
        description:
            - Image events for image upload operation.
            - Field introduced in 21.1.3.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: list
        elements: dict
    fips_mode_transition_applicable:
        description:
            - Specifies whether fips mode can be enabled on this image.
            - Field introduced in 30.1.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as True.
        type: bool
    img_state:
        description:
            - Status of the image.
            - Field introduced in 21.1.3.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: dict
    migrations:
        description:
            - This field describes the api migration related information.
            - Field introduced in 18.2.6.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: dict
    name:
        description:
            - Name of the image.
            - Field introduced in 18.2.6.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        required: true
        type: str
    progress:
        description:
            - Image upload progress which holds value between 0-100.
            - Allowed values are 0-100.
            - Field introduced in 21.1.3.
            - Unit is percent.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 0.
        type: int
    se_info:
        description:
            - Se package details.
            - Field introduced in 18.2.6.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: dict
    se_patch_name:
        description:
            - Mandatory serviceengine patch name that is applied along with this base image.
            - Field introduced in 18.2.10, 20.1.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    se_patch_ref:
        description:
            - It references the service engine patch associated with the uber image.
            - It is a reference to an object of type image.
            - Field introduced in 18.2.8, 20.1.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    start_time:
        description:
            - Image upload start time.
            - Field introduced in 21.1.3.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: str
    tasks_completed:
        description:
            - Completed set of tasks for image upload.
            - Field introduced in 21.1.3.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 0.
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
            - Total number of tasks for image upload.
            - Field introduced in 21.1.3.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 0.
        type: int
    type:
        description:
            - Type of the image patch/system.
            - Enum options - IMAGE_TYPE_PATCH, IMAGE_TYPE_SYSTEM, IMAGE_TYPE_MUST_CHECK.
            - Field introduced in 18.2.6.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    uber_bundle:
        description:
            - Status to check if the image is an uber bundle.
            - Field introduced in 18.2.8, 20.1.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    url:
        description:
            - Avi controller URL of the object.
        type: str
    uuid:
        description:
            - Uuid of the image.
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

- name: Example to create Image object
  vmware.alb.avi_image:
    avi_credentials: "{{ avi_credentials }}"
    state: present
    name: sample_image
"""

RETURN = '''
obj:
    description: Image (api/image) object
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
        cloud_info_values=dict(type='list', elements='dict',),
        controller_info=dict(type='dict',),
        controller_patch_name=dict(type='str',),
        controller_patch_ref=dict(type='str',),
        duration=dict(type='int',),
        end_time=dict(type='str',),
        events=dict(type='list', elements='dict',),
        fips_mode_transition_applicable=dict(type='bool',),
        img_state=dict(type='dict',),
        migrations=dict(type='dict',),
        name=dict(type='str', required=True),
        progress=dict(type='int',),
        se_info=dict(type='dict',),
        se_patch_name=dict(type='str',),
        se_patch_ref=dict(type='str',),
        start_time=dict(type='str',),
        tasks_completed=dict(type='int',),
        tenant_ref=dict(type='str',),
        total_tasks=dict(type='int',),
        type=dict(type='str',),
        uber_bundle=dict(type='bool',),
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
    return avi_ansible_api(module, 'image',
                           set())


if __name__ == '__main__':
    main()
