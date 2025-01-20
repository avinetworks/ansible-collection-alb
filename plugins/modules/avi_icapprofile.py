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
module: avi_icapprofile
author: Gaurav Rastogi (@grastogi23) <grastogi@avinetworks.com>
short_description: Module for setup of IcapProfile Avi RESTful Object
description:
    - This module is used to configure IcapProfile object
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
    allow_204:
        description:
            - Allow icap server to send 204 response as described in rfc 3507 section 4.5.
            - Service engine will buffer the complete request if alllow_204 is enabled.
            - If disabled, preview_size request body will be buffered if enable_preview is set to true, and rest of the request body will be streamed to the
            - icap server.
            - Field introduced in 20.1.3.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as True.
        type: bool
    buffer_size:
        description:
            - The maximum buffer size for the http request body.
            - If the request body exceeds this size, the request will not be checked by the icap server.
            - In this case, the configured action will be executed and a significant log entry will be generated.
            - Allowed values are 1-51200.
            - Field introduced in 20.1.1.
            - Unit is kb.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 51200.
        type: int
    buffer_size_exceed_action:
        description:
            - Decide what should happen if the request body size exceeds the configured buffer size.
            - If this is set to fail open, the request will not be checked by the icap server.
            - If this is set to fail closed, the request will be rejected with 413 status code.
            - Enum options - ICAP_FAIL_OPEN, ICAP_FAIL_CLOSED.
            - Field introduced in 20.1.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as ICAP_FAIL_OPEN.
        type: str
    cloud_ref:
        description:
            - The cloud where this object belongs to.
            - This must match the cloud referenced in the pool group below.
            - It is a reference to an object of type cloud.
            - Field introduced in 20.1.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    configpb_attributes:
        description:
            - Protobuf versioning for config pbs.
            - Field introduced in 21.1.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: dict
    description:
        description:
            - A description for this icap profile.
            - Field introduced in 20.1.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    enable_preview:
        description:
            - Use the icap preview feature as described in rfc 3507 section 4.5.
            - Field introduced in 20.1.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as True.
        type: bool
    fail_action:
        description:
            - Decide what should happen if there is a problem with the icap server like communication timeout, protocol error, pool error, etc.
            - If the icap server responds with 4xx-5xx error code the configured fail action is performed.
            - If this is set to fail open, the request will continue, but will create a significant log entry.
            - If this is set to fail closed, the request will be rejected with a 500 status code.
            - Enum options - ICAP_FAIL_OPEN, ICAP_FAIL_CLOSED.
            - Field introduced in 20.1.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as ICAP_FAIL_OPEN.
        type: str
    name:
        description:
            - Name of the icap profile.
            - Field introduced in 20.1.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        required: true
        type: str
    nsx_defender_config:
        description:
            - Nsxdefender specific icap configurations.
            - Field introduced in 21.1.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: dict
    pool_group_ref:
        description:
            - The pool group which is used to connect to icap servers.
            - It is a reference to an object of type poolgroup.
            - Field introduced in 20.1.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        required: true
        type: str
    preview_size:
        description:
            - The icap preview size as described in rfc 3507 section 4.5.
            - This should not exceed the size supported by the icap server.
            - If this is set to 0, only the http header will be sent to the icap server as a preview.
            - To disable preview completely, set the enable-preview option to false.if vendor is lastline, recommended preview size is 1000 bytes,minimum
            - preview size is 10 bytes.
            - Allowed values are 0-5000.
            - Field introduced in 20.1.1.
            - Unit is bytes.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 5000.
        type: int
    response_timeout:
        description:
            - Maximum time, client's request will be paused for icap processing.
            - If this timeout is exceeded, the request to the icap server will be aborted and the configured fail action is executed.
            - Allowed values are 50-3600000.
            - Field introduced in 20.1.1.
            - Unit is milliseconds.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 60000.
        type: int
    service_uri:
        description:
            - The path and query component of the icap url.
            - Host name and port will be taken from the pool.
            - Field introduced in 20.1.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        required: true
        type: str
    slow_response_warning_threshold:
        description:
            - If the icap request takes longer than this value, this request will generate a significant log entry.
            - Allowed values are 50-3600000.
            - Field introduced in 20.1.1.
            - Unit is milliseconds.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 10000.
        type: int
    tenant_ref:
        description:
            - Tenant which this object belongs to.
            - It is a reference to an object of type tenant.
            - Field introduced in 20.1.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    url:
        description:
            - Avi controller URL of the object.
        type: str
    uuid:
        description:
            - Uuid of the icap profile.
            - Field introduced in 20.1.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    vendor:
        description:
            - The vendor of the icap server.
            - Enum options - ICAP_VENDOR_GENERIC, ICAP_VENDOR_OPSWAT, ICAP_VENDOR_LASTLINE.
            - Field introduced in 20.1.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as ICAP_VENDOR_OPSWAT.
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

- name: Example to create IcapProfile object
  vmware.alb.avi_icapprofile:
    avi_credentials: "{{ avi_credentials }}"
    state: present
    name: sample_icapprofile
"""

RETURN = '''
obj:
    description: IcapProfile (api/icapprofile) object
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
        allow_204=dict(type='bool',),
        buffer_size=dict(type='int',),
        buffer_size_exceed_action=dict(type='str',),
        cloud_ref=dict(type='str',),
        configpb_attributes=dict(type='dict',),
        description=dict(type='str',),
        enable_preview=dict(type='bool',),
        fail_action=dict(type='str',),
        name=dict(type='str', required=True),
        nsx_defender_config=dict(type='dict',),
        pool_group_ref=dict(type='str', required=True),
        preview_size=dict(type='int',),
        response_timeout=dict(type='int',),
        service_uri=dict(type='str', required=True),
        slow_response_warning_threshold=dict(type='int',),
        tenant_ref=dict(type='str',),
        url=dict(type='str',),
        uuid=dict(type='str',),
        vendor=dict(type='str',),
    )
    argument_specs.update(avi_common_argument_spec())
    module = AnsibleModule(
        argument_spec=argument_specs, supports_check_mode=True)
    if not HAS_REQUESTS:
        return module.fail_json(msg=(
            'Python requests package is not installed. '
            'For installation instructions, visit https://pypi.org/project/requests.'))
    return avi_ansible_api(module, 'icapprofile',
                           set())


if __name__ == '__main__':
    main()
