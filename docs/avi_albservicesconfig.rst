.. vmware.alb.avi_albservicesconfig:


**********************************************
vmware.alb.avi_albservicesconfig
**********************************************

**Module for setup of ALBServicesConfig Avi RESTful Object**


.. contents::
   :local:
   :depth: 1


Synopsis
--------
- This module is used to configure ALBServicesConfig object.
- More examples at (https://github.com/avinetworks/devops).


Parameters
----------

.. raw:: html

    <table  border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="2">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
            <th width="100%">Comments</th>
        </tr>
        <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>state</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                <ul style="margin: 0; padding: 0">
                    <li>absent</li>
                    <li><div style="color: blue"><b>present</b>&nbsp;&larr;</div></li>
                </ul>
            </td>
            <td>
                <div style="font-size: small">
                    - The state that should be applied on the entity.
                </div>
            </td>
        </tr>
        <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>avi_api_update_method</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                <ul style="margin: 0; padding: 0">
                    <li><div style="color: blue"><b>put</b>&nbsp;&larr;</div></li>
                    <li>patch</li>
                </ul>
            </td>
            <td>
                <div style="font-size: small">
                    - Default method for object update is HTTP PUT.
                </div>
                <div style="font-size: small">
                    - Setting to patch will override that behavior to use HTTP PATCH.
                </div>
            </td>
        </tr>
        <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>avi_api_patch_op</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                <ul style="margin: 0; padding: 0">
                    <li><div style="color: blue"><b>add</b>&nbsp;&larr;</div></li>
                    <li>replace</li>
                    <li>delete</li>
                    <li>remove</li>
                </ul>
            </td>
            <td>
                <div style="font-size: small">
                    - Patch operation to use when using avi_api_update_method as patch.
                </div>
            </td>
        </tr>
        <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>avi_patch_path</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td></td>
            <td>
                <div style="font-size: small">
                    - Patch path to use when using avi_api_update_method as patch.
                </div>
            </td>
        </tr>
        <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>avi_patch_value</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td></td>
            <td>
                <div style="font-size: small">
                    - Patch value to use when using avi_api_update_method as patch.
                </div>
            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>app_signature_config</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">dict</span>
                </div>
            </td>
            <td>
                                <div style="font-size: small">
                <b>required: true</b>
                </div>
                            </td>
            <td>
                                                <div style="font-size: small">
                  - Default values for application signature sync.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 20.1.4.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>asset_contact</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">dict</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Default contact for this controller cluster.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 20.1.1.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>case_config</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">dict</span>
                </div>
            </td>
            <td>
                                <div style="font-size: small">
                <b>required: true</b>
                </div>
                            </td>
            <td>
                                                <div style="font-size: small">
                  - Default values for case management.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 21.1.1.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>configpb_attributes</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">dict</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Protobuf versioning for config pbs.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 21.1.1.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>feature_opt_in_status</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">dict</span>
                </div>
            </td>
            <td>
                                <div style="font-size: small">
                <b>required: true</b>
                </div>
                            </td>
            <td>
                                                <div style="font-size: small">
                  - Features opt-in for pulse cloud services.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 20.1.1.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>inventory_config</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">dict</span>
                </div>
            </td>
            <td>
                                <div style="font-size: small">
                <b>required: true</b>
                </div>
                            </td>
            <td>
                                                <div style="font-size: small">
                  - Inventory configurations for pulse cloud services.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 30.2.1.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>ip_reputation_config</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">dict</span>
                </div>
            </td>
            <td>
                                <div style="font-size: small">
                <b>required: true</b>
                </div>
                            </td>
            <td>
                                                <div style="font-size: small">
                  - Default values to be used for ip reputation sync.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 20.1.1.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>mode</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Mode helps log collection and upload.
                </div>
                                <div style="font-size: small">
                  - Enum options - MODE_UNKNOWN, SALESFORCE, SYSTEST, MYVMWARE, BROADCOM.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 20.1.2.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, enterprise with cloud services edition.
                </div>
                                <div style="font-size: small">
                  - Allowed in essentials (allowed values- salesforce,myvmware,systest), basic (allowed values- salesforce,myvmware,systest) edition.
                </div>
                                <div style="font-size: small">
                  - Default value when not specified in API or module is interpreted by Avi Controller as MYVMWARE.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>name</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Name of the albservicesconfig object.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 30.1.1.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>polling_interval</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">int</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Time interval in minutes.
                </div>
                                <div style="font-size: small">
                  - Allowed values are 5-60.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 18.2.6.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                <div style="font-size: small">
                  - Default value when not specified in API or module is interpreted by Avi Controller as 10.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>portal_url</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                                <div style="font-size: small">
                <b>required: true</b>
                </div>
                            </td>
            <td>
                                                <div style="font-size: small">
                  - The fqdn or ip address of the pulse cloud services.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 18.2.6.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>saas_licensing_config</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">dict</span>
                </div>
            </td>
            <td>
                                <div style="font-size: small">
                <b>required: true</b>
                </div>
                            </td>
            <td>
                                                <div style="font-size: small">
                  - Saas licensing configuration.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 21.1.3.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>session_config</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">dict</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Session configuration data.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 30.2.1.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>split_proxy_configuration</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">dict</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Split proxy configuration to connect external pulse cloud services.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 20.1.1.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>tenant_config</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">dict</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Tenant based configuration data.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 30.2.1.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>tenant_ref</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Tenant uuid associated with the object.
                </div>
                                <div style="font-size: small">
                  - It is a reference to an object of type tenant.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 30.1.1.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>url</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Avi controller URL of the object.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>use_split_proxy</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - By default, pulse cloud services uses proxy added in system configuration.
                </div>
                                <div style="font-size: small">
                  - If it should use a separate proxy, set this flag to true and configure split proxy configuration.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 20.1.1.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                <div style="font-size: small">
                  - Default value when not specified in API or module is interpreted by Avi Controller as False.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>use_tls</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">bool</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Secure the controller to pulse cloud services communication over tls.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 20.1.3.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, basic, enterprise with cloud services edition.
                </div>
                                <div style="font-size: small">
                  - Default value when not specified in API or module is interpreted by Avi Controller as True.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>user_agent_db_config</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">dict</span>
                </div>
            </td>
            <td>
                                <div style="font-size: small">
                <b>required: true</b>
                </div>
                            </td>
            <td>
                                                <div style="font-size: small">
                  - Default values for user agent db service.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 21.1.1.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>uuid</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">str</span>
                </div>
            </td>
            <td>
                                                            </td>
            <td>
                                                <div style="font-size: small">
                  - Field introduced in 18.2.6.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
                </div>
                                            </td>
        </tr>
                <tr>
            <td colspan="2">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>waf_config</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">dict</span>
                </div>
            </td>
            <td>
                                <div style="font-size: small">
                <b>required: true</b>
                </div>
                            </td>
            <td>
                                                <div style="font-size: small">
                  - Default values for waf management.
                </div>
                                <div style="font-size: small">
                  - Field introduced in 21.1.1.
                </div>
                                <div style="font-size: small">
                  - Allowed with any value in essentials, basic, enterprise, enterprise with cloud services edition.
                </div>
                                            </td>
        </tr>
            </table>
    <br/>


Examples
--------

.. code-block:: yaml

    - hosts: localhost
      connection: local
      collections:
        - vmware.alb
      vars:
        avi_credentials:
          username: "avi_user"
          password: "avi_password"
          controller: "192.168.138.18"
          api_version: "21.1.1"
      tasks:
        - name: Example to create ALBServicesConfig object
          avi_albservicesconfig:
            avi_credentials: "{{ avi_credentials }}"
            state: present
            name: sample_albservicesconfig


Authors
~~~~~~~
- Gaurav Rastogi (grastogi@vmware.com)
- Sandeep Bandi (sbandi@vmware.com)
- Amol Shinde (samol@vmware.com)



