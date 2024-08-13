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
module: avi_api_image
author: Sandeep Bandi (@sabandi) <sabandi@vmware.com>
short_description: Avi API Module for image
description:
    - This module can be used for calling image resources to upload upgrade/patch files
options:
    file_path:
        description:
            - Local file path of file to be uploaded or downloaded file
        required: true
        type: str
    params:
        description:
            - Query parameters passed to the HTTP API.
        type: dict
    timeout:
        description:
            - Timeout (in seconds) for Avi API calls.
        default: 300
        type: int
extends_documentation_fragment:
    - vmware.alb.avi
'''

EXAMPLES = '''
  - name: Upload se patch image to controller
    vmware.alb.avi_api_image:
      avi_credentials:
        username: "{{ username }}"
        password: "{{ password }}"
        controller: "{{ controller }}"
        api_version: "{{ api_version }}"
      file_path: ./se_patch.pkg
      api_version: 20.1.1
'''


RETURN = '''
obj:
    description: Avi REST resource
    returned: success, changed
    type: dict
'''

import json
import os
from ansible.module_utils.basic import AnsibleModule

try:
    from requests_toolbelt import MultipartEncoder
    HAS_LIB = True
except ImportError:
    HAS_LIB = False

try:
    from ansible_collections.vmware.alb.plugins.module_utils.utils.ansible_utils import (
        avi_common_argument_spec, ansible_return, avi_obj_cmp,
        cleanup_absent_fields)
    from ansible_collections.vmware.alb.plugins.module_utils.avi_api import (
        ApiSession, AviCredentials)
    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False
try:
    from avi.sdk.avi_api import ApiSession, AviCredentials
    from avi.sdk.utils.ansible_utils import (
        avi_obj_cmp, cleanup_absent_fields, avi_common_argument_spec,
        ansible_return)
    HAS_AVI = True
except ImportError:
    HAS_AVI = False


def main():
    argument_specs = dict(
        file_path=dict(type='str', required=True),
        params=dict(type='dict'),
        timeout=dict(type='int', default=300)
    )
    argument_specs.update(avi_common_argument_spec())
    module = AnsibleModule(argument_spec=argument_specs)
    if not HAS_REQUESTS:
        return module.fail_json(msg=(
            'Python requests package is not installed. '
            'For installation instructions, visit https://pypi.org/project/requests.'))
    if not HAS_LIB:
        return module.fail_json(
            msg='avi_api_image, requests_toolbelt is required for this module')

    api_creds = AviCredentials()
    api_creds.update_from_ansible_module(module)
    api = ApiSession.get_session(
        api_creds.controller, api_creds.username, password=api_creds.password,
        timeout=api_creds.timeout, tenant=api_creds.tenant,
        tenant_uuid=api_creds.tenant_uuid, token=api_creds.token,
        port=api_creds.port)

    tenant_uuid = api_creds.tenant_uuid
    tenant = api_creds.tenant
    timeout = int(module.params.get('timeout'))
    params = module.params.get('params', None)
    # Get the api_version from module.
    api_version = api_creds.api_version
    file_path = module.params['file_path']
    if not os.path.exists(file_path):
        return module.fail_json(msg=('File not found : %s' % file_path))
    file_name = os.path.basename(file_path)
    with open(file_path, "rb") as f:
        f_data = {"file": (file_name, f, "application/octet-stream")}
        m = MultipartEncoder(fields=f_data)
        headers = {'Content-Type': m.content_type}
        rsp = api.post("image", data=m, headers=headers, verify=False)
        if rsp.status_code > 300:
            return module.fail_json(msg='Fail to upload file: %s' %
                                    rsp.text)
        else:
            return module.exit_json(
                changed=True, msg="File uploaded successfully")


if __name__ == '__main__':
    main()
