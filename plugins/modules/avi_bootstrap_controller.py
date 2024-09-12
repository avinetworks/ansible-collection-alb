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
module: avi_bootstrap_controller
author: Shrikant Chaudhari (@gitshrikant) <shrikant.chaudhari@avinetworks.com>
short_description: avi bootstrap controller module.
description:
    - This module can be used for initializing the password of a user.
    - This module is useful for setting up admin password for Controller bootstrap.
options:
    password:
        description:
            - New password to initialize controller password.
        required: true
        type: str
    ssh_key_pair:
        description:
            - AWS/Azure ssh key pair to login on the controller instance.
        required: true
        type: str
    force_mode:
        description:
            - Avoid check for login with given password and re-initialise controller
              with given password even if controller password is initialised before
        type: bool
        default: false
    con_wait_time:
        description:
            - Wait for controller to come up for given con_wait_time.
        default: 3600
        type: int
    round_wait:
        description:
            - Wait for controller to come up for given round_wait.
        default: 10
        type: int
extends_documentation_fragment:
    - vmware.alb.avi
'''

EXAMPLES = '''
  - name: Initialize user password
    vmware.alb.avi_bootstrap_controller:
      avi_credentials:
        username: "{{ username }}"
        password: "{{ password }}"
        controller: "{{ controller }}"
        api_version: "{{ api_version }}"
      ssh_key_pair: "/path/to/key-pair-file.pem"
      password: new_password
      con_wait_time: 3600
      round_wait: 10
'''

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
        avi_common_argument_spec, ansible_return, avi_obj_cmp,
        cleanup_absent_fields)
    from ansible_collections.vmware.alb.plugins.module_utils.avi_api import (
        ApiSession, AviCredentials)

    from pkg_resources import parse_version
    import subprocess
    import requests
    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False


def controller_wait(controller_ip, port=None, round_wait=10, wait_time=3600):
    """
    It waits for controller to come up for a given wait_time (default 1 hour).
    :return: controller_up: Boolean value for controller up state.
    """
    count = 0
    max_count = wait_time / round_wait
    ctrl_port = port if port else 80
    path = "http://{1}:{2}{3}".format(controller_ip, ctrl_port, "/api/cluster/runtime")
    ctrl_status = False
    while True:
        if count >= max_count:
            break
        try:
            r = requests.get(path, timeout=10, verify=False)
            # Check for controller response for login URI.
            if r.json()['cluster_state']['state'] == 'CLUSTER_UP_NO_HA':
                ctrl_status = True
                break
        except Exception as e:
            pass
        time.sleep(round_wait)
        count += 1
    return ctrl_status


def main():
    argument_specs = dict(
        password=dict(type='str', required=True, no_log=True),
        ssh_key_pair=dict(type='str', required=True),
        force_mode=dict(type='bool', default=False),
        # Max time to wait for controller up state
        con_wait_time=dict(type='int', default=3600),
        # Retry after every rount_wait time to check for controller state.
        round_wait=dict(type='int', default=10),
    )
    argument_specs.update(avi_common_argument_spec())
    module = AnsibleModule(argument_spec=argument_specs)
    if not HAS_REQUESTS:
        return module.fail_json(msg=(
            'Python requests package is not installed. '
            'For installation instructions, visit https://pypi.org/project/requests.'))
    api_creds = AviCredentials()
    api_creds.update_from_ansible_module(module)
    new_password = module.params.get('password')
    key_pair = module.params.get('ssh_key_pair')
    force_mode = module.params.get('force_mode')
    # Wait for controller to come up for given con_wait_time
    controller_up = controller_wait(api_creds.controller, api_creds.port, module.params['round_wait'],
                                    module.params['con_wait_time'])
    if not controller_up:
        return module.fail_json(
            msg='Something wrong with the controller. The Controller is not in the up state.')
    if not force_mode:
        # Check for admin login with new password before initializing controller password.
        try:
            ApiSession.get_session(
                api_creds.controller, "admin",
                password=new_password, timeout=api_creds.timeout,
                tenant=api_creds.tenant, tenant_uuid=api_creds.tenant_uuid,
                token=api_creds.token, port=api_creds.port)
            module.exit_json(msg="Already initialized controller password with a given password.", changed=False)
        except Exception as e:
            pass
    cmd = "ssh -o \"StrictHostKeyChecking no\" -t -i " + key_pair + " admin@" + \
          api_creds.controller + " \"ls /opt/avi/scripts/initialize_admin_user.py && echo -e '" + \
          api_creds.controller + "\\n" + new_password + "' | sudo /opt/avi/scripts/initialize_admin_user.py\""
    process = subprocess.Popen(cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
    stdout, stderr = process.communicate()
    cmd_status = process.returncode
    if cmd_status == 0:
        return module.exit_json(changed=True, msg="Successfully initialized controller with new password. "
                                "return_code: %s output: %s error: %s" % (cmd_status, stdout, stderr))
    else:
        return module.fail_json(msg='Fail to initialize password for controllers return_code: %s '
                                'output: %s error: %s' % (cmd_status, stdout, stderr))


if __name__ == '__main__':
    main()
