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
module: avi_virtualservice
author: Gaurav Rastogi (@grastogi23) <grastogi@avinetworks.com>
short_description: Module for setup of VirtualService Avi RESTful Object
description:
    - This module is used to configure VirtualService object
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
    active_standby_se_tag:
        description:
            - This configuration only applies if the virtualservice is in legacy active standby ha mode and load distribution among active standby is enabled.
            - This field is used to tag the virtualservice so that virtualservices with the same tag will share the same active serviceengine.
            - Virtualservices with different tags will have different active serviceengines.
            - If one of the serviceengine's in the serviceenginegroup fails, all virtualservices will end up using the same active serviceengine.
            - Redistribution of the virtualservices can be either manual or automated when the failed serviceengine recovers.
            - Redistribution is based on the auto redistribute property of the serviceenginegroup.
            - Enum options - ACTIVE_STANDBY_SE_1, ACTIVE_STANDBY_SE_2.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as ACTIVE_STANDBY_SE_1.
        type: str
    advertise_down_vs:
        description:
            - Keep advertising virtual service via bgp even if it is marked down by health monitor.
            - This setting takes effect for future virtual service flaps.
            - To advertise current vses that are down, please disable and re-enable the virtual service.
            - Field introduced in 20.1.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Allowed in essentials (allowed values- false), basic (allowed values- false) edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    allow_invalid_client_cert:
        description:
            - Process request even if invalid client certificate is presented.
            - Datascript apis need to be used for processing of such requests.
            - Field introduced in 18.2.3.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Allowed in essentials (allowed values- false), basic (allowed values- false) edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    analytics_policy:
        description:
            - Determines analytics settings for the application.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: dict
    analytics_profile_ref:
        description:
            - Specifies settings related to analytics.
            - It is a reference to an object of type analyticsprofile.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    application_profile_ref:
        description:
            - Enable application layer specific features for the virtual service.
            - It is a reference to an object of type applicationprofile.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
            - Special default for essentials edition is system-l4-application.
        type: str
    azure_availability_set:
        description:
            - (internal-use)applicable for azure only.
            - Azure availability set to which this vs is associated.
            - Internally set by the cloud connector.
            - Field introduced in 17.2.12, 18.1.2.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    bgp_local_preference:
        description:
            - Local_pref to be used for vsvip advertised.
            - Applicable only over ibgp.
            - Field introduced in 30.2.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: int
    bgp_num_as_path_prepend:
        description:
            - Number of times the local as should be prepended additionally to vsvip.
            - Applicable only over ebgp.
            - Allowed values are 1-10.
            - Field introduced in 30.2.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: int
    bgp_peer_labels:
        description:
            - Select bgp peers, using peer label, for vsvip advertisement.
            - Field introduced in 20.1.5.
            - Maximum of 128 items allowed.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: list
        elements: str
    bot_policy_ref:
        description:
            - Bot detection policy for the virtual service.
            - It is a reference to an object of type botdetectionpolicy.
            - Field introduced in 21.1.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: str
    bulk_sync_kvcache:
        description:
            - (this is a beta feature).
            - Sync key-value cache to the new ses when vs is scaled out.
            - For ex  ssl sessions are stored using vs's key-value cache.
            - When the vs is scaled out, the ssl session information is synced to the new se, allowing existing ssl sessions to be reused on the new se.
            - Field introduced in 17.2.7, 18.1.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Allowed in essentials (allowed values- false), basic (allowed values- false) edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    close_client_conn_on_config_update:
        description:
            - Close client connection on vs config update.
            - Field introduced in 17.2.4.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Allowed in essentials (allowed values- false), basic (allowed values- false) edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    cloud_config_cksum:
        description:
            - Checksum of cloud configuration for vs.
            - Internally set by cloud connector.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    cloud_ref:
        description:
            - It is a reference to an object of type cloud.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    cloud_type:
        description:
            - Enum options - CLOUD_NONE, CLOUD_VCENTER, CLOUD_OPENSTACK, CLOUD_AWS, CLOUD_VCA, CLOUD_APIC, CLOUD_MESOS, CLOUD_LINUXSERVER, CLOUD_DOCKER_UCP,
            - CLOUD_RANCHER, CLOUD_OSHIFT_K8S, CLOUD_AZURE, CLOUD_GCP, CLOUD_NSXT.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Allowed in essentials (allowed values- cloud_none,cloud_vcenter), basic (allowed values- cloud_none,cloud_nsxt) edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as CLOUD_NONE.
        type: str
    configpb_attributes:
        description:
            - Protobuf versioning for config pbs.
            - Field introduced in 21.1.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: dict
    connections_rate_limit:
        description:
            - Rate limit the incoming connections to this virtual service.
            - Allowed with any value in enterprise, basic, enterprise with cloud services edition.
        type: dict
    content_rewrite:
        description:
            - Profile used to match and rewrite strings in request and/or response body.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: dict
    created_by:
        description:
            - Creator name.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    csrf_policy_ref:
        description:
            - Csrf protection policy for the virtual service.
            - It is a reference to an object of type csrfpolicy.
            - Field introduced in 30.2.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: str
    delay_fairness:
        description:
            - Select the algorithm for qos fairness.
            - This determines how multiple virtual services sharing the same service engines will prioritize traffic over a congested network.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Allowed in essentials (allowed values- false), basic (allowed values- false) edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    description:
        description:
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    dns_info:
        description:
            - Service discovery specific data including fully qualified domain name, type and time-to-live of the dns record.
            - Note that only one of fqdn and dns_info setting is allowed.
            - Maximum of 1000 items allowed.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: list
        elements: dict
    dns_policies:
        description:
            - Dns policies applied on the dns traffic of the virtual service.
            - Field introduced in 17.1.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: list
        elements: dict
    east_west_placement:
        description:
            - Force placement on all se's in service group (mesos mode only).
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Allowed in essentials (allowed values- false), basic (allowed values- false) edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    enable_autogw:
        description:
            - Response traffic to clients will be sent back to the source mac address of the connection, rather than statically sent to a default gateway.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Allowed in essentials (allowed values- false), basic (allowed values- false) edition.
            - Special default for essentials edition is false, basic edition is false, enterprise edition is true.
            - Default value when not specified in API or module is interpreted by Avi Controller as True.
        type: bool
    enable_rhi:
        description:
            - Enable route health injection using the bgp config in the vrf context.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: bool
    enable_rhi_snat:
        description:
            - Enable route health injection for source nat'ted floating ip address using the bgp config in the vrf context.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: bool
    enable_session:
        description:
            - Enable http sessions for this virtual service.
            - If enabled, a session cookie will be added to http responses and persistent key-value store will be activated.
            - Field introduced in 30.2.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    enabled:
        description:
            - Enable or disable the virtual service.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as True.
        type: bool
    error_page_profile_ref:
        description:
            - Error page profile to be used for this virtualservice.this profile is used to send the custom error page to the client generated by the proxy.
            - It is a reference to an object of type errorpageprofile.
            - Field introduced in 17.2.4.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    flow_dist:
        description:
            - Criteria for flow distribution among ses.
            - Enum options - LOAD_AWARE, CONSISTENT_HASH_SOURCE_IP_ADDRESS, CONSISTENT_HASH_SOURCE_IP_ADDRESS_AND_PORT.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Allowed in essentials (allowed values- load_aware), basic (allowed values- load_aware) edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as LOAD_AWARE.
        type: str
    flow_label_type:
        description:
            - Criteria for flow labelling.
            - Enum options - NO_LABEL, APPLICATION_LABEL, SERVICE_LABEL.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as NO_LABEL.
        type: str
    fqdn:
        description:
            - Dns resolvable, fully qualified domain name of the virtualservice.
            - Only one of 'fqdn' and 'dns_info' configuration is allowed.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: str
    host_name_xlate:
        description:
            - Translate the host name sent to the servers to this value.
            - Translate the host name sent from servers back to the value used by the client.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: str
    http_policies:
        description:
            - Http policies applied on the data traffic of the virtual service.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: list
        elements: dict
    icap_request_profile_refs:
        description:
            - The config settings for the icap server when checking the http request.
            - It is a reference to an object of type icapprofile.
            - Field introduced in 20.1.1.
            - Maximum of 1 items allowed.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: list
        elements: str
    ign_pool_net_reach:
        description:
            - Ignore pool servers network reachability constraints for virtual service placement.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    jwt_config:
        description:
            - Application-specific config for jwt validation.
            - Field introduced in 20.1.3.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: dict
    l4_policies:
        description:
            - L4 policies applied to the data traffic of the virtual service.
            - Field introduced in 17.2.7.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: list
        elements: dict
    ldap_vs_config:
        description:
            - Application-specific ldap config.
            - Field introduced in 21.1.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: dict
    limit_doser:
        description:
            - Limit potential dos attackers who exceed max_cps_per_client significantly to a fraction of max_cps_per_client for a while.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    markers:
        description:
            - List of labels to be used for granular rbac.
            - Field introduced in 20.1.5.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: list
        elements: dict
    max_cps_per_client:
        description:
            - Maximum connections per second per client ip.
            - Allowed values are 10-1000.
            - Special values are 0- unlimited.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 0.
        type: int
    microservice_ref:
        description:
            - Microservice representing the virtual service.
            - It is a reference to an object of type microservice.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: str
    min_pools_up:
        description:
            - Minimum number of up pools to mark vs up.
            - Field introduced in 18.2.1, 17.2.12.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: int
    name:
        description:
            - Name for the virtual service.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        required: true
        type: str
    network_profile_ref:
        description:
            - Determines network settings such as protocol, tcp or udp, and related options for the protocol.
            - It is a reference to an object of type networkprofile.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
            - Special default for essentials edition is system-tcp-fast-path.
        type: str
    network_security_policy_ref:
        description:
            - Network security policies for the virtual service.
            - It is a reference to an object of type networksecuritypolicy.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    nsx_securitygroup:
        description:
            - A list of nsx groups representing the clients which can access the virtual ip of the virtual service.
            - Field introduced in 17.1.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: list
        elements: str
    oauth_vs_config:
        description:
            - Virtualservice specific oauth config.
            - Field introduced in 21.1.3.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: dict
    performance_limits:
        description:
            - Optional settings that determine performance limits like max connections or bandwdith etc.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: dict
    pool_group_ref:
        description:
            - The pool group is an object that contains pools.
            - It is a reference to an object of type poolgroup.
            - Allowed with any value in enterprise, basic, enterprise with cloud services edition.
        type: str
    pool_ref:
        description:
            - The pool is an object that contains destination servers and related attributes such as load-balancing and persistence.
            - It is a reference to an object of type pool.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    remove_listening_port_on_vs_down:
        description:
            - Remove listening port if virtualservice is down.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    requests_rate_limit:
        description:
            - Rate limit the incoming requests to this virtual service.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: dict
    revoke_vip_route:
        description:
            - Revoke the advertisement of virtual service via the cloud if it is marked down by health monitor.
            - Supported for nsxt clouds only.this setting takes effect for future virtual service flaps.
            - To advertise current vses that are down, please disable and re-enable the virtual service.
            - Field introduced in 30.2.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    saml_sp_config:
        description:
            - Application-specific saml config.
            - Field introduced in 18.2.3.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: dict
    scaleout_ecmp:
        description:
            - Disable re-distribution of flows across service engines for a virtual service.
            - Enable if the network itself performs flow hashing with ecmp in environments such as gcp.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    se_group_ref:
        description:
            - The service engine group to use for this virtual service.
            - Moving to a new se group is disruptive to existing connections for this vs.
            - It is a reference to an object of type serviceenginegroup.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    security_policy_ref:
        description:
            - Security policy applied on the traffic of the virtual service.
            - This policy is used to perform security actions such as distributed denial of service (ddos) attack mitigation, etc.
            - It is a reference to an object of type securitypolicy.
            - Field introduced in 18.2.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: str
    server_network_profile_ref:
        description:
            - Determines the network settings profile for the server side of tcp proxied connections.
            - Leave blank to use the same settings as the client to vs side of the connection.
            - It is a reference to an object of type networkprofile.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: str
    service_metadata:
        description:
            - Metadata pertaining to the service provided by this virtual service.
            - In openshift/kubernetes environments, egress pod info is stored.
            - Any user input to this field will be overwritten by avi vantage.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    service_pool_select:
        description:
            - Select pool based on destination port.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: list
        elements: dict
    services:
        description:
            - List of services defined for this virtual service.
            - Maximum of 2048 items allowed.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: list
        elements: dict
    sideband_profile:
        description:
            - Sideband configuration to be used for this virtualservice.it can be used for sending traffic to sideband vips for external inspection etc.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: dict
    snat_ip:
        description:
            - Nat'ted floating source ip address(es) for upstream connection to servers.
            - Maximum of 32 items allowed.
            - Allowed with any value in enterprise, basic, enterprise with cloud services edition.
        type: list
        elements: dict
    snat_ip6_addresses:
        description:
            - Ipv6 address for se snat.
            - Field introduced in 30.2.1.
            - Maximum of 32 items allowed.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: list
        elements: dict
    sp_pool_refs:
        description:
            - Gslb pools used to manage site-persistence functionality.
            - Each site-persistence pool contains the virtualservices in all the other sites, that is auto-generated by the gslb manager.
            - This is a read-only field for the user.
            - It is a reference to an object of type pool.
            - Field introduced in 17.2.2.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: list
        elements: str
    ssl_key_and_certificate_refs:
        description:
            - Select or create one or two certificates, ec and/or rsa, that will be presented to ssl/tls terminated connections.
            - It is a reference to an object of type sslkeyandcertificate.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: list
        elements: str
    ssl_profile_ref:
        description:
            - Determines the set of ssl versions and ciphers to accept for ssl/tls terminated connections.
            - It is a reference to an object of type sslprofile.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    ssl_profile_selectors:
        description:
            - Select ssl profile based on client ip address match.
            - Field introduced in 18.2.3.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: list
        elements: dict
    ssl_sess_cache_avg_size:
        description:
            - Expected number of ssl session cache entries (may be exceeded).
            - Allowed values are 1024-16383.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 1024.
        type: int
    sso_policy_ref:
        description:
            - The sso policy attached to the virtualservice.
            - It is a reference to an object of type ssopolicy.
            - Field introduced in 18.2.3.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: str
    static_dns_records:
        description:
            - List of static dns records applied to this virtual service.
            - These are static entries and no health monitoring is performed against the ip addresses.
            - Maximum of 2000 items allowed.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: list
        elements: dict
    tenant_ref:
        description:
            - It is a reference to an object of type tenant.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    test_se_datastore_level_1_ref:
        description:
            - Used for testing se datastore upgrade 2.0 functionality.
            - It is a reference to an object of type testsedatastorelevel1.
            - Field introduced in 18.2.6.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    topology_policies:
        description:
            - Topology policies applied on the dns traffic of the virtual service based ongslb topology algorithm.
            - Field introduced in 18.2.3.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: list
        elements: dict
    traffic_clone_profile_ref:
        description:
            - Server network or list of servers for cloning traffic.
            - It is a reference to an object of type trafficcloneprofile.
            - Field introduced in 17.1.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: str
    traffic_enabled:
        description:
            - Knob to enable the virtual service traffic on its assigned service engines.
            - This setting is effective only when the enabled flag is set to true.
            - Field introduced in 17.2.8.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as True.
        type: bool
    type:
        description:
            - Specify if this is a normal virtual service, or if it is the parent or child of an sni-enabled virtual hosted virtual service.
            - Enum options - VS_TYPE_NORMAL, VS_TYPE_VH_PARENT, VS_TYPE_VH_CHILD.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Allowed in essentials (allowed values- vs_type_normal), basic (allowed values- vs_type_normal,vs_type_vh_parent) edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as VS_TYPE_NORMAL.
        type: str
    url:
        description:
            - Avi controller URL of the object.
        type: str
    use_bridge_ip_as_vip:
        description:
            - Use bridge ip as vip on each host in mesos deployments.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Allowed in essentials (allowed values- false), basic (allowed values- false) edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    use_vip_as_snat:
        description:
            - Use the virtual ip as the snat ip for health monitoring and sending traffic to the backend servers instead of the service engine interface ip.
            - The caveat of enabling this option is that the virtualservice cannot be configued in an active-active ha mode.
            - Dns based multi vip solution has to be used for ha & non-disruptive upgrade purposes.
            - Field introduced in 17.1.9,17.2.3.
            - Allowed with any value in enterprise, basic, enterprise with cloud services edition.
            - Allowed in essentials (allowed values- false) edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    uuid:
        description:
            - Uuid of the virtualservice.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    vh_domain_name:
        description:
            - The exact name requested from the client's sni-enabled tls hello domain name field.
            - If this is a match, the parent vs will forward the connection to this child vs.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: list
        elements: str
    vh_matches:
        description:
            - Match criteria to select this child vs.
            - Field introduced in 20.1.3.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: list
        elements: dict
    vh_parent_vs_ref:
        description:
            - Specifies the virtual service acting as virtual hosting (sni) parent.
            - It is a reference to an object of type virtualservice.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    vh_type:
        description:
            - Specify if the virtual hosting vs is of type sni or enhanced.
            - Enum options - VS_TYPE_VH_SNI, VS_TYPE_VH_ENHANCED.
            - Field introduced in 20.1.3.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Allowed in basic (allowed values- vs_type_vh_sni,vs_type_vh_enhanced) edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as VS_TYPE_VH_SNI.
        type: str
    vip:
        description:
            - List of virtual service ips.
            - While creating a 'shared vs',please use vsvip_ref to point to the shared entities.
            - Field introduced in 17.1.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: list
        elements: dict
    vrf_context_ref:
        description:
            - Virtual routing context that the virtual service is bound to.
            - This is used to provide the isolation of the set of networks the application is attached to.
            - It is a reference to an object of type vrfcontext.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    vs_datascripts:
        description:
            - Datascripts applied on the data traffic of the virtual service.
            - Allowed with any value in enterprise, basic, enterprise with cloud services edition.
        type: list
        elements: dict
    vsvip_cloud_config_cksum:
        description:
            - Checksum of cloud configuration for vsvip.
            - Internally set by cloud connector.
            - Field introduced in 17.2.9, 18.1.2.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    vsvip_ref:
        description:
            - Mostly used during the creation of shared vs, this field refers to entities that can be shared across virtual services.
            - It is a reference to an object of type vsvip.
            - Field introduced in 17.1.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    waf_policy_ref:
        description:
            - Waf policy for the virtual service.
            - It is a reference to an object of type wafpolicy.
            - Field introduced in 17.2.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: str
    weight:
        description:
            - The quality of service weight to assign to traffic transmitted from this virtual service.
            - A higher weight will prioritize traffic versus other virtual services sharing the same service engines.
            - Allowed values are 1-128.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Allowed in essentials (allowed values- 1), basic (allowed values- 1) edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 1.
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

