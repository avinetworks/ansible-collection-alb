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
module: avi_systemconfiguration
author: Gaurav Rastogi (@grastogi23) <grastogi@avinetworks.com>
short_description: Module for setup of SystemConfiguration Avi RESTful Object
description:
    - This module is used to configure SystemConfiguration object
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
    admin_auth_configuration:
        description:
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: dict
    common_criteria_mode:
        description:
            - Common criteria mode's current state.
            - Field introduced in 20.1.3.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    configpb_attributes:
        description:
            - Protobuf versioning for config pbs.
            - Field introduced in 21.1.1.
            - Allowed in enterprise edition with any value, essentials edition with any value, basic edition with any value, enterprise with cloud services
            - edition.
        type: dict
    controller_analytics_policy:
        description:
            - Controller metrics event dynamic thresholds can be set here.
            - Controller_cpu_high and controller_mem_high evets can take configured dynamic thresholds.
            - Field introduced in 21.1.3.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
        type: dict
    default_license_tier:
        description:
            - Specifies the default license tier which would be used by new clouds.
            - Enum options - ENTERPRISE_16, ENTERPRISE, ENTERPRISE_18, BASIC, ESSENTIALS, ENTERPRISE_WITH_CLOUD_SERVICES.
            - Field introduced in 17.2.5.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Special default for essentials edition is essentials, basic edition is basic, enterprise is enterprise_with_cloud_services.
            - Default value when not specified in API or module is interpreted by Avi Controller as ENTERPRISE_WITH_CLOUD_SERVICES.
        type: str
    dns_configuration:
        description:
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: dict
    dns_virtualservice_refs:
        description:
            - Dns virtualservices hosting fqdn records for applications across avi vantage.
            - If no virtualservices are provided, avi vantage will provide dns services for configured applications.
            - Switching back to avi vantage from dns virtualservices is not allowed.
            - It is a reference to an object of type virtualservice.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
        type: list
        elements: str
    docker_mode:
        description:
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    email_configuration:
        description:
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: dict
    enable_cors:
        description:
            - Enable cors header.
            - Field introduced in 20.1.3.
            - Allowed in enterprise edition with any value, essentials edition with any value, basic edition with any value, enterprise with cloud services
            - edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    enable_host_header_check:
        description:
            - Host header check.
            - Field introduced in 31.1.1.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    fips_mode:
        description:
            - Fips mode current state.
            - Field introduced in 20.1.1.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    global_tenant_config:
        description:
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: dict
    host_key_algorithm_exclude:
        description:
            - Users can specify comma separated list of deprecated host key algorithm.if nothing is specified, all known algorithms provided by openssh will be
            - supported.this change could only apply on the controller node.
            - Field introduced in 22.1.3.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: str
    kex_algorithm_exclude:
        description:
            - Users can specify comma separated list of deprecated key exchange algorithm.if nothing is specified, all known algorithms provided by openssh
            - will be supported.this change could only apply on the controller node.
            - Field introduced in 22.1.3.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: str
    linux_configuration:
        description:
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: dict
    mgmt_ip_access_control:
        description:
            - Configure ip access control for controller to restrict open access.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: dict
    ntp_configuration:
        description:
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: dict
    portal_configuration:
        description:
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: dict
    proxy_configuration:
        description:
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: dict
    rekey_time_limit:
        description:
            - Users can specify and update the time limit of rekeylimit in sshd_config.if nothing is specified, the default setting will be none.
            - Field introduced in 30.2.1.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as none.
        type: str
    rekey_volume_limit:
        description:
            - Users can specify and update the size/volume limit of rekeylimit in sshd_config.if nothing is specified, the default setting will be default.
            - Field introduced in 30.2.1.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as default.
        type: str
    secure_channel_configuration:
        description:
            - Configure secure channel properties.
            - Field introduced in 18.1.4, 18.2.1.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: dict
    snmp_configuration:
        description:
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: dict
    ssh_ciphers:
        description:
            - Allowed ciphers list for ssh to the management interface on the controller and service engines.
            - If this is not specified, all the default ciphers are allowed.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: list
        elements: str
    ssh_hmacs:
        description:
            - Allowed hmac list for ssh to the management interface on the controller and service engines.
            - If this is not specified, all the default hmacs are allowed.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: list
        elements: str
    trusted_host_profiles_refs:
        description:
            - Trusted host profiles for host header validation.
            - Only function when enable_host_header_check is set to true.
            - It is a reference to an object of type trustedhostprofile.
            - Field introduced in 31.1.1.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
        type: list
        elements: str
    url:
        description:
            - Avi controller URL of the object.
        type: str
    uuid:
        description:
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: str
    welcome_workflow_complete:
        description:
            - This flag is set once the initial controller setup workflow is complete.
            - Field introduced in 18.2.3.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
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

- hosts: all
  vars:
    avi_credentials:
      username: "admin"
      password: "something"
      controller: "192.168.15.18"
      api_version: "21.1.1"
  tasks:
    - name: Example to create SystemConfiguration object
      vmware.alb.avi_systemconfiguration:
        avi_credentials: "{{ avi_credentials }}"
        state: present
        welcome_workflow_complete: True
        dns_configuration:
          search_domain: ''
          server_list:
            - type: V4
              addr: "8.8.8.8"
            - type: DNS
              addr: "dns.rainpole.com"
"""

RETURN = '''
obj:
    description: SystemConfiguration (api/systemconfiguration) object
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
        admin_auth_configuration=dict(type='dict',),
        common_criteria_mode=dict(type='bool',),
        configpb_attributes=dict(type='dict',),
        controller_analytics_policy=dict(type='dict',),
        default_license_tier=dict(type='str',),
        dns_configuration=dict(type='dict',),
        dns_virtualservice_refs=dict(type='list', elements='str',),
        docker_mode=dict(type='bool',),
        email_configuration=dict(type='dict',),
        enable_cors=dict(type='bool',),
        enable_host_header_check=dict(type='bool',),
        fips_mode=dict(type='bool',),
        global_tenant_config=dict(type='dict',),
        host_key_algorithm_exclude=dict(type='str',),
        kex_algorithm_exclude=dict(type='str',),
        linux_configuration=dict(type='dict',),
        mgmt_ip_access_control=dict(type='dict',),
        ntp_configuration=dict(type='dict',),
        portal_configuration=dict(type='dict',),
        proxy_configuration=dict(type='dict',),
        rekey_time_limit=dict(type='str',),
        rekey_volume_limit=dict(type='str',),
        secure_channel_configuration=dict(type='dict',),
        snmp_configuration=dict(type='dict',),
        ssh_ciphers=dict(type='list', elements='str',),
        ssh_hmacs=dict(type='list', elements='str',),
        trusted_host_profiles_refs=dict(type='list', elements='str',),
        url=dict(type='str',),
        uuid=dict(type='str',),
        welcome_workflow_complete=dict(type='bool',),
    )
    argument_specs.update(avi_common_argument_spec())
    module = AnsibleModule(
        argument_spec=argument_specs, supports_check_mode=True)
    if not HAS_REQUESTS:
        return module.fail_json(msg=(
            'Python requests package is not installed. '
            'For installation instructions, visit https://pypi.org/project/requests.'))
    return avi_ansible_api(module, 'systemconfiguration',
                           set())


if __name__ == '__main__':
    main()
