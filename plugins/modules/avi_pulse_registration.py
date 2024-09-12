#!/usr/bin/python
# module_check: supported

# Avi Version: 17.1.1
# Copyright 2021 VMware, Inc. All rights reserved. VMware Confidential
# SPDX-License-Identifier: Apache License 2.0

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: avi_pulse_registration
author: Patnala Chandana (@chandanapatnala) <cpatnala@vmware.com>

short_description: Avi API Module for pulse registration
description:
    - This module can be used for registering with optins or deregistering the controller with pulse.
options:
    state:
        description:
            - The state that should be applied on the entity.
        default: present
        choices: ["absent", "present"]
        type: str
    jwt_token:
        description:
            - Token which is used to login to pulse from controller for the specific user.
            - For generation of the jwt_token paste the related link in Incognito window to prevent IdP from considering any existing valid login session
            - If controller is running >= 21.1.3 and is in ENTERPRISE tier then visit URL :https://portal.avipulse.vmware.com/portal/controller/auth/ctrllogin
            - If controller is running >= 21.1.3 and is in SAAS tier then visit URL :https://portal.avipulse.vmware.com/portal/controller/auth/ccctrllogin
            - jwt_token is valid for 365 days.
        required: true
        type: str
    name:
        description:
            - name to be specified for registration.
        required: true
        type: str
    params:
        description:
            - Query parameters passed to the HTTP API.
        type: dict
    description:
        description:
            - description to be specified for registration.
        required: true
        type: str
    email:
        description:
            - email to be specified for registration.
        required: true
        type: str
    account_id:
        description:
            - account id to be specified for registration.
        required: true
        type: str
    optins:
        description:
            - The opt-in that should be applied on the entity.
        default: present
        choices: ["absent", "present"]
        type: str
    enable_cleanup_of_attached_files:
        description:
            - Enable to clean up the attached files.
        type: bool
        default: False
    enable_appsignature_sync:
        description:
            - Enable to receive application specific signature updates.
        type: bool
        default: False
    enable_ip_reputation:
        description:
            - Enable to receive IP reputation updates.
        type: bool
        default: False
    enable_pulse_case_management:
        description:
            - Enable for pulse case management.
        type: bool
        default: False
    enable_pulse_waf_management:
        description:
            - Enable to receive WAF CRS updates.
        type: bool
        default: False
    enable_user_agent_db_sync:
        description:
            - Enable to receive bot management updates.
        type: bool
        default: False
    use_tls:
        description:
            - Enable to allow secure end to end communication between controller and NSX alb services.
        type: bool
        default: False
    waf_config:
        description:
            - Dictionary which is used to set the default values to be used for WAF management.
        suboptions:
            enable_waf_signatures_notifications:
                description:
                    - Enable event notifications when new WAF signatures/CRS versions are available.
                type: bool
                default: False
            enable_auto_download_waf_signatures:
                description:
                    - Enable to automatically download new WAF signatures/CRS version to the controller.
                type: bool
                default: False
        type: dict
    case_config:
        description:
            - Dictionary which is used to set the default values to be used for pulse case management.
        suboptions:
            enable_auto_case_creation_on_controller_failure:
                description:
                    - Enable pro-active support case creation when a controller failure occurs.
                type: bool
                default: False
            enable_auto_case_creation_on_se_failure:
                description:
                    - Enable pro-active support case creation when a service engine failure occurs.
                type: bool
                default: False
        type: dict
extends_documentation_fragment:
    - vmware.alb.avi
'''

EXAMPLES = """
- hosts: localhost
  collections:
    - vmware.alb
  vars:
    avi_credentials:
      username: "{{ username }}"
      password: "{{ password }}"
      controller: "{{ controller }}"
      api_version: "{{ api_version }}"
  tasks:
    - name: Pulse registration or deregistration
      vmware.alb.avi_pulse_registration:
        avi_credentials: "{{ avi_credentials }}"
        state: present
        jwt_token: "{{ jwt_token }}"
        name: 'AviPulse'
        description: 'Registration and deregistration'
        email: 'user@gmail.com'
        account_id: '123456789'
        optins: present
        enable_pulse_case_management: True
        case_config:
          enable_auto_case_creation_on_controller_failure: False
          enable_auto_case_creation_on_se_failure: True
        enable_pulse_waf_management: True
        waf_config:
          enable_waf_signatures_notifications: True
          enable_auto_download_waf_signatures: True
        enable_user_agent_db_sync: False
        enable_ip_reputation: True
        enable_appsignature_sync: True
    - name: Sleep for 7 seconds and continue with play
      wait_for:
        timeout: 7
      delegate_to: localhost
"""
RETURN = '''
obj:
    description: Avi REST resource
    returned: success, changed
    type: dict