- name: Create SSL Virtual Service using Pool testpool2
  vmware.alb.avi_virtualservice:
    avi_credentials: "{{ avi_credentials }}"
    name: newtestvs
    state: present
    performance_limits:
    max_concurrent_connections: 1000
    vsvip_ref: /api/vsvip/?name=vsvip-newtestvs-Default-Cloud
    services:
        - port: 443
          enable_ssl: true
        - port: 80
    ssl_profile_ref: '/api/sslprofile?name=System-Standard'
    application_profile_ref: '/api/applicationprofile?name=System-Secure-HTTP'
    ssl_key_and_certificate_refs:
        - '/api/sslkeyandcertificate?name=System-Default-Cert'
    pool_ref: '/api/pool?name=testpool2'
"""

RETURN = '''
obj:
    description: VirtualService (api/virtualservice) object
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
        active_standby_se_tag=dict(type='str',),
        advertise_down_vs=dict(type='bool',),
        allow_invalid_client_cert=dict(type='bool',),
        analytics_policy=dict(type='dict',),
        analytics_profile_ref=dict(type='str',),
        application_profile_ref=dict(type='str',),
        azure_availability_set=dict(type='str',),
        bgp_local_preference=dict(type='int',),
        bgp_num_as_path_prepend=dict(type='int',),
        bgp_peer_labels=dict(type='list', elements='str',),
        bot_policy_ref=dict(type='str',),
        bulk_sync_kvcache=dict(type='bool',),
        close_client_conn_on_config_update=dict(type='bool',),
        cloud_config_cksum=dict(type='str',),
        cloud_ref=dict(type='str',),
        cloud_type=dict(type='str',),
        configpb_attributes=dict(type='dict',),
        connections_rate_limit=dict(type='dict',),
        content_rewrite=dict(type='dict',),
        created_by=dict(type='str',),
        csrf_policy_ref=dict(type='str',),
        delay_fairness=dict(type='bool',),
        description=dict(type='str',),
        dns_info=dict(type='list', elements='dict',),
        dns_policies=dict(type='list', elements='dict',),
        east_west_placement=dict(type='bool',),
        enable_autogw=dict(type='bool',),
        enable_rhi=dict(type='bool',),
        enable_rhi_snat=dict(type='bool',),
        enable_session=dict(type='bool',),
        enabled=dict(type='bool',),
        error_page_profile_ref=dict(type='str',),
        flow_dist=dict(type='str',),
        flow_label_type=dict(type='str',),
        fqdn=dict(type='str',),
        host_name_xlate=dict(type='str',),
        http_policies=dict(type='list', elements='dict',),
        icap_request_profile_refs=dict(type='list', elements='str',),
        ign_pool_net_reach=dict(type='bool',),
        jwt_config=dict(type='dict',),
        l4_policies=dict(type='list', elements='dict',),
        ldap_vs_config=dict(type='dict',),
        limit_doser=dict(type='bool',),
        markers=dict(type='list', elements='dict',),
        max_cps_per_client=dict(type='int',),
        microservice_ref=dict(type='str',),
        min_pools_up=dict(type='int',),
        name=dict(type='str', required=True),
        network_profile_ref=dict(type='str',),
        network_security_policy_ref=dict(type='str',),
        nsx_securitygroup=dict(type='list', elements='str',),
        oauth_vs_config=dict(type='dict',),
        performance_limits=dict(type='dict',),
        pool_group_ref=dict(type='str',),
        pool_ref=dict(type='str',),
        remove_listening_port_on_vs_down=dict(type='bool',),
        requests_rate_limit=dict(type='dict',),
        revoke_vip_route=dict(type='bool',),
        saml_sp_config=dict(type='dict',),
        scaleout_ecmp=dict(type='bool',),
        se_group_ref=dict(type='str',),
        security_policy_ref=dict(type='str',),
        server_network_profile_ref=dict(type='str',),
        service_metadata=dict(type='str',),
        service_pool_select=dict(type='list', elements='dict',),
        services=dict(type='list', elements='dict',),
        sideband_profile=dict(type='dict',),
        snat_ip=dict(type='list', elements='dict',),
        snat_ip6_addresses=dict(type='list', elements='dict',),
        sp_pool_refs=dict(type='list', elements='str',),
        ssl_key_and_certificate_refs=dict(type='list', elements='str',),
        ssl_profile_ref=dict(type='str',),
        ssl_profile_selectors=dict(type='list', elements='dict',),
        ssl_sess_cache_avg_size=dict(type='int',),
        sso_policy_ref=dict(type='str',),
        static_dns_records=dict(type='list', elements='dict',),
        tenant_ref=dict(type='str',),
        test_se_datastore_level_1_ref=dict(type='str',),
        topology_policies=dict(type='list', elements='dict',),
        traffic_clone_profile_ref=dict(type='str',),
        traffic_enabled=dict(type='bool',),
        type=dict(type='str',),
        url=dict(type='str',),
        use_bridge_ip_as_vip=dict(type='bool',),
        use_vip_as_snat=dict(type='bool',),
        uuid=dict(type='str',),
        vh_domain_name=dict(type='list', elements='str',),
        vh_matches=dict(type='list', elements='dict',),
        vh_parent_vs_ref=dict(type='str',),
        vh_type=dict(type='str',),
        vip=dict(type='list', elements='dict',),
        vrf_context_ref=dict(type='str',),
        vs_datascripts=dict(type='list', elements='dict',),
        vsvip_cloud_config_cksum=dict(type='str',),
        vsvip_ref=dict(type='str',),
        waf_policy_ref=dict(type='str',),
        weight=dict(type='int',),
    )
    argument_specs.update(avi_common_argument_spec())
    module = AnsibleModule(
        argument_spec=argument_specs, supports_check_mode=True)
    if not HAS_REQUESTS:
        return module.fail_json(msg=(
            'Python requests package is not installed. '
            'For installation instructions, visit https://pypi.org/project/requests.'))
    return avi_ansible_api(module, 'virtualservice',
                           set())


if __name__ == '__main__':
    main()
