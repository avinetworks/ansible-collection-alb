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
module: avi_alertconfig
author: Gaurav Rastogi (@grastogi23) <grastogi@avinetworks.com>
short_description: Module for setup of AlertConfig Avi RESTful Object
description:
    - This module is used to configure AlertConfig object
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
    action_group_ref:
        description:
            - The alert config will trigger the selected alert action, which can send notifications and execute a controlscript.
            - It is a reference to an object of type actiongroupconfig.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: str
    alert_rule:
        description:
            - List of filters matching on events or client logs used for triggering alerts.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        required: true
        type: dict
    autoscale_alert:
        description:
            - This alert config applies to auto scale alerts.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: bool
    category:
        description:
            - Determines whether an alert is raised immediately when event occurs (realtime) or after specified number of events occurs within rolling time
            - window.
            - Enum options - REALTIME, ROLLINGWINDOW, WATERMARK.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as REALTIME.
        required: true
        type: str
    configpb_attributes:
        description:
            - Protobuf versioning for config pbs.
            - Field introduced in 21.1.1.
            - Allowed in enterprise edition with any value, essentials edition with any value, basic edition with any value, enterprise with cloud services
            - edition.
        type: dict
    description:
        description:
            - A custom description field.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: str
    enabled:
        description:
            - Enable or disable this alert config from generating new alerts.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as True.
        type: bool
    expiry_time:
        description:
            - An alert is expired and deleted after the expiry time has elapsed.
            - The original event triggering the alert remains in the event's log.
            - Allowed values are 1-31536000.
            - Unit is sec.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 86400.
        type: int
    name:
        description:
            - Name of the alert configuration.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        required: true
        type: str
    obj_uuid:
        description:
            - Instance of the resource for which alert was raised.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: str
    object_type:
        description:
            - The object type to which the alert config is associated with.
            - Valid object types are - virtual service, pool, service engine.
            - Enum options - VIRTUALSERVICE, POOL, HEALTHMONITOR, NETWORKPROFILE, APPLICATIONPROFILE, HTTPPOLICYSET, DNSPOLICY, SECURITYPOLICY, IPADDRGROUP,
            - STRINGGROUP, SSLPROFILE, SSLKEYANDCERTIFICATE, NETWORKSECURITYPOLICY, APPLICATIONPERSISTENCEPROFILE, ANALYTICSPROFILE, VSDATASCRIPTSET, TENANT,
            - PKIPROFILE, AUTHPROFILE, CLOUD...
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: str
    recommendation:
        description:
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: str
    rolling_window:
        description:
            - Only if the number of events is reached or exceeded within the time window will an alert be generated.
            - Allowed values are 1-31536000.
            - Unit is sec.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 300.
        type: int
    source:
        description:
            - Signifies system events or the type of client logsused in this alert configuration.
            - Enum options - CONN_LOGS, APP_LOGS, EVENT_LOGS, METRICS.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        required: true
        type: str
    summary:
        description:
            - Summary of reason why alert is generated.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: str
    tenant_ref:
        description:
            - It is a reference to an object of type tenant.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: str
    threshold:
        description:
            - An alert is created only when the number of events meets or exceeds this number within the chosen time frame.
            - Allowed values are 1-65536.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 1.
        type: int
    throttle:
        description:
            - Alerts are suppressed (throttled) for this duration of time since the last alert was raised for this alert config.
            - Allowed values are 0-31536000.
            - Unit is sec.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 600.
        type: int
    url:
        description:
            - Avi controller URL of the object.
        type: str
    uuid:
        description:
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

- name: Example to create AlertConfig object
  vmware.alb.avi_alertconfig:
    avi_credentials: "{{ avi_credentials }}"
    state: present
    name: sample_alertconfig
"""

RETURN = '''
obj:
    description: AlertConfig (api/alertconfig) object
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
        action_group_ref=dict(type='str',),
        alert_rule=dict(type='dict', required=True),
        autoscale_alert=dict(type='bool',),
        category=dict(type='str', required=True),
        configpb_attributes=dict(type='dict',),
        description=dict(type='str',),
        enabled=dict(type='bool',),
        expiry_time=dict(type='int',),
        name=dict(type='str', required=True),
        obj_uuid=dict(type='str',),
        object_type=dict(type='str',),
        recommendation=dict(type='str',),
        rolling_window=dict(type='int',),
        source=dict(type='str', required=True),
        summary=dict(type='str',),
        tenant_ref=dict(type='str',),
        threshold=dict(type='int',),
        throttle=dict(type='int',),
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
    return avi_ansible_api(module, 'alertconfig',
                           set())


if __name__ == '__main__':
    main()
