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
module: avi_siteversion
author: Gaurav Rastogi (@grastogi23) <grastogi@avinetworks.com>
short_description: Module for setup of SiteVersion Avi RESTful Object
description:
    - This module is used to configure SiteVersion object
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
    datetime:
        description:
            - This field represents the creation time of the federateddiff.
            - Field introduced in 20.1.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    name:
        description:
            - Name of the site.
            - Field introduced in 20.1.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        required: true
        type: str
    prev_target_version:
        description:
            - Previous targer version for a site.
            - Field introduced in 20.1.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: int
    replication_state:
        description:
            - Replication state for a site.
            - Enum options - REPLICATION_STATE_FASTFORWARD, REPLICATION_STATE_FORCESYNC, REPLICATION_STATE_STREAMING, REPLICATION_STATE_SUSPENDED,
            - REPLICATION_STATE_INIT, REPLICATION_STATE_WAIT, REPLICATION_STATE_NOT_APPLICABLE, REPLICATION_STATE_SYNC_STALLED.
            - Field introduced in 20.1.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    site_id:
        description:
            - Cluster uuid of the site.
            - Field introduced in 20.1.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    target_timeline:
        description:
            - Target timeline of the site.
            - Field introduced in 20.1.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    target_version:
        description:
            - Target version of the site.
            - Field introduced in 20.1.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: int
    tenant_ref:
        description:
            - Tenant that this object belongs to.
            - It is a reference to an object of type tenant.
            - Field introduced in 20.1.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    timeline:
        description:
            - Timeline of the site.
            - Field introduced in 20.1.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    url:
        description:
            - Avi controller URL of the object.
        type: str
    uuid:
        description:
            - Uuid of the siteversion object.
            - Field introduced in 20.1.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    version:
        description:
            - Version of the site.
            - Field introduced in 20.1.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: int
    version_type:
        description:
            - Type of message for which version is maintained.
            - Enum options - CONFIG_VERSION, HEALTH_STATUS_VERSION.
            - Field introduced in 20.1.1.
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

- name: Example to create SiteVersion object
  vmware.alb.avi_siteversion:
    avi_credentials: "{{ avi_credentials }}"
    state: present
    name: sample_siteversion
"""

RETURN = '''
obj:
    description: SiteVersion (api/siteversion) object
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
        datetime=dict(type='str',),
        name=dict(type='str', required=True),
        prev_target_version=dict(type='int',),
        replication_state=dict(type='str',),
        site_id=dict(type='str',),
        target_timeline=dict(type='str',),
        target_version=dict(type='int',),
        tenant_ref=dict(type='str',),
        timeline=dict(type='str',),
        url=dict(type='str',),
        uuid=dict(type='str',),
        version=dict(type='int',),
        version_type=dict(type='str',),
    )
    argument_specs.update(avi_common_argument_spec())
    module = AnsibleModule(
        argument_spec=argument_specs, supports_check_mode=True)
    if not HAS_REQUESTS:
        return module.fail_json(msg=(
            'Python requests package is not installed. '
            'For installation instructions, visit https://pypi.org/project/requests.'))
    return avi_ansible_api(module, 'siteversion',
                           set())


if __name__ == '__main__':
    main()
