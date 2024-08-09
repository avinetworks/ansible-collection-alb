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
module: avi_fileobject
author: Gaurav Rastogi (@grastogi23) <grastogi@avinetworks.com>
short_description: Module for setup of FileObject Avi RESTful Object
description:
    - This module is used to configure FileObject object
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
    checksum:
        description:
            - Sha1 checksum of the file.
            - Field introduced in 20.1.1.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: str
    compressed:
        description:
            - This field indicates whether the file is gzip-compressed.
            - Field introduced in 20.1.1.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    configpb_attributes:
        description:
            - Protobuf versioning for config pbs.
            - Field introduced in 30.2.1.
            - Allowed in enterprise edition with any value, essentials edition with any value, basic edition with any value, enterprise with cloud services
            - edition.
        type: dict
    created:
        description:
            - Timestamp of creation for the file.
            - Field introduced in 20.1.1.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: str
    crl_info:
        description:
            - This field contains certificate revocation list metadata.
            - Field introduced in 30.2.1.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
        type: dict
    description:
        description:
            - Description of the file.
            - Field introduced in 20.1.1.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: str
    expires_at:
        description:
            - Timestamp when the file will be no longer needed and can be removed by the system.
            - If this is set, a garbage collector process will try to remove the file after this time.
            - Field introduced in 20.1.1.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: str
    is_federated:
        description:
            - This field describes the object's replication scope.
            - If the field is set to false, then the object is visible within the controller-cluster and its associated service-engines.
            - If the field is set to true, then the object is replicated across the federation.
            - Field introduced in 20.1.1.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    name:
        description:
            - Name of the file object.
            - Field introduced in 20.1.1.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        required: true
        type: str
    path:
        description:
            - Path to the file.
            - Field introduced in 20.1.1.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: str
    read_only:
        description:
            - Enforce read-only on the file.
            - Field introduced in 20.1.1.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: bool
    restrict_download:
        description:
            - Flag to allow/restrict download of the file.
            - Field introduced in 20.1.1.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: bool
    size:
        description:
            - Size of the file.
            - Field introduced in 20.1.1.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: int
    tenant_ref:
        description:
            - Tenant that this object belongs to.
            - It is a reference to an object of type tenant.
            - Field introduced in 20.1.1.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: str
    type:
        description:
            - Type of the file.
            - Enum options - OTHER_FILE_TYPES, IP_REPUTATION, GEO_DB, TECH_SUPPORT, HSMPACKAGES, IPAMDNSSCRIPTS, CONTROLLER_IMAGE, CRL_DATA,
            - IP_REPUTATION_IPV6.
            - Field introduced in 20.1.1.
            - Allowed in enterprise edition with any value, essentials edition(allowed values- other_file_types), basic edition(allowed values-
            - other_file_types), enterprise with cloud services edition.
        required: true
        type: str
    url:
        description:
            - Avi controller URL of the object.
        type: str
    uuid:
        description:
            - Uuid of the file.
            - Field introduced in 20.1.1.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: str
    version:
        description:
            - Version of the file.
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

- name: Example to create FileObject object
  vmware.alb.avi_fileobject:
    avi_credentials: "{{ avi_credentials }}"
    state: present
    name: sample_fileobject
"""

RETURN = '''
obj:
    description: FileObject (api/fileobject) object
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
        checksum=dict(type='str',),
        compressed=dict(type='bool',),
        configpb_attributes=dict(type='dict',),
        created=dict(type='str',),
        crl_info=dict(type='dict',),
        description=dict(type='str',),
        expires_at=dict(type='str',),
        is_federated=dict(type='bool',),
        name=dict(type='str', required=True),
        path=dict(type='str',),
        read_only=dict(type='bool',),
        restrict_download=dict(type='bool',),
        size=dict(type='int',),
        tenant_ref=dict(type='str',),
        type=dict(type='str', required=True),
        url=dict(type='str',),
        uuid=dict(type='str',),
        version=dict(type='str',),
    )
    argument_specs.update(avi_common_argument_spec())
    module = AnsibleModule(
        argument_spec=argument_specs, supports_check_mode=True)
    if not HAS_REQUESTS:
        return module.fail_json(msg=(
            'Python requests package is not installed. '
            'For installation instructions, visit https://pypi.org/project/requests.'))
    return avi_ansible_api(module, 'fileobject',
                           set())


if __name__ == '__main__':
    main()
