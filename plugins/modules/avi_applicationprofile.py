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
module: avi_applicationprofile
author: Gaurav Rastogi (@grastogi23) <grastogi@avinetworks.com>
short_description: Module for setup of ApplicationProfile Avi RESTful Object
description:
    - This module is used to configure ApplicationProfile object
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
    app_service_type:
        description:
            - Specifies app service type for an application.
            - Enum options - APP_SERVICE_TYPE_L7_HORIZON, APP_SERVICE_TYPE_L4_BLAST, APP_SERVICE_TYPE_L4_PCOIP, APP_SERVICE_TYPE_L4_FTP.
            - Field introduced in 21.1.3.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
        type: str
    cloud_config_cksum:
        description:
            - Checksum of application profiles.
            - Internally set by cloud connector.
            - Field introduced in 17.2.14, 18.1.5, 18.2.1.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: str
    configpb_attributes:
        description:
            - Protobuf versioning for config pbs.
            - Field introduced in 21.1.1.
            - Allowed in enterprise edition with any value, essentials edition with any value, basic edition with any value, enterprise with cloud services
            - edition.
        type: dict
    created_by:
        description:
            - Name of the application profile creator.
            - Field introduced in 17.2.14, 18.1.5, 18.2.1.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: str
    description:
        description:
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: str
    diameter_service_profile:
        description:
            - Specifies various diameter service related controls for virtual service.
            - Field introduced in 31.1.1.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
        type: dict
    dns_service_profile:
        description:
            - Specifies various dns service related controls for virtual service.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
        type: dict
    dos_rl_profile:
        description:
            - Specifies various security related controls for virtual service.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
        type: dict
    http_profile:
        description:
            - Specifies the http application proxy profile parameters.
            - Allowed in enterprise edition with any value, basic, enterprise with cloud services edition.
        type: dict
    l4_ssl_profile:
        description:
            - Specifies various l4 ssl service related controls for virtual service.
            - Field introduced in 22.1.2.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
        type: dict
    markers:
        description:
            - List of labels to be used for granular rbac.
            - Field introduced in 20.1.5.
            - Allowed in enterprise edition with any value, essentials edition with any value, basic edition with any value, enterprise with cloud services
            - edition.
        type: list
        elements: dict
    name:
        description:
            - The name of the application profile.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        required: true
        type: str
    preserve_client_ip:
        description:
            - Specifies if client ip needs to be preserved for backend connection.
            - Not compatible with connection multiplexing.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    preserve_client_port:
        description:
            - Specifies if we need to preserve client port while preserving client ip for backend connections.
            - Field introduced in 17.2.7.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: bool
    preserve_dest_ip_port:
        description:
            - Specifies if destination ip and port needs to be preserved for backend connection.
            - Field introduced in 20.1.1.
            - Allowed in enterprise edition with any value, essentials edition(allowed values- false), basic edition(allowed values- false), enterprise with
            - cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    sip_service_profile:
        description:
            - Specifies various sip service related controls for virtual service.
            - Field introduced in 17.2.8, 18.1.3, 18.2.1.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
        type: dict
    tcp_app_profile:
        description:
            - Specifies the tcp application proxy profile parameters.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: dict
    tenant_ref:
        description:
            - It is a reference to an object of type tenant.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: str
    type:
        description:
            - Specifies which application layer proxy is enabled for the virtual service.
            - Enum options - APPLICATION_PROFILE_TYPE_L4, APPLICATION_PROFILE_TYPE_HTTP, APPLICATION_PROFILE_TYPE_SYSLOG, APPLICATION_PROFILE_TYPE_DNS,
            - APPLICATION_PROFILE_TYPE_SSL, APPLICATION_PROFILE_TYPE_SIP, APPLICATION_PROFILE_TYPE_DIAMETER.
            - Allowed in enterprise edition with any value, essentials edition(allowed values- application_profile_type_l4), basic edition(allowed values-
            - application_profile_type_l4,application_profile_type_http), enterprise with cloud services edition.
        required: true
        type: str
    url:
        description:
            - Avi controller URL of the object.
        type: str
    uuid:
        description:
            - Uuid of the application profile.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
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

- name: Create an Application Profile for HTTP application enabled for SSL traffic
  vmware.alb.avi_applicationprofile:
    avi_credentials: "{{ avi_credentials }}"
    http_profile:
      cache_config:
        age_header: true
        aggressive: false
        date_header: true
        default_expire: 600
        enabled: false
        heuristic_expire: false
        max_cache_size: 0
        max_object_size: 4194304
        mime_types_group_refs:
        - admin:System-Cacheable-Resource-Types
        min_object_size: 100
        query_cacheable: false
        xcache_header: true
      client_body_timeout: 0
      client_header_timeout: 10000
      client_max_body_size: 0
      client_max_header_size: 12
      client_max_request_size: 48
      compression_profile:
        compressible_content_ref: admin:System-Compressible-Content-Types
        compression: false
        remove_accept_encoding_header: true
        type: AUTO_COMPRESSION
      connection_multiplexing_enabled: true
      hsts_enabled: false
      hsts_max_age: 365
      http_to_https: false
      httponly_enabled: false
      keepalive_header: false
      keepalive_timeout: 30000
      max_bad_rps_cip: 0
      max_bad_rps_cip_uri: 0
      max_bad_rps_uri: 0
      max_rps_cip: 0
      max_rps_cip_uri: 0
      max_rps_unknown_cip: 0
      max_rps_unknown_uri: 0
      max_rps_uri: 0
      post_accept_timeout: 30000
      secure_cookie_enabled: false
      server_side_redirect_to_https: false
      spdy_enabled: false
      spdy_fwd_proxy_mode: false
      ssl_client_certificate_mode: SSL_CLIENT_CERTIFICATE_NONE
      ssl_everywhere_enabled: false
      websockets_enabled: true
      x_forwarded_proto_enabled: false
      xff_alternate_name: X-Forwarded-For
      xff_enabled: true
    name: System-HTTP
    tenant_ref: /api/tenant?name=admin
    type: APPLICATION_PROFILE_TYPE_HTTP
"""

RETURN = '''
obj:
    description: ApplicationProfile (api/applicationprofile) object
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
        app_service_type=dict(type='str',),
        cloud_config_cksum=dict(type='str',),
        configpb_attributes=dict(type='dict',),
        created_by=dict(type='str',),
        description=dict(type='str',),
        diameter_service_profile=dict(type='dict',),
        dns_service_profile=dict(type='dict',),
        dos_rl_profile=dict(type='dict',),
        http_profile=dict(type='dict',),
        l4_ssl_profile=dict(type='dict',),
        markers=dict(type='list', elements='dict',),
        name=dict(type='str', required=True),
        preserve_client_ip=dict(type='bool',),
        preserve_client_port=dict(type='bool',),
        preserve_dest_ip_port=dict(type='bool',),
        sip_service_profile=dict(type='dict',),
        tcp_app_profile=dict(type='dict',),
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
    return avi_ansible_api(module, 'applicationprofile',
                           set())


if __name__ == '__main__':
    main()
