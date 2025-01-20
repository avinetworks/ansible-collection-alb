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
module: avi_pool
author: Gaurav Rastogi (@grastogi23) <grastogi@avinetworks.com>
short_description: Module for setup of Pool Avi RESTful Object
description:
    - This module is used to configure Pool object
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
    analytics_policy:
        description:
            - Determines analytics settings for the pool.
            - Field introduced in 18.1.5, 18.2.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: dict
    analytics_profile_ref:
        description:
            - Specifies settings related to analytics.
            - It is a reference to an object of type analyticsprofile.
            - Field introduced in 18.1.4,18.2.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    append_port:
        description:
            - Allows the option to append port to hostname in the host header while sending a request to the server.
            - By default, port is appended for non-default ports.
            - This setting will apply for pool's 'rewrite host header to server name', 'rewrite host header to sni' features and server's 'rewrite host header'
            - settings as well as http healthmonitors attached to pools.
            - Enum options - NON_DEFAULT_80_443, NEVER, ALWAYS.
            - Field introduced in 21.1.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Allowed in essentials (allowed values- never), basic (allowed values- never) edition.
            - Special default for essentials edition is never, basic edition is never, enterprise edition is non_default_80_443.
            - Default value when not specified in API or module is interpreted by Avi Controller as NON_DEFAULT_80_443.
        type: str
    application_persistence_profile_ref:
        description:
            - Persistence will ensure the same user sticks to the same server for a desired duration of time.
            - It is a reference to an object of type applicationpersistenceprofile.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    autoscale_launch_config_ref:
        description:
            - If configured then avi will trigger orchestration of pool server creation and deletion.
            - It is a reference to an object of type autoscalelaunchconfig.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: str
    autoscale_networks:
        description:
            - Network ids for the launch configuration.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: list
        elements: str
    autoscale_policy_ref:
        description:
            - Reference to server autoscale policy.
            - It is a reference to an object of type serverautoscalepolicy.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: str
    capacity_estimation:
        description:
            - Inline estimation of capacity of servers.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Allowed in essentials (allowed values- false), basic (allowed values- false) edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    capacity_estimation_ttfb_thresh:
        description:
            - The maximum time-to-first-byte of a server.
            - Allowed values are 1-5000.
            - Special values are 0 - automatic.
            - Unit is milliseconds.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Allowed in essentials (allowed values- 0), basic (allowed values- 0) edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 0.
        type: int
    cloud_config_cksum:
        description:
            - Checksum of cloud configuration for pool.
            - Internally set by cloud connector.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    cloud_ref:
        description:
            - It is a reference to an object of type cloud.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    configpb_attributes:
        description:
            - Protobuf versioning for config pbs.
            - Field introduced in 21.1.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: dict
    conn_pool_properties:
        description:
            - Connnection pool properties.
            - Field introduced in 18.2.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: dict
    connection_ramp_duration:
        description:
            - Duration for which new connections will be gradually ramped up to a server recently brought online.
            - Useful for lb algorithms that are least connection based.
            - Allowed values are 1-300.
            - Special values are 0 - immediate.
            - Unit is min.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Allowed in essentials (allowed values- 0), basic (allowed values- 0) edition.
            - Special default for essentials edition is 0, basic edition is 0, enterprise edition is 10.
            - Default value when not specified in API or module is interpreted by Avi Controller as 10.
        type: int
    created_by:
        description:
            - Creator name.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    default_server_port:
        description:
            - Traffic sent to servers will use this destination server port unless overridden by the server's specific port attribute.
            - The ssl checkbox enables avi to server encryption.
            - Allowed values are 1-65535.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 80.
        type: int
    delete_server_on_dns_refresh:
        description:
            - Indicates whether existing ips are disabled(false) or deleted(true) on dns hostname refreshdetail -- on a dns refresh, some ips set on pool may
            - no longer be returned by the resolver.
            - These ips are deleted from the pool when this knob is set to true.
            - They are disabled, if the knob is set to false.
            - Field introduced in 18.2.3.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Allowed in essentials (allowed values- true), basic (allowed values- true) edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as True.
        type: bool
    description:
        description:
            - A description of the pool.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    domain_name:
        description:
            - Comma separated list of domain names which will be used to verify the common names or subject alternative names presented by server certificates.
            - It is performed only when common name check host_check_enabled is enabled.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: list
        elements: str
    east_west:
        description:
            - Inherited config from virtualservice.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: bool
    enable_http2:
        description:
            - Enable http/2 for traffic from virtualservice to all backend servers in this pool.
            - Field introduced in 20.1.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Allowed in essentials (allowed values- false), basic (allowed values- false) edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    enabled:
        description:
            - Enable or disable the pool.
            - Disabling will terminate all open connections and pause health monitors.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as True.
        type: bool
    external_autoscale_groups:
        description:
            - Names of external auto-scale groups for pool servers.
            - Currently available only for aws and azure.
            - Field introduced in 17.1.2.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: list
        elements: str
    fail_action:
        description:
            - Enable an action - close connection, http redirect or local http response - when a pool failure happens.
            - By default, a connection will be closed, in case the pool experiences a failure.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: dict
    fewest_tasks_feedback_delay:
        description:
            - Periodicity of feedback for fewest tasks server selection algorithm.
            - Allowed values are 1-300.
            - Unit is sec.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 10.
        type: int
    graceful_disable_timeout:
        description:
            - Used to gracefully disable a server.
            - Virtual service waits for the specified time before terminating the existing connections  to the servers that are disabled.
            - Allowed values are 1-7200.
            - Special values are 0 - immediate, -1 - infinite.
            - Unit is min.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 1.
        type: int
    graceful_hm_down_disable_timeout:
        description:
            - Time interval for gracefully closing the connections on server, when health monitoring marks the server down.
            - Allowed values are 1-432000.
            - Special values are 0 - immediate, -1 - infinite.
            - Field introduced in 30.2.1.
            - Unit is sec.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as -1.
        type: int
    gslb_sp_enabled:
        description:
            - Indicates if the pool is a site-persistence pool.
            - Field introduced in 17.2.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: bool
    health_monitor_refs:
        description:
            - Verify server health by applying one or more health monitors.
            - Active monitors generate synthetic traffic from each service engine and mark a server up or down based on the response.
            - The passive monitor listens only to client to server communication.
            - It raises or lowers the ratio of traffic destined to a server based on successful responses.
            - It is a reference to an object of type healthmonitor.
            - Maximum of 50 items allowed.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: list
        elements: str
    horizon_profile:
        description:
            - Horizon uag configuration.
            - Field introduced in 21.1.3.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: dict
    host_check_enabled:
        description:
            - Enable common name check for server certificate.
            - If enabled and no explicit domain name is specified, avi will use the incoming host header to do the match.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    http2_properties:
        description:
            - Http2 pool properties.
            - Field introduced in 21.1.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: dict
    ignore_server_port:
        description:
            - Ignore the server port in building the load balancing state.applicable only for consistent hash load balancing algorithm or disable port
            - translation (use_service_port) use cases.
            - Field introduced in 20.1.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    inline_health_monitor:
        description:
            - The passive monitor will monitor client to server connections and requests and adjust traffic load to servers based on successful responses.
            - This may alter the expected behavior of the lb method, such as round robin.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as True.
        type: bool
    ipaddrgroup_ref:
        description:
            - Use list of servers from ip address group.
            - It is a reference to an object of type ipaddrgroup.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    lb_algo_rr_per_se:
        description:
            - Do load balancing at se level instead of the default per core load balancing.
            - Field introduced in 21.1.5, 22.1.3.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    lb_algorithm:
        description:
            - The load balancing algorithm will pick a server within the pool's list of available servers.
            - Values lb_algorithm_nearest_server and lb_algorithm_topology are only allowed for gslb pool.
            - Enum options - LB_ALGORITHM_LEAST_CONNECTIONS, LB_ALGORITHM_ROUND_ROBIN, LB_ALGORITHM_FASTEST_RESPONSE, LB_ALGORITHM_CONSISTENT_HASH,
            - LB_ALGORITHM_LEAST_LOAD, LB_ALGORITHM_FEWEST_SERVERS, LB_ALGORITHM_RANDOM, LB_ALGORITHM_FEWEST_TASKS, LB_ALGORITHM_NEAREST_SERVER,
            - LB_ALGORITHM_CORE_AFFINITY, LB_ALGORITHM_TOPOLOGY.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Allowed in essentials (allowed values- lb_algorithm_least_connections,lb_algorithm_round_robin,lb_algorithm_consistent_hash), basic (allowed
            - values- lb_algorithm_least_connections,lb_algorithm_round_robin,lb_algorithm_consistent_hash) edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as LB_ALGORITHM_LEAST_CONNECTIONS.
        type: str
    lb_algorithm_consistent_hash_hdr:
        description:
            - Http header name to be used for the hash key.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    lb_algorithm_core_nonaffinity:
        description:
            - Degree of non-affinity for core affinity based server selection.
            - Allowed values are 1-65535.
            - Field introduced in 17.1.3.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Allowed in essentials (allowed values- 2), basic (allowed values- 2) edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 2.
        type: int
    lb_algorithm_hash:
        description:
            - Criteria used as a key for determining the hash between the client and  server.
            - Enum options - LB_ALGORITHM_CONSISTENT_HASH_SOURCE_IP_ADDRESS, LB_ALGORITHM_CONSISTENT_HASH_SOURCE_IP_ADDRESS_AND_PORT,
            - LB_ALGORITHM_CONSISTENT_HASH_URI, LB_ALGORITHM_CONSISTENT_HASH_CUSTOM_HEADER, LB_ALGORITHM_CONSISTENT_HASH_CUSTOM_STRING,
            - LB_ALGORITHM_CONSISTENT_HASH_CALLID.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Allowed in essentials (allowed values- lb_algorithm_consistent_hash_source_ip_address), basic (allowed values-
            - lb_algorithm_consistent_hash_source_ip_address) edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as LB_ALGORITHM_CONSISTENT_HASH_SOURCE_IP_ADDRESS.
        type: str
    lookup_server_by_name:
        description:
            - Allow server lookup by name.
            - Field introduced in 17.1.11,17.2.4.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Allowed in essentials (allowed values- false), basic (allowed values- false) edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    markers:
        description:
            - List of labels to be used for granular rbac.
            - Field introduced in 20.1.5.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: list
        elements: dict
    max_concurrent_connections_per_server:
        description:
            - The maximum number of concurrent connections allowed to each server within the pool.
            - Note  applied value will be no less than the number of service engines that the pool is placed on.
            - If set to 0, no limit is applied.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 0.
        type: int
    max_conn_rate_per_server:
        description:
            - Rate limit connections to each server.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: dict
    min_health_monitors_up:
        description:
            - Minimum number of health monitors in up state to mark server up.
            - Field introduced in 18.2.1, 17.2.12.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: int
    min_servers_up:
        description:
            - Minimum number of servers in up state for marking the pool up.
            - Field introduced in 18.2.1, 17.2.12.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: int
    name:
        description:
            - The name of the pool.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        required: true
        type: str
    networks:
        description:
            - (internal-use) networks designated as containing servers for this pool.
            - The servers may be further narrowed down by a filter.
            - This field is used internally by avi, not editable by the user.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: list
        elements: dict
    nsx_securitygroup:
        description:
            - A list of nsx groups where the servers for the pool are created.
            - Field introduced in 17.1.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: list
        elements: str
    pki_profile_ref:
        description:
            - Avi will validate the ssl certificate present by a server against the selected pki profile.
            - It is a reference to an object of type pkiprofile.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    placement_networks:
        description:
            - Manually select the networks and subnets used to provide reachability to the pool's servers.
            - Specify the subnet using the following syntax  10-1-1-0/24.
            - Use static routes in vrf configuration when pool servers are not directly connected but routable from the service engine.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: list
        elements: dict
    pool_type:
        description:
            - Type or purpose, the pool is to be used for.
            - Enum options - POOL_TYPE_GENERIC_APP, POOL_TYPE_OAUTH.
            - Field introduced in 22.1.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as POOL_TYPE_GENERIC_APP.
        type: str
    request_queue_depth:
        description:
            - Minimum number of requests to be queued when pool is full.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Allowed in essentials (allowed values- 128), basic (allowed values- 128) edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 128.
        type: int
    request_queue_enabled:
        description:
            - Enable request queue when pool is full.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Allowed in essentials (allowed values- false), basic (allowed values- false) edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    resolve_pool_by_dns:
        description:
            - This field is used as a flag to create a job for jobmanager.
            - Field introduced in 18.2.10,20.1.2.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    rewrite_host_header_to_server_name:
        description:
            - Rewrite incoming host header to server name of the server to which the request is proxied.
            - Enabling this feature rewrites host header for requests to all servers in the pool.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    rewrite_host_header_to_sni:
        description:
            - If sni server name is specified, rewrite incoming host header to the sni server name.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    routing_pool:
        description:
            - Enable to do routing when this pool is selected to send traffic.
            - No servers present in routing pool.
            - Field introduced in 20.1.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    server_disable_type:
        description:
            - Server graceful disable timeout behaviour.
            - Enum options - DISALLOW_NEW_CONNECTION, ALLOW_NEW_CONNECTION_IF_PERSISTENCE_PRESENT.
            - Field introduced in 21.1.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as DISALLOW_NEW_CONNECTION.
        type: str
    server_name:
        description:
            - Fully qualified dns hostname which will be used in the tls sni extension in server connections if sni is enabled.
            - If no value is specified, avi will use the incoming host header instead.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    server_reselect:
        description:
            - Server reselect configuration for http requests.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: dict
    server_timeout:
        description:
            - Server timeout value specifies the time within which a server connection needs to be established and a request-response exchange completes
            - between avi and the server.
            - Value of 0 results in using default timeout of 60 minutes.
            - Allowed values are 0-21600000.
            - Field introduced in 18.1.5,18.2.1.
            - Unit is milliseconds.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 0.
        type: int
    servers:
        description:
            - The pool directs load balanced traffic to this list of destination servers.
            - The servers can be configured by ip address, name, network or via ip address group.
            - Maximum of 5000 items allowed.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: list
        elements: dict
    service_metadata:
        description:
            - Metadata pertaining to the service provided by this pool.
            - In openshift/kubernetes environments, app metadata info is stored.
            - Any user input to this field will be overwritten by avi vantage.
            - Field introduced in 17.2.14,18.1.5,18.2.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    sni_enabled:
        description:
            - Enable tls sni for server connections.
            - If disabled, avi will not send the sni extension as part of the handshake.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as True.
        type: bool
    sp_gs_info:
        description:
            - Gslb service associated with the site persistence pool.
            - Field introduced in 22.1.3.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: dict
    ssl_key_and_certificate_ref:
        description:
            - Service engines will present a client ssl certificate to the server.
            - It is a reference to an object of type sslkeyandcertificate.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    ssl_profile_ref:
        description:
            - When enabled, avi re-encrypts traffic to the backend servers.
            - The specific ssl profile defines which ciphers and ssl versions will be supported.
            - It is a reference to an object of type sslprofile.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    tenant_ref:
        description:
            - It is a reference to an object of type tenant.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    tier1_lr:
        description:
            - This tier1_lr field should be set same as virtualservice associated for nsx-t.
            - Field introduced in 20.1.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    url:
        description:
            - Avi controller URL of the object.
        type: str
    use_service_port:
        description:
            - Do not translate the client's destination port when sending the connection to the server.
            - Monitor port needs to be specified for health monitors.
            - Allowed with any value in enterprise, basic, enterprise with cloud services edition.
            - Allowed in essentials (allowed values- false) edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    use_service_ssl_mode:
        description:
            - This applies only when use_service_port is set to true.
            - If enabled, ssl mode of the connection to the server is decided by the ssl mode on the virtualservice service port, on which the request was
            - received.
            - Field introduced in 21.1.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    uuid:
        description:
            - Uuid of the pool.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    vrf_ref:
        description:
            - Virtual routing context that the pool is bound to.
            - This is used to provide the isolation of the set of networks the pool is attached to.
            - The pool inherits the virtual routing context of the virtual service, and this field is used only internally, and is set by pb-transform.
            - It is a reference to an object of type vrfcontext.
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

