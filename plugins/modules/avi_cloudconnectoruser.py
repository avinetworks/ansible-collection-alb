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
module: avi_cloudconnectoruser
author: Gaurav Rastogi (@grastogi23) <grastogi@avinetworks.com>
short_description: Module for setup of CloudConnectorUser Avi RESTful Object
description:
    - This module is used to configure CloudConnectorUser object
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
    azure_serviceprincipal:
        description:
            - Field introduced in 17.2.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: dict
    azure_userpass:
        description:
            - Field introduced in 17.2.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: dict
    configpb_attributes:
        description:
            - Protobuf versioning for config pbs.
            - Field introduced in 21.1.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: dict
    gcp_credentials:
        description:
            - Credentials for google cloud platform.
            - Field introduced in 18.2.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: dict
    name:
        description:
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        required: true
        type: str
    nsxt_credentials:
        description:
            - Credentials to talk to nsx-t manager.
            - Field introduced in 20.1.1.
            - Allowed with any value in enterprise, basic, enterprise with cloud services edition.
        type: dict
    obj_password:
        description:
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    oci_credentials:
        description:
            - Credentials for oracle cloud infrastructure.
            - Field deprecated in 31.1.1.
            - Field introduced in 18.2.1,18.1.3.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: dict
    private_key:
        description:
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    public_key:
        description:
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    tenant_ref:
        description:
            - It is a reference to an object of type tenant.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    tencent_credentials:
        description:
            - Credentials for tencent cloud.
            - Field introduced in 18.2.3.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: dict
    url:
        description:
            - Avi controller URL of the object.
        type: str
    uuid:
        description:
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    vcenter_credentials:
        description:
            - Credentials to talk to vcenter.
            - Field introduced in 20.1.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: dict
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

- name: Create a Cloud connector user that is used for integration into cloud platforms
  vmware.alb.avi_cloudconnectoruser:
    avi_credentials: "{{ avi_credentials }}"
    name: root
    private_key: |
      -----BEGIN RSA PRIVATE KEY-----
      -----END RSA PRIVATE KEY-----'
    public_key: 'ssh-rsa ...'
    tenant_ref: /api/tenant?name=admin
"""

RETURN = '''
obj:
    description: CloudConnectorUser (api/cloudconnectoruser) object
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
        azure_serviceprincipal=dict(type='dict',),
        azure_userpass=dict(type='dict',),
        configpb_attributes=dict(type='dict',),
        gcp_credentials=dict(type='dict',),
        name=dict(type='str', required=True),
        nsxt_credentials=dict(type='dict',),
        obj_password=dict(type='str',),
        oci_credentials=dict(type='dict',),
        private_key=dict(type='str', no_log=True,),
        public_key=dict(type='str',),
        tenant_ref=dict(type='str',),
        tencent_credentials=dict(type='dict',),
        url=dict(type='str',),
        uuid=dict(type='str',),
        vcenter_credentials=dict(type='dict',),
    )
    argument_specs.update(avi_common_argument_spec())
    module = AnsibleModule(
        argument_spec=argument_specs, supports_check_mode=True)
    if not HAS_REQUESTS:
        return module.fail_json(msg=(
            'Python requests package is not installed. '
            'For installation instructions, visit https://pypi.org/project/requests.'))
    return avi_ansible_api(module, 'cloudconnectoruser',
                           ['password', 'private_key'])


if __name__ == '__main__':
    main()
