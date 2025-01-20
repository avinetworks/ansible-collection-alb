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
module: avi_ssopolicy
author: Chaitanya Deshpande (@chaitanyaavi) <chaitanya.deshpande@avinetworks.com>
short_description: Module for setup of SSOPolicy Avi RESTful Object
description:
    - This module is used to configure SSOPolicy object
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
    authentication_policy:
        description:
            - Authentication policy settings.
            - Field introduced in 18.2.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: dict
    authorization_policy:
        description:
            - Authorization policy settings.
            - Field introduced in 18.2.5.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: dict
    configpb_attributes:
        description:
            - Protobuf versioning for config pbs.
            - Field introduced in 21.1.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: dict
    markers:
        description:
            - List of labels to be used for granular rbac.
            - Field introduced in 20.1.5.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: list
        elements: dict
    name:
        description:
            - Name of the sso policy.
            - Field introduced in 18.2.3.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        required: true
        type: str
    tenant_ref:
        description:
            - Uuid of the tenant.
            - It is a reference to an object of type tenant.
            - Field introduced in 18.2.3.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    type:
        description:
            - Sso policy type.
            - Enum options - SSO_TYPE_SAML, SSO_TYPE_PINGACCESS, SSO_TYPE_JWT, SSO_TYPE_LDAP, SSO_TYPE_OAUTH.
            - Field introduced in 18.2.5.
            - Allowed with any value in enterprise, essentials, enterprise with cloud services edition.
            - Allowed in basic (allowed values- sso_type_saml, sso_type_jwt, sso_type_ldap, sso_type_oauth) edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as SSO_TYPE_SAML.
        type: str
    url:
        description:
            - Avi controller URL of the object.
        type: str
    uuid:
        description:
            - Uuid of the sso policy.
            - Field introduced in 18.2.3.
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

- name: Example to create SSOPolicy object
  vmware.alb.avi_ssopolicy:
    avi_credentials: "{{ avi_credentials }}"
    state: present
    name: sample_ssopolicy
"""

RETURN = '''
obj:
    description: SSOPolicy (api/ssopolicy) object
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
        authentication_policy=dict(type='dict',),
        authorization_policy=dict(type='dict',),
        configpb_attributes=dict(type='dict',),
        markers=dict(type='list', elements='dict',),
        name=dict(type='str', required=True),
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
    return avi_ansible_api(module, 'ssopolicy',
                           set())


if __name__ == '__main__':
    main()
