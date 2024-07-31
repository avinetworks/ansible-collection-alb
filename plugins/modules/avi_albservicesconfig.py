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
module: avi_albservicesconfig
author: Gaurav Rastogi (@grastogi23) <grastogi@avinetworks.com>
short_description: Module for setup of ALBServicesConfig Avi RESTful Object
description:
    - This module is used to configure ALBServicesConfig object
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
    app_signature_config:
        description:
            - Default values for application signature sync.
            - Field introduced in 20.1.4.
            - Allowed in enterprise edition with any value, essentials edition with any value, basic edition with any value, enterprise with cloud services
            - edition.
        required: true
        type: dict
    asset_contact:
        description:
            - Default contact for this controller cluster.
            - Field introduced in 20.1.1.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: dict
    case_config:
        description:
            - Default values for case management.
            - Field introduced in 21.1.1.
            - Allowed in enterprise edition with any value, essentials edition with any value, basic edition with any value, enterprise with cloud services
            - edition.
        required: true
        type: dict
    configpb_attributes:
        description:
            - Protobuf versioning for config pbs.
            - Field introduced in 21.1.1.
            - Allowed in enterprise edition with any value, essentials edition with any value, basic edition with any value, enterprise with cloud services
            - edition.
        type: dict
    feature_opt_in_status:
        description:
            - Features opt-in for pulse cloud services.
            - Field introduced in 20.1.1.
        required: true
        type: dict
    inventory_config:
        description:
            - Inventory configurations for pulse cloud services.
            - Field introduced in 30.2.1.
            - Allowed in enterprise edition with any value, essentials edition with any value, basic edition with any value, enterprise with cloud services
            - edition.
        required: true
        type: dict
    ip_reputation_config:
        description:
            - Default values to be used for ip reputation sync.
            - Field introduced in 20.1.1.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        required: true
        type: dict
    mode:
        description:
            - Mode helps log collection and upload.
            - Enum options - MODE_UNKNOWN, SALESFORCE, SYSTEST, MYVMWARE, BROADCOM.
            - Field introduced in 20.1.2.
            - Allowed in enterprise edition with any value, essentials edition(allowed values- salesforce,myvmware,systest), basic edition(allowed values-
            - salesforce,myvmware,systest), enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as MYVMWARE.
        type: str
    name:
        description:
            - Name of the albservicesconfig object.
            - Field introduced in 30.1.1.
            - Allowed in enterprise edition with any value, essentials edition with any value, basic edition with any value, enterprise with cloud services
            - edition.
        type: str
    polling_interval:
        description:
            - Time interval in minutes.
            - Allowed values are 5-60.
            - Field introduced in 18.2.6.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 10.
        type: int
    portal_url:
        description:
            - The fqdn or ip address of the pulse cloud services.
            - Field introduced in 18.2.6.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        required: true
        type: str
    saas_licensing_config:
        description:
            - Saas licensing configuration.
            - Field introduced in 21.1.3.
            - Allowed in enterprise edition with any value, essentials edition with any value, basic edition with any value, enterprise with cloud services
            - edition.
        required: true
        type: dict
    session_config:
        description:
            - Session configuration data.
            - Field introduced in 30.2.1.
            - Allowed in enterprise edition with any value, essentials edition with any value, basic edition with any value, enterprise with cloud services
            - edition.
        type: dict
    split_proxy_configuration:
        description:
            - Split proxy configuration to connect external pulse cloud services.
            - Field introduced in 20.1.1.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: dict
    tenant_config:
        description:
            - Tenant based configuration data.
            - Field introduced in 30.2.1.
            - Allowed in enterprise edition with any value, essentials edition with any value, basic edition with any value, enterprise with cloud services
            - edition.
        type: dict
    tenant_ref:
        description:
            - Tenant uuid associated with the object.
            - It is a reference to an object of type tenant.
            - Field introduced in 30.1.1.
            - Allowed in enterprise edition with any value, essentials edition with any value, basic edition with any value, enterprise with cloud services
            - edition.
        type: str
    url:
        description:
            - Avi controller URL of the object.
        type: str
    use_split_proxy:
        description:
            - By default, pulse cloud services uses proxy added in system configuration.
            - If it should use a separate proxy, set this flag to true and configure split proxy configuration.
            - Field introduced in 20.1.1.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    use_tls:
        description:
            - Secure the controller to pulse cloud services communication over tls.
            - Field introduced in 20.1.3.
            - Allowed in enterprise edition with any value, basic edition with any value, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as True.
        type: bool
    user_agent_db_config:
        description:
            - Default values for user agent db service.
            - Field introduced in 21.1.1.
            - Allowed in enterprise edition with any value, essentials edition with any value, basic edition with any value, enterprise with cloud services
            - edition.
        required: true
        type: dict
    uuid:
        description:
            - Field introduced in 18.2.6.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: str
    waf_config:
        description:
            - Default values for waf management.
            - Field introduced in 21.1.1.
            - Allowed in essentials edition with any value, basic edition with any value, enterprise, enterprise with cloud services edition.
        required: true
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

- name: Example to create ALBServicesConfig object
  vmware.alb.avi_albservicesconfig:
    avi_credentials: "{{ avi_credentials }}"
    state: present
    name: sample_albservicesconfig
"""

RETURN = '''
obj:
    description: ALBServicesConfig (api/albservicesconfig) object
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
        app_signature_config=dict(type='dict', required=True),
        asset_contact=dict(type='dict',),
        case_config=dict(type='dict', required=True),
        configpb_attributes=dict(type='dict',),
        feature_opt_in_status=dict(type='dict', required=True),
        inventory_config=dict(type='dict', required=True),
        ip_reputation_config=dict(type='dict', required=True),
        mode=dict(type='str',),
        name=dict(type='str',),
        polling_interval=dict(type='int',),
        portal_url=dict(type='str', required=True),
        saas_licensing_config=dict(type='dict', required=True),
        session_config=dict(type='dict',),
        split_proxy_configuration=dict(type='dict',),
        tenant_config=dict(type='dict',),
        tenant_ref=dict(type='str',),
        url=dict(type='str',),
        use_split_proxy=dict(type='bool',),
        use_tls=dict(type='bool',),
        user_agent_db_config=dict(type='dict', required=True),
        uuid=dict(type='str',),
        waf_config=dict(type='dict', required=True),
    )
    argument_specs.update(avi_common_argument_spec())
    module = AnsibleModule(
        argument_spec=argument_specs, supports_check_mode=True)
    if not HAS_REQUESTS:
        return module.fail_json(msg=(
            'Python requests package is not installed. '
            'For installation instructions, visit https://pypi.org/project/requests.'))
    return avi_ansible_api(module, 'albservicesconfig',
                           set())


if __name__ == '__main__':
    main()
