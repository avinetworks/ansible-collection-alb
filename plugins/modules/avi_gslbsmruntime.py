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
module: avi_gslbsmruntime
author: Gaurav Rastogi (@grastogi23) <grastogi@avinetworks.com>
short_description: Module for setup of GslbSMRuntime Avi RESTful Object
description:
    - This module is used to configure GslbSMRuntime object
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
    cluster_leader:
        description:
            - The controller cluster leader node uuid.
            - Field introduced in 31.1.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: str
    cluster_uuid:
        description:
            - The site controller cluster uuid.
            - Field introduced in 31.1.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: str
    dns_configs:
        description:
            - Sub domain configuration for the gslb.
            - Gslb service's fqdn must be a match one of these subdomains.
            - Field introduced in 31.1.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: list
        elements: dict
    dns_info:
        description:
            - Dns info at the site.
            - Field introduced in 31.1.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: dict
    enabled:
        description:
            - Activate/de-activate state retrieved from the cfg.
            - Field introduced in 31.1.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: bool
    events:
        description:
            - Captures sm related events.
            - Field introduced in 31.1.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: list
        elements: dict
    health_monitor_info:
        description:
            - This field will provide information on origin(site name) of the health monitoring information.
            - Field introduced in 31.1.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: str
    leader_cluster_uuid:
        description:
            - Mark this site as leader of gslb configuration.
            - This site is the one among the avi sites.
            - Field introduced in 31.1.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        required: true
        type: str
    member_type:
        description:
            - The site's member type  a leader is set to active while all members are set to passive.
            - Enum options - GSLB_ACTIVE_MEMBER, GSLB_PASSIVE_MEMBER.
            - Field introduced in 31.1.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as GSLB_PASSIVE_MEMBER.
        type: str
    name:
        description:
            - The name of db entry.
            - Field introduced in 31.1.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: str
    node_uuid:
        description:
            - The controller cluster node uuid that processes the site.sites are sharded across the cluster nodes.
            - Field introduced in 31.1.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: str
    num_of_retries:
        description:
            - Number of retry attempts to reach the remote site.
            - Field introduced in 31.1.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 0.
        type: int
    obj_state:
        description:
            - Represents the state of the site.
            - Enum options - SITE_STATE_NULL, SITE_STATE_JOIN_IN_PROGRESS, SITE_STATE_LEAVE_IN_PROGRESS, SITE_STATE_INIT, SITE_STATE_UNREACHABLE,
            - SITE_STATE_MMODE, SITE_STATE_DISABLE_IN_PROGRESS, SITE_STATE_DISABLED, SITE_STATE_HS_IN_PROGRESS.
            - Field introduced in 31.1.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as SITE_STATE_NULL.
        type: str
    obj_uuid:
        description:
            - Gslb sm runtime object uuid.
            - Points to the gslb to which this belongs.
            - Field introduced in 31.1.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: str
    oper_status:
        description:
            - Gslb site operational status, represents whether site is up or down.
            - Field introduced in 31.1.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: dict
    remote_info:
        description:
            - Remote info is basically updated by grw.
            - Field introduced in 31.1.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: dict
    role:
        description:
            - Site role  leader or follower.
            - Enum options - GSLB_LEADER, GSLB_MEMBER, GSLB_NOT_A_MEMBER.
            - Field introduced in 31.1.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as GSLB_NOT_A_MEMBER.
        type: str
    site_name:
        description:
            - The gslb site name.
            - Field introduced in 31.1.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: str
    site_type:
        description:
            - Indicates if it is avi site or third-party.
            - Enum options - GSLB_AVI_SITE, GSLB_THIRD_PARTY_SITE.
            - Field introduced in 31.1.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: str
    sw_version:
        description:
            - Current software version of the site.
            - Field introduced in 31.1.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as Not-Initialized.
        type: str
    tenant_ref:
        description:
            - Uuid of the tenant.
            - It is a reference to an object of type tenant.
            - Field introduced in 31.1.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: str
    url:
        description:
            - Avi controller URL of the object.
        type: str
    uuid:
        description:
            - The uuid of db entry.
            - Field introduced in 31.1.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: str
    view_id:
        description:
            - The view-id is used in change-leader mode to differentiate partitioned groups while they have the same gslb namespace.
            - Each partitioned group will be able to operate independently by using the view-id.
            - Field introduced in 31.1.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 0.
        type: int
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

- name: Example to create GslbSMRuntime object
  vmware.alb.avi_gslbsmruntime:
    avi_credentials: "{{ avi_credentials }}"
    state: present
    name: sample_gslbsmruntime
"""

RETURN = '''
obj:
    description: GslbSMRuntime (api/gslbsmruntime) object
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
        cluster_leader=dict(type='str',),
        cluster_uuid=dict(type='str',),
        dns_configs=dict(type='list', elements='dict',),
        dns_info=dict(type='dict',),
        enabled=dict(type='bool',),
        events=dict(type='list', elements='dict',),
        health_monitor_info=dict(type='str',),
        leader_cluster_uuid=dict(type='str', required=True),
        member_type=dict(type='str',),
        name=dict(type='str',),
        node_uuid=dict(type='str',),
        num_of_retries=dict(type='int',),
        obj_state=dict(type='str',),
        obj_uuid=dict(type='str',),
        oper_status=dict(type='dict',),
        remote_info=dict(type='dict',),
        role=dict(type='str',),
        site_name=dict(type='str',),
        site_type=dict(type='str',),
        sw_version=dict(type='str',),
        tenant_ref=dict(type='str',),
        url=dict(type='str',),
        uuid=dict(type='str',),
        view_id=dict(type='int',),
    )
    argument_specs.update(avi_common_argument_spec())
    module = AnsibleModule(
        argument_spec=argument_specs, supports_check_mode=True)
    if not HAS_REQUESTS:
        return module.fail_json(msg=(
            'Python requests package is not installed. '
            'For installation instructions, visit https://pypi.org/project/requests.'))
    return avi_ansible_api(module, 'gslbsmruntime',
                           set())


if __name__ == '__main__':
    main()