'''


import time
from ansible.module_utils.basic import AnsibleModule
try:
    from ansible_collections.vmware.alb.plugins.module_utils.utils.ansible_utils import (
        avi_common_argument_spec, AviCheckModeResponse, ansible_return, avi_obj_cmp,
        cleanup_absent_fields)
    from ansible_collections.vmware.alb.plugins.module_utils.avi_api import (
        ApiSession, AviCredentials)
    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False


def main():
    case_spec = dict(
        enable_auto_case_creation_on_controller_failure=dict(type='bool', default=False),
        enable_auto_case_creation_on_se_failure=dict(type='bool', default=False)
    )
    waf_spec = dict(
        enable_auto_download_waf_signatures=dict(type='bool', default=False),
        enable_waf_signatures_notifications=dict(type='bool', default=False)

    )
    argument_specs = dict(
        state=dict(default='present', choices=['absent', 'present']),
        jwt_token=dict(type='str', required=True, no_log=True),
        name=dict(required=True, type='str'),
        params=dict(type='dict'),
        description=dict(type='str', required=True),
        email=dict(type='str', required=True),
        account_id=dict(type='str', required=True),
        optins=dict(default='present', choices=['absent', 'present']),
        enable_cleanup_of_attached_files=dict(type='bool', default=False),
        enable_appsignature_sync=dict(type='bool', default=False),
        enable_ip_reputation=dict(type='bool', default=False),
        enable_pulse_case_management=dict(type='bool', default=False),
        enable_pulse_waf_management=dict(type='bool', default=False),
        enable_user_agent_db_sync=dict(type='bool', default=False),
        use_tls=dict(type='bool', default=False),
        waf_config=dict(type='dict', options=waf_spec),
        case_config=dict(type='dict', options=case_spec)
    )
    argument_specs.update(avi_common_argument_spec())
    module = AnsibleModule(argument_spec=argument_specs, supports_check_mode=True)
    if not HAS_REQUESTS:
        return module.fail_json(msg=(
            'Python requests package is not installed. '
            'For installation instructions, visit https://pypi.org/project/requests.'))

    api_creds = AviCredentials()
    api_creds.update_from_ansible_module(module)
    api = ApiSession.get_session(
        api_creds.controller, api_creds.username, password=api_creds.password,
        api_version=api_creds.api_version, timeout=api_creds.timeout,
        tenant=api_creds.tenant, tenant_uuid=api_creds.tenant_uuid,
        token=api_creds.token, port=api_creds.port)
    api_version = api_creds.api_version
    tenant_uuid = api_creds.tenant_uuid
    tenant = api_creds.tenant
    check_mode = module.check_mode
    path = module.params.get('path', '')
    state = module.params.get('state', None)
    jwt_token = module.params.get('jwt_token', None)
    name = module.params.get('name', None)
    description = module.params.get('description', None)
    email = module.params.get('email', None)
    account_id = module.params.get('account_id', None)
    portal_url = 'https://portal.avipulse.vmware.com'
    optins = module.params.get('optins', None)
    enable_cleanup_of_attached_files = module.params.get('enable_cleanup_of_attached_files', None)
    enable_appsignature_sync = module.params.get('enable_appsignature_sync', None)
    enable_ip_reputation = module.params.get('enable_ip_reputation', None)
    enable_pulse_case_management = module.params.get('enable_pulse_case_management', None)
    enable_pulse_waf_management = module.params.get('enable_pulse_waf_management', None)
    enable_user_agent_db_sync = module.params.get('enable_user_agent_db_sync', None)
    use_tls = module.params.get('use_tls', None)
    waf_config = module.params.get('waf_config', None)
    case_config = module.params.get('case_config', None)
    if waf_config:
        enable_auto_download_waf_signatures = module.params.get('waf_config', dict()).get('enable_auto_download_waf_signatures', None)
        enable_waf_signatures_notifications = module.params.get('waf_config', dict()).get('enable_waf_signatures_notifications', None)
    else:
        enable_auto_download_waf_signatures = False
        enable_waf_signatures_notifications = False
    if case_config:
        enable_auto_case_creation_on_controller_failure = module.params.get('case_config', dict()).get('enable_auto_case_creation_on_controller_failure', None)
        enable_auto_case_creation_on_se_failure = module.params.get('case_config', dict()).get('enable_auto_case_creation_on_se_failure', None)
    else:
        enable_auto_case_creation_on_controller_failure = False
        enable_auto_case_creation_on_se_failure = False
    reg = True

    if state == 'present':
        # registration
        path = "albservices/status"
        resp = api.get(path, tenant=tenant, tenant_uuid=tenant_uuid, api_version=api_version)
        existing_obj = resp
        if not (check_mode) and resp.json().get("connectivity_status") == "ALBSERVICES_DISCONNECTED":
            headers = {'Content-Type': 'application/json', 'Authorization': 'Basic YWRtaW46YWRtaW4='}
            data = {"jwt_token": jwt_token}
            path = "portal/refresh-access-token"
            rsp = api.post(path, api_version=api_version, headers=headers, data=data)
            if rsp.status_code > 300:
                return module.fail_json(msg='Failed: %s' % rsp.text)
            else:
                changed = True
                time.sleep(10)

        if resp.json().get("registration_status") == "ALBSERVICES_DEREGISTERED":
            if not check_mode:
                path = "albservices/register"
                data = {"name": name, "description": description, "email": email,
                        "account_id": account_id}
                rsp = api.post(path, data=data)
                changed = True
                time.sleep(5)
            else:
                # No need to process any further.
                rsp = AviCheckModeResponse(obj=existing_obj)
                changed = True

        if resp.json().get("registration_status") == "ALBSERVICES_REGISTERED":
            changed = False
            reg = False

        if reg and rsp.status_code > 300:
            return module.fail_json(msg='Failed: %s' % rsp.text)
        else:
            if optins == 'present':
                if enable_pulse_case_management is False and (enable_auto_case_creation_on_se_failure or enable_auto_case_creation_on_controller_failure):
                    return module.fail_json(msg='Unable to enable the options as enable_pulse_case_management is not enabled.')

                if enable_pulse_waf_management is False and (enable_auto_download_waf_signatures or enable_waf_signatures_notifications):
                    return module.fail_json(msg='Unable to enable the options as enable_pulse_waf_management is not enabled.')
                path = "albservicesconfig"
                response = api.get(path, tenant=tenant, tenant_uuid=tenant_uuid,
                                   api_version=api_version)
                path = "albservicesconfig"
                data = dict()
                data["portal_url"] = portal_url
                data["polling_interval"] = 10
                data["feature_opt_in_status"] = dict()
                data[("feature_opt_in_status")]["enable_appsignature_sync"] = enable_appsignature_sync
                data[("feature_opt_in_status")]["enable_ip_reputation"] = enable_ip_reputation
                data[("feature_opt_in_status")]["enable_pulse_case_management"] = enable_pulse_case_management
                data[("feature_opt_in_status")]["enable_pulse_waf_management"] = enable_pulse_waf_management
                data[("feature_opt_in_status")]["enable_user_agent_db_sync"] = enable_user_agent_db_sync
                data[("tenant_config")] = dict()
                data[("tenant_config")]["heartbeat_interval"] = 3
                data[("tenant_config")]["token_refresh_interval"] = 57
                data[("tenant_config")]["license_escrow_interval"] = 60
                data["ip_reputation_config"] = dict()
                data[("ip_reputation_config")]["ip_reputation_file_object_expiry_duration"] = 3
                data[("ip_reputation_config")]["ip_reputation_sync_interval"] = 60
                data["use_tls"] = use_tls
                data["mode"] = "MYVMWARE"
                data["app_signature_config"] = dict()
                data[("app_signature_config")]["app_signature_sync_interval"] = 1440
                data["user_agent_db_config"] = dict()
                data[("user_agent_db_config")]["allowed_batch_size"] = 500
                data["waf_config"] = dict()
                data[("waf_config")]["enable_auto_download_waf_signatures"] = enable_auto_download_waf_signatures
                data[("waf_config")]["enable_waf_signatures_notifications"] = enable_waf_signatures_notifications
                data["case_config"] = dict()
                data[("case_config")]["enable_auto_case_creation_on_controller_failure"] = enable_auto_case_creation_on_controller_failure
                data[("case_config")]["enable_auto_case_creation_on_se_failure"] = enable_auto_case_creation_on_se_failure
                data[("case_config")]["enable_cleanup_of_attached_files"] = enable_cleanup_of_attached_files
                data["saas_licensing_config"] = dict()
                data[("saas_licensing_config")]["max_service_units"] = 1000
                data[("saas_licensing_config")]["reserve_service_units"] = 0
                data_for_cmp = data
                response_data = response.json()
                ch = not avi_obj_cmp(data_for_cmp, response_data)
                if ch:
                    if not check_mode:
                        rsp = api.put(path, data=data)
                        changed = True
                    else:
                        rsp = AviCheckModeResponse(obj=existing_obj)
                        changed = True
            return module.exit_json(changed=changed, msg='Registered successfully')
    else:
        # deregistration
        reg = True
        path = "albservices/status"
        resp = api.get(path, tenant=tenant, tenant_uuid=tenant_uuid,
                       api_version=api_version)
        existing_obj = resp
        if resp.json().get("registration_status") == "ALBSERVICES_REGISTERED":
            if not check_mode:
                path = "albservices/register"
                data = {"status": "Obsolete"}
                rsp = api.put(path, data=data)
                changed = True
            else:
                rsp = AviCheckModeResponse(obj=existing_obj)
                changed = True

        if resp.json().get("registration_status") == "ALBSERVICES_DEREGISTERED":
            changed = False
            reg = False
        if reg and rsp.status_code > 300:
            return module.fail_json(msg='Failed: %s' % rsp.text)
        else:
            return module.exit_json(
                changed=changed, msg="Deregistered successfully")


if __name__ == '__main__':
    main()
