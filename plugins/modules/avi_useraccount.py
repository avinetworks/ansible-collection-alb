#!/usr/bin/python
# module_check: not supported

# Copyright 2021 VMware, Inc. All rights reserved. VMware Confidential
# SPDX-License-Identifier: Apache License 2.0


from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: avi_useraccount
author: Chaitanya Deshpande (@chaitanyaavi) <chaitanya.deshpande@avinetworks.com>
short_description: Avi UserAccount Module
description:
    - This module can be used for updating the password of a user.
    - This module is useful for setting up admin password for Controller bootstrap.
options:
    full_name:
        description:
            - To set the full name for useraccount.
        type: str
    email:
        description:
            - To set email address for useraccount.
        type: str
    old_password:
        description:
            - Old password for update password or default password for bootstrap.
        required: true
        type: str
    force_change:
        description:
            - If specifically set to true then old password is tried first for controller and then the new password is
              tried. If not specified this flag then the new password is tried first.
        type: bool
        default: false
extends_documentation_fragment:
    - vmware.alb.avi
'''

EXAMPLES = '''
  - hosts: all
    vars:
      avi_credentials:
        username: "{{ username }}"
        password: "{{ password }}"
        controller: "{{ controller }}"
        api_version: "{{ api_version }}"

  - name: Update user password
    vmware.alb.avi_useraccount:
      avi_credentials: "{{ avi_credentials }}"
      full_name: "abc xyz"
      email: "abc@xyz.com"
      old_password: "{{ avi_credentials.password }}"
      force_change: false

  - name: Update user password using avi_credentials
    vmware.alb.avi_useraccount:
      avi_credentials: "{{ avi_credentials }}"
      old_password: "{{ avi_credentials.password }}"
      force_change: false
'''

RETURN = '''
obj:
    description: Avi REST resource
    returned: success, changed
    type: dict
'''

import json
import time
from ansible.module_utils.basic import AnsibleModule
from copy import deepcopy

try:
    from ansible_collections.vmware.alb.plugins.module_utils.utils.ansible_utils import (
        avi_common_argument_spec, ansible_return, avi_obj_cmp,
        cleanup_absent_fields)
    from ansible_collections.vmware.alb.plugins.module_utils.avi_api import (
        ApiSession, AviCredentials)
    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False


def main():
    argument_specs = dict(
        full_name=dict(type='str'),
        email=dict(type='str'),
        old_password=dict(type='str', required=True, no_log=True),
        # Flag to specify priority of old/new password while establishing session with controller.
        # To handle both Saas and conventional (Entire state in playbook) scenario.
        force_change=dict(type='bool', default=False)
    )
    argument_specs.update(avi_common_argument_spec())
    module = AnsibleModule(argument_spec=argument_specs)
    if not HAS_REQUESTS:
        return module.fail_json(msg=(
            'Python requests package is not installed. '
            'For installation instructions, visit https://pypi.org/project/requests.'))
    api_creds = AviCredentials()
    api_creds.update_from_ansible_module(module)
    full_name = module.params.get('full_name')
    email = module.params.get('email')
    old_password = module.params.get('old_password')
    force_change = module.params.get('force_change', False)
    data = {
        'old_password': old_password,
        'password': api_creds.password
    }
    if full_name:
        data['full_name'] = full_name
    if email:
        data['email'] = email
    api = None
    if not force_change:
        # check if the new password is already set.
        try:
            api = ApiSession.get_session(
                api_creds.controller, api_creds.username,
                password=api_creds.password, timeout=api_creds.timeout,
                tenant=api_creds.tenant, tenant_uuid=api_creds.tenant_uuid,
                token=api_creds.token, port=api_creds.port)
            data['old_password'] = api_creds.password
        except Exception:
            # create a new session using the old password.
            pass
    if not api:
        api = ApiSession.get_session(
            api_creds.controller, api_creds.username,
            password=old_password, timeout=api_creds.timeout,
            tenant=api_creds.tenant, tenant_uuid=api_creds.tenant_uuid,
            token=api_creds.token, port=api_creds.port)
    rsp = api.put('useraccount', data=data)
    return ansible_return(module, rsp, True, req=data)


if __name__ == '__main__':
    main()
