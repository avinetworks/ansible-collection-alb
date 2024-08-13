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
module: avi_api_fileservice
author: Chaitanya Deshpande (@chaitanyaavi) <chaitanya.deshpande@avinetworks.com>

short_description: Avi API Module for fileservice
description:
    - This module can be used for calling fileservice resources to upload/download files
options:
    upload:
        description:
            - Allowed upload flag false for download and true for upload.
        required: true
        type: bool
    force_mode:
        description:
            - Allowed force mode for upload forcefully.
        default: true
        type: bool
    file_path:
        description:
            - Local file path of file to be uploaded or downloaded file
        required: true
        type: str
    params:
        description:
            - Query parameters passed to the HTTP API.
        type: dict
    path:
        description:
            - 'Path for Avi API resource. For example, C(path: seova) will translate to C(api/fileservice/seova).'
        required: true
        type: str
    timeout:
        description:
            - Timeout (in seconds) for Avi API calls.
        default: 60
        type: int
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

  - name: Download se image from controller
    vmware.alb.avi_api_fileservice:
      avi_credentials: "{{ avi_credentials }}"
      upload: false
      path: seova
      file_path: ./se.ova
      api_version: 17.2.8

  - name: Upload HSM package to controller
    vmware.alb.avi_api_fileservice:
      avi_credentials: "{{ avi_credentials }}"
      upload: true
      path: hsmpackages?hsmtype=safenet
      file_path: ./safenet.tar
      api_version: 17.2.8

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


def main():
    argument_specs = dict(
        force_mode=dict(type='bool', default=True),
        upload=dict(required=True,
                    type='bool'),
        path=dict(type='str', required=True),
        file_path=dict(type='str', required=True),
        params=dict(type='dict'),
        timeout=dict(type='int', default=60)
    )
    argument_specs.update(avi_common_argument_spec())
    module = AnsibleModule(argument_spec=argument_specs)
    if not HAS_REQUESTS:
        return module.fail_json(msg=(
            'Python API requests is not installed.'))
    if not HAS_LIB:
        return module.fail_json(
            msg='avi_api_fileservice, requests_toolbelt is required for this module')

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
    # path is a required argument
    path = 'fileservice/%s' % module.params.get('path', '')
    params = module.params.get('params', None)
    data = module.params.get('data', None)
    # Get the api_version from module.
    api_version = api_creds.api_version
    if data is not None:
        data = json.loads(data)
    upload = module.params['upload']
    file_path = module.params['file_path']
    force_mode = module.params['force_mode']

    if upload:
        if not os.path.exists(file_path):
            return module.fail_json(msg=('File not found : %s' % file_path))
        file_name = os.path.basename(file_path)
        # Handle special case of upgrade controller using .pkg file which will be uploaded to upgrade_pkgs directory
        if file_name.lower().endswith('.pkg'):
            uri = 'controller://upgrade_pkgs'
            path = 'fileservice/uploads'
        else:
            uri = 'controller://%s' % module.params.get('path', '').split('?')[0]
        changed = False
        file_uri = 'fileservice?uri=%s' % uri
        rsp = api.post(file_uri, tenant=tenant, tenant_uuid=tenant_uuid,
                       timeout=timeout)
        with open(file_path, "rb") as f:
            f_data = {"file": (file_name, f, "application/octet-stream"),
                      "uri": uri}
            m = MultipartEncoder(fields=f_data)
            headers = {'Content-Type': m.content_type}
            rsp = api.post(path, data=m, headers=headers,
                           verify=False)
            if rsp.status_code > 300:
                return module.fail_json(msg='Fail to upload file: %s' %
                                        rsp.text)
            else:
                return module.exit_json(
                    changed=True, msg="File uploaded successfully")

    elif not upload:
        # Removing existing file.
        if force_mode and os.path.exists(file_path):
            os.remove(file_path)
        rsp = api.get(path, params=params, stream=True)
        if rsp.status_code > 300:
            return module.fail_json(msg='Fail to download file: %s' % rsp.text)
        with open(file_path, 'wb') as f:
            for chunk in rsp.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
        return module.exit_json(msg='File downloaded successfully',
                                changed=True)


if __name__ == '__main__':
    main()
