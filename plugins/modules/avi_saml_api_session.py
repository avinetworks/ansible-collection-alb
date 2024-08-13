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
module: avi_saml_api_session
author: Shrikant Chaudhari (@gitshrikant) <shrikant.chaudhari@avinetworks.com>
short_description: Avi API Module
description:
    - This module is useful to get SAML session after successful SAML authentication from a given IDP.
    - This module return api_context and token after successful authentication from IDP.
options:
    idp_class:
        description:
            - IDP class which will be used to authenticate session with that corresponding IDP such as Okta,
            - Onelogin and Pingfederate. Currently, we support two idp classes OktaSAMLApiSession, OneloginSAMLApiSession.
        required: true
        type: str
extends_documentation_fragment:
    - vmware.alb.avi
'''

EXAMPLES = '''
  - hosts: all
    vars:
      avi_credentials:
        username: "{{ username }}"
        password: "{{ password }}"
        controller: "{{ controller }}"
        api_version: "{{ api_version }}"
      idp_class: "{{ idp_class }}"

  - name: Get SAML Session
    vmware.alb.avi_saml_api_session:
      idp_class: "{{ idp_class }}"
      avi_credentials: "{{ avi_credentials }}"
    register: saml_api_session

  - set_fact:
      saml_api_context: "{{ saml_api_session.ansible_facts.avi_api_context }}"

  - name: Create Pool
    vmware.alb.avi_pool:
      api_context: "{{ saml_api_context | default(omit) }}"
      avi_credentials: "{{ avi_credentials }}"
      state: "{{ state | default(present) }}"
      name: vs-simple-pool
      lb_algorithm: LB_ALGORITHM_ROUND_ROBIN
      servers:
      - ip:
          addr: 10.90.64.12
          type: 'V4'
      - ip:
          addr: 10.90.64.11
          type: 'V4'
      - ip:
          addr: 10.90.64.13
          type: 'V4'

  - name: Create Virtual Service
    vmware.alb.avi_virtualservice:
      api_context: "{{ saml_api_context | default(omit) }}"
      avi_credentials: "{{ avi_credentials }}"
      state: "{{ state | default(present) }}"
      name: vs-simple
      services:
      - port: 80
      pool_ref: '/api/pool?name=vs-simple-pool'
      vip:
      - ip_address:
          addr: 10.90.64.244
          type: 'V4'
        vip_id: '1'
'''


RETURN = '''
obj:
    description: Avi REST resource
    returned: success, changed
    type: dict
'''

from ansible.module_utils.basic import AnsibleModule
try:
    from ansible_collections.vmware.alb.plugins.module_utils.utils.ansible_utils import (
        avi_common_argument_spec, ansible_return, avi_obj_cmp,
        cleanup_absent_fields)
    from ansible_collections.vmware.alb.plugins.module_utils.avi_api import (
        ApiSession, AviCredentials)
    from pkg_resources import parse_version
    from requests import ConnectionError
    from ssl import SSLError
    from requests.exceptions import ChunkedEncodingError
    from ansible_collections.vmware.alb.plugins.module_utils.saml_avi_api import OktaSAMLApiSession, OneloginSAMLApiSession
    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False


def get_idp_class(idp):
    """
    This return corresponding idp class.
    :param idp: idp type such as okta, onelogin, pingfed
    :return: IDP class or ApiSession class
    """

    if str(idp).lower() == "oktasamlapisession":
        idp_class = OktaSAMLApiSession
    elif str(idp).lower() == 'oneloginsamlapisession':
        idp_class = OneloginSAMLApiSession
    else:
        idp_class = None
    return idp_class


def main():
    argument_specs = dict(
        idp_class=dict(type=str, required=True, ),
    )
    argument_specs.update(avi_common_argument_spec())
    module = AnsibleModule(argument_spec=argument_specs)

    if not HAS_REQUESTS:
        return module.fail_json(msg=(
            'Python requests package is not installed. '
            'For installation instructions, visit https://pypi.org/project/requests.'))
    idp_class = module.params.get("idp_class", None)
    idp = get_idp_class(idp_class)
    if not idp:
        msg = "IDP {1} not supported yet.".format(idp_class)
        return module.fail_json(msg=msg)
    avi_credentials = AviCredentials()
    avi_credentials.update_from_ansible_module(module)
    try:
        api = ApiSession.get_session(
            avi_credentials.controller, avi_credentials.username, password=avi_credentials.password,
            timeout=avi_credentials.timeout, tenant=avi_credentials.tenant,
            tenant_uuid=avi_credentials.tenant_uuid, port=avi_credentials.port, idp_class=idp)
        changed = True
    except (ConnectionError, SSLError, ChunkedEncodingError) as e:
        msg = "Error during get session {1}".format(e.message)
        return module.fail_json(msg=msg)
    return ansible_return(module, None, changed, None, api_context=api.get_context())


if __name__ == '__main__':
    main()