- name: Create a Pool with two servers and HTTP monitor
  vmware.alb.avi_pool:
    avi_credentials: "{{ avi_credentials }}"
    name: testpool1
    description: testpool1
    state: present
    health_monitor_refs:
        - '/api/healthmonitor?name=System-HTTP'
    servers:
        - ip:
            addr: 192.168.138.11
            type: V4
        - ip:
            addr: 192.168.138.12
            type: V4

- name: Patch pool with a single server using patch op and avi_credentials
  vmware.alb.avi_pool:
    avi_credentials: "{{ avi_credentials }}"
    avi_api_update_method: patch
    avi_api_patch_op: delete
    name: test-pool
    servers:
      - ip:
        addr: 192.168.138.13
        type: 'V4'
  register: pool
  when:
    - state | default("present") == "present"
"""

RETURN = '''
obj:
    description: Pool (api/pool) object
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
        analytics_policy=dict(type='dict',),
        analytics_profile_ref=dict(type='str',),
        append_port=dict(type='str',),
        application_persistence_profile_ref=dict(type='str',),
        autoscale_launch_config_ref=dict(type='str',),
        autoscale_networks=dict(type='list', elements='str',),
        autoscale_policy_ref=dict(type='str',),
        capacity_estimation=dict(type='bool',),
        capacity_estimation_ttfb_thresh=dict(type='int',),
        cloud_config_cksum=dict(type='str',),
        cloud_ref=dict(type='str',),
        configpb_attributes=dict(type='dict',),
        conn_pool_properties=dict(type='dict',),
        connection_ramp_duration=dict(type='int',),
        created_by=dict(type='str',),
        default_server_port=dict(type='int',),
        delete_server_on_dns_refresh=dict(type='bool',),
        description=dict(type='str',),
        domain_name=dict(type='list', elements='str',),
        east_west=dict(type='bool',),
        enable_http2=dict(type='bool',),
        enabled=dict(type='bool',),
        external_autoscale_groups=dict(type='list', elements='str',),
        fail_action=dict(type='dict',),
        fewest_tasks_feedback_delay=dict(type='int',),
        graceful_disable_timeout=dict(type='int',),
        graceful_hm_down_disable_timeout=dict(type='int',),
        gslb_sp_enabled=dict(type='bool',),
        health_monitor_refs=dict(type='list', elements='str',),
        horizon_profile=dict(type='dict',),
        host_check_enabled=dict(type='bool',),
        http2_properties=dict(type='dict',),
        ignore_server_port=dict(type='bool',),
        inline_health_monitor=dict(type='bool',),
        ipaddrgroup_ref=dict(type='str',),
        lb_algo_rr_per_se=dict(type='bool',),
        lb_algorithm=dict(type='str',),
        lb_algorithm_consistent_hash_hdr=dict(type='str',),
        lb_algorithm_core_nonaffinity=dict(type='int',),
        lb_algorithm_hash=dict(type='str',),
        lookup_server_by_name=dict(type='bool',),
        markers=dict(type='list', elements='dict',),
        max_concurrent_connections_per_server=dict(type='int',),
        max_conn_rate_per_server=dict(type='dict',),
        min_health_monitors_up=dict(type='int',),
        min_servers_up=dict(type='int',),
        name=dict(type='str', required=True),
        networks=dict(type='list', elements='dict',),
        nsx_securitygroup=dict(type='list', elements='str',),
        pki_profile_ref=dict(type='str',),
        placement_networks=dict(type='list', elements='dict',),
        pool_type=dict(type='str',),
        request_queue_depth=dict(type='int',),
        request_queue_enabled=dict(type='bool',),
        resolve_pool_by_dns=dict(type='bool',),
        rewrite_host_header_to_server_name=dict(type='bool',),
        rewrite_host_header_to_sni=dict(type='bool',),
        routing_pool=dict(type='bool',),
        server_disable_type=dict(type='str',),
        server_name=dict(type='str',),
        server_reselect=dict(type='dict',),
        server_timeout=dict(type='int',),
        servers=dict(type='list', elements='dict',),
        service_metadata=dict(type='str',),
        sni_enabled=dict(type='bool',),
        sp_gs_info=dict(type='dict',),
        ssl_key_and_certificate_ref=dict(type='str',),
        ssl_profile_ref=dict(type='str',),
        tenant_ref=dict(type='str',),
        tier1_lr=dict(type='str',),
        url=dict(type='str',),
        use_service_port=dict(type='bool',),
        use_service_ssl_mode=dict(type='bool',),
        uuid=dict(type='str',),
        vrf_ref=dict(type='str',),
    )
    argument_specs.update(avi_common_argument_spec())
    module = AnsibleModule(
        argument_spec=argument_specs, supports_check_mode=True)
    if not HAS_REQUESTS:
        return module.fail_json(msg=(
            'Python requests package is not installed. '
            'For installation instructions, visit https://pypi.org/project/requests.'))
    return avi_ansible_api(module, 'pool',
                           set())


if __name__ == '__main__':
    main()
