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
module: avi_ipreputationdb
author: Gaurav Rastogi (@grastogi23) <grastogi@avinetworks.com>
short_description: Module for setup of IPReputationDB Avi RESTful Object
description:
    - This module is used to configure IPReputationDB object
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
    base_file_refs:
        description:
            - Ip reputation db base file.
            - It is a reference to an object of type fileobject.
            - Field introduced in 20.1.1.
            - Maximum of 1 items allowed.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: list
        elements: str
    base_file_v6_refs:
        description:
            - Ip reputation db base file for ipv6.
            - It is a reference to an object of type fileobject.
            - Field introduced in 31.1.1.
            - Maximum of 1 items allowed.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
        type: list
        elements: str
    configpb_attributes:
        description:
            - Protobuf versioning for config pbs.
            - Field introduced in 21.1.1.
            - Allowed in enterprise edition with any value, essentials edition with any value, basic edition with any value, enterprise with cloud services
            - edition.
        type: dict
    description:
        description:
            - Description.
            - Field introduced in 20.1.1.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: str
    incremental_file_refs:
        description:
            - Ip reputation db incremental update files.
            - It is a reference to an object of type fileobject.
            - Field introduced in 20.1.1.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: list
        elements: str
    incremental_file_v6_refs:
        description:
            - Ip reputation db incremental update files for ipv6.
            - It is a reference to an object of type fileobject.
            - Field introduced in 31.1.1.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
        type: list
        elements: str
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
            - Ip reputation db name.
            - Field introduced in 20.1.1.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        required: true
        type: str
    service_status:
        description:
            - If this object is managed by the ip reputation service, this field contain the status of this syncronization.
            - Field introduced in 20.1.1.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: dict
    tenant_ref:
        description:
            - Tenant that this object belongs to.
            - It is a reference to an object of type tenant.
            - Field introduced in 20.1.1.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: str
    url:
        description:
            - Avi controller URL of the object.
        type: str
    uuid:
        description:
            - Uuid of this object.
            - Field introduced in 20.1.1.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: str
    vendor:
        description:
            - Organization providing ip reputation data.
            - Enum options - IP_REPUTATION_VENDOR_WEBROOT.
            - Field introduced in 20.1.1.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        required: true
        type: str
    version:
        description:
            - A version number for this database object.
            - This is informal for the consumer of this api only, a tool which manages this object can store version information here.
            - Field introduced in 20.1.1.
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

- name: Example to create IPReputationDB object
  vmware.alb.avi_ipreputationdb:
    avi_credentials: "{{ avi_credentials }}"
    state: present
    name: sample_ipreputationdb
"""

RETURN = '''
obj:
    description: IPReputationDB (api/ipreputationdb) object
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
        base_file_refs=dict(type='list', elements='str',),
        base_file_v6_refs=dict(type='list', elements='str',),
        configpb_attributes=dict(type='dict',),
        description=dict(type='str',),
        incremental_file_refs=dict(type='list', elements='str',),
        incremental_file_v6_refs=dict(type='list', elements='str',),
        markers=dict(type='list', elements='dict',),
        name=dict(type='str', required=True),
        service_status=dict(type='dict',),
        tenant_ref=dict(type='str',),
        url=dict(type='str',),
        uuid=dict(type='str',),
        vendor=dict(type='str', required=True),
        version=dict(type='str',),
    )
    argument_specs.update(avi_common_argument_spec())
    module = AnsibleModule(
        argument_spec=argument_specs, supports_check_mode=True)
    if not HAS_REQUESTS:
        return module.fail_json(msg=(
            'Python requests package is not installed. '
            'For installation instructions, visit https://pypi.org/project/requests.'))
    return avi_ansible_api(module, 'ipreputationdb',
                           set())


if __name__ == '__main__':
    main()
