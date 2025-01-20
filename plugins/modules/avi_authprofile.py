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
module: avi_authprofile
author: Gaurav Rastogi (@grastogi23) <grastogi@avinetworks.com>
short_description: Module for setup of AuthProfile Avi RESTful Object
description:
    - This module is used to configure AuthProfile object
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
    description:
        description:
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    http:
        description:
            - Http user authentication params.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: dict
    jwt_profile_ref:
        description:
            - Jwtserverprofile to be used for authentication.
            - It is a reference to an object of type jwtserverprofile.
            - Field introduced in 20.1.3.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: str
    ldap:
        description:
            - Ldap server and directory settings.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: dict
    markers:
        description:
            - List of labels to be used for granular rbac.
            - Field introduced in 20.1.6.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: list
        elements: dict
    name:
        description:
            - Name of the auth profile.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        required: true
        type: str
    oauth_profile:
        description:
            - Oauth profile - common endpoint information.
            - Field introduced in 21.1.3.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: dict
    saml:
        description:
            - Saml settings.
            - Field introduced in 17.2.3.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: dict
    tacacs_plus:
        description:
            - Tacacs+ settings.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: dict
    tenant_ref:
        description:
            - It is a reference to an object of type tenant.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    type:
        description:
            - Type of the auth profile.
            - Enum options - AUTH_PROFILE_LDAP, AUTH_PROFILE_TACACS_PLUS, AUTH_PROFILE_SAML, AUTH_PROFILE_PINGACCESS, AUTH_PROFILE_JWT, AUTH_PROFILE_OAUTH.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Allowed in essentials (allowed values- auth_profile_ldap,auth_profile_tacacs_plus,auth_profile_saml,auth_profile_jwt,auth_profile_oauth), basic
            - (allowed values- auth_profile_ldap,auth_profile_tacacs_plus,auth_profile_saml,auth_profile_jwt,auth_profile_oauth) edition.
        required: true
        type: str
    url:
        description:
            - Avi controller URL of the object.
        type: str
    uuid:
        description:
            - Uuid of the auth profile.
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

- name: Create user authorization profile based on the LDAP
  vmware.alb.avi_authprofile:
    avi_credentials: "{{ avi_credentials }}"

    ldap:
      base_dn: dc=avi,dc=local
      bind_as_administrator: true
      port: 389
      security_mode: AUTH_LDAP_SECURE_NONE
      server:
      - 192.168.12.18
      settings:
        admin_bind_dn: user@avi.local
        group_filter: (objectClass=*)
        group_member_attribute: member
        group_member_is_full_dn: true
        group_search_dn: dc=avi,dc=local
        group_search_scope: AUTH_LDAP_SCOPE_SUBTREE
        ignore_referrals: true
        password: password
        user_id_attribute: samAccountname
        user_search_dn: dc=avi,dc=local
        user_search_scope: AUTH_LDAP_SCOPE_ONE
    name: ProdAuth
    tenant_ref: /api/tenant?name=admin
    type: AUTH_PROFILE_LDAP
"""

RETURN = '''
obj:
    description: AuthProfile (api/authprofile) object
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
        description=dict(type='str',),
        http=dict(type='dict',),
        jwt_profile_ref=dict(type='str',),
        ldap=dict(type='dict',),
        markers=dict(type='list', elements='dict',),
        name=dict(type='str', required=True),
        oauth_profile=dict(type='dict',),
        saml=dict(type='dict',),
        tacacs_plus=dict(type='dict',),
        tenant_ref=dict(type='str',),
        type=dict(type='str', required=True),
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
    return avi_ansible_api(module, 'authprofile',
                           set())


if __name__ == '__main__':
    main()
