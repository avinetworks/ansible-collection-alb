#!/usr/bin/python
# -*- coding: utf-8 -*-

# module_check: supported

# Copyright 2021 VMware, Inc. All rights reserved. VMware Confidential
# SPDX-License-Identifier: Apache License 2.0
from __future__ import absolute_import, division, print_function
__metaclass__ = type
ANSIBLE_METADATA = {'metadata_version': '1.1', 'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = \
    '''
---
module: avi_serviceenginegroup
author: Gaurav Rastogi (@grastogi23) <grastogi@avinetworks.com>
short_description: Module for setup of ServiceEngineGroup Avi RESTful Object
description:
    - This module is used to configure ServiceEngineGroup object
options:
    state:
        description:
            - The state that should be applied on the entity.
        default: present
        choices: ["absent", "present"]
        type: str
    name:
        description:
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        required: true
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
    aggressive_failure_detection:
        description:
            - Enable aggressive failover configuration for ha.
            - Allowed in enterprise edition with any value, essentials edition(allowed values- false), basic edition(allowed values- false), enterprise with
            - cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    allow_burst:
        description:
            - Allow ses to be created using burst license.
            - Field introduced in 17.2.5.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: bool
    app_cache_threshold:
        description:
            - The max memory that can be allocated for the app cache.
            - This value will act as an upper bound on the cache size specified in app_cache_percent.
            - Special values are 0- disable.
            - Field introduced in 20.1.1.
            - Unit is gb.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 5.
        type: int
    app_learning_memory_percent:
        description:
            - A percent value of total se memory reserved for application learning.
            - This is an se bootup property and requires se restart.
            - Allowed values are 0 - 10.
            - Field introduced in 18.2.3.
            - Unit is percent.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 0.
        type: int
    archive_shm_limit:
        description:
            - Amount of se memory in gb until which shared memory is collected in core archive.
            - Field introduced in 17.1.3.
            - Unit is gb.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 8.
        type: int
    async_ssl:
        description:
            - Ssl handshakes will be handled by dedicated ssl threads.requires se reboot.
            - Allowed in enterprise edition with any value, essentials edition(allowed values- false), basic edition(allowed values- false), enterprise with
            - cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    async_ssl_threads:
        description:
            - Number of async ssl threads per se_dp.requires se reboot.
            - Allowed values are 1-16.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 1.
        type: int
    auto_rebalance:
        description:
            - If set, virtual services will be automatically migrated when load on an se is less than minimum or more than maximum thresholds.
            - Only alerts are generated when the auto_rebalance is not set.
            - Allowed in enterprise edition with any value, essentials edition(allowed values- false), basic edition(allowed values- false), enterprise with
            - cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    auto_rebalance_capacity_per_se:
        description:
            - Capacities of se for auto rebalance for each criteria.
            - Field introduced in 17.2.4.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: list
        elements: int
    auto_rebalance_criteria:
        description:
            - Set of criteria for se auto rebalance.
            - Enum options - SE_AUTO_REBALANCE_CPU, SE_AUTO_REBALANCE_PPS, SE_AUTO_REBALANCE_MBPS, SE_AUTO_REBALANCE_OPEN_CONNS, SE_AUTO_REBALANCE_CPS.
            - Field introduced in 17.2.3.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: list
        elements: str
    auto_rebalance_interval:
        description:
            - Frequency of rebalance, if 'auto rebalance' is enabled.
            - Unit is sec.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 300.
        type: int
    auto_redistribute_active_standby_load:
        description:
            - Redistribution of virtual services from the takeover se to the replacement se can cause momentary traffic loss.
            - If the auto-redistribute load option is left in its default off state, any desired rebalancing requires calls to rest api.
            - Allowed in enterprise edition with any value, essentials edition(allowed values- false), basic edition(allowed values- false), enterprise with
            - cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    availability_zone_refs:
        description:
            - Availability zones for virtual service high availability.
            - It is a reference to an object of type availabilityzone.
            - Field introduced in 20.1.1.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: list
        elements: str
    baremetal_dispatcher_handles_flows:
        description:
            - Control if dispatcher core also handles tcp flows in baremetal se.
            - Field introduced in 21.1.3.
            - Allowed in enterprise edition with any value, essentials edition with any value, basic edition with any value, enterprise with cloud services
            - edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    bgp_peer_monitor_failover_enabled:
        description:
            - Enable bgp peer monitoring based failover.
            - Field introduced in 21.1.3.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    bgp_state_update_interval:
        description:
            - Bgp peer state update interval.
            - Allowed values are 5-100.
            - Field introduced in 17.2.14,18.1.5,18.2.1.
            - Unit is sec.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 60.
        type: int
    compress_ip_rules_for_each_ns_subnet:
        description:
            - Compress ip rules into a single subnet based ip rule for each north-south ipam subnet configured in pcap mode in openshift/kubernetes node.
            - Field introduced in 18.2.9, 20.1.1.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as True.
        type: bool
    config_debugs_on_all_cores:
        description:
            - Enable config debugs on all cores of se.
            - Field introduced in 17.2.13,18.1.5,18.2.1.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    configpb_attributes:
        description:
            - Protobuf versioning for config pbs.
            - Field introduced in 21.1.1.
            - Allowed in enterprise edition with any value, essentials edition with any value, basic edition with any value, enterprise with cloud services
            - edition.
        type: dict
    core_shm_app_cache:
        description:
            - Include shared memory for app cache in core file.requires se reboot.
            - Field introduced in 18.2.8, 20.1.1.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    core_shm_app_learning:
        description:
            - Include shared memory for app learning in core file.requires se reboot.
            - Field introduced in 18.2.8, 20.1.1.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    custom_securitygroups_data:
        description:
            - Custom security groups to be associated with data vnics for se instances in openstack and aws clouds.
            - Field introduced in 17.1.3.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: list
        elements: str
    custom_securitygroups_mgmt:
        description:
            - Custom security groups to be associated with management vnic for se instances in openstack and aws clouds.
            - Field introduced in 17.1.3.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: list
        elements: str
    data_network_id:
        description:
            - Subnet used to spin up the data nic for service engines, used only for azure cloud.
            - Overrides the cloud level setting for service engine subnet.
            - Field introduced in 18.2.3.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: str
    datascript_timeout:
        description:
            - Number of instructions before datascript times out.
            - Allowed values are 0-100000000.
            - Field introduced in 18.2.3.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 1000000.
        type: int
    deactivate_ipv6_discovery:
        description:
            - If activated, ipv6 address and route discovery are deactivated.requires se reboot.
            - Field introduced in 21.1.1.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
        type: bool
    deactivate_kni_filtering_at_dispatcher:
        description:
            - Deactivate filtering of packets to kni interface.
            - To be used under surveillance of avi support.
            - Field introduced in 21.1.3.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
        type: bool
    disable_avi_securitygroups:
        description:
            - By default, avi creates and manages security groups along with custom sg provided by user.
            - Set this to true to disallow avi to create and manage new security groups.
            - Avi will only make use of custom security groups provided by user.
            - This option is supported for aws and openstack cloud types.
            - Field introduced in 17.2.13,18.1.4,18.2.1.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    disable_csum_offloads:
        description:
            - Stop using tcp/udp and ip checksum offload features of nics.
            - Field introduced in 17.1.14, 17.2.5, 18.1.1.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    disable_flow_probes:
        description:
            - Disable flow probes for scaled out vs'es.
            - Field introduced in 20.1.3.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    disable_gro:
        description:
            - Disable generic receive offload (gro) in dpdk poll-mode driver packet receive path.
            - Gro is on by default on nics that do not support lro (large receive offload) or do not gain performance boost from lro.
            - Field introduced in 17.2.5, 18.1.1.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: bool
    disable_se_memory_check:
        description:
            - If set, disable the config memory check done in service engine.
            - Field introduced in 18.1.2.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    disable_tso:
        description:
            - Disable tcp segmentation offload (tso) in dpdk poll-mode driver packet transmit path.
            - Tso is on by default on nics that support it.
            - Field introduced in 17.2.5, 18.1.1.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    distribute_load_active_standby:
        description:
            - Use both the active and standby service engines for virtual service placement in the legacy active standby ha mode.
            - Allowed in enterprise edition with any value, essentials edition(allowed values- false), basic edition(allowed values- false), enterprise with
            - cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    distribute_queues:
        description:
            - Distributes queue ownership among cores so multiple cores handle dispatcher duties.
            - Requires se reboot.
            - Deprecated from 18.2.8, instead use max_queues_per_vnic.
            - Field introduced in 17.2.8.
            - Allowed in enterprise edition with any value, essentials edition(allowed values- false), basic edition(allowed values- false), enterprise with
            - cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    distribute_vnics:
        description:
            - Distributes vnic ownership among cores so multiple cores handle dispatcher duties.requires se reboot.
            - Field introduced in 18.2.5.
            - Allowed in enterprise edition with any value, essentials edition(allowed values- false), basic edition(allowed values- false), enterprise with
            - cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    downstream_send_timeout:
        description:
            - Timeout for downstream to become writable.
            - Field introduced in 21.1.1.
            - Unit is milliseconds.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 3600000.
        type: int
    dp_aggressive_deq_interval_msec:
        description:
            - Dequeue interval for receive queue from se_dp in aggressive mode.
            - Allowed values are 1-1000.
            - Field introduced in 21.1.1.
            - Unit is milliseconds.
            - Allowed in enterprise edition with any value, essentials edition with any value, basic edition with any value, enterprise with cloud services
            - edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 1.
        type: int
    dp_aggressive_enq_interval_msec:
        description:
            - Enqueue interval for request queue to se_dp in aggressive mode.
            - Allowed values are 1-1000.
            - Field introduced in 21.1.1.
            - Unit is milliseconds.
            - Allowed in enterprise edition with any value, essentials edition with any value, basic edition with any value, enterprise with cloud services
            - edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 1.
        type: int
    dp_aggressive_hb_frequency:
        description:
            - Frequency of se - se hb messages when aggressive failure mode detection is enabled.
            - Field introduced in 20.1.3.
            - Unit is milliseconds.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 100.
        type: int
    dp_aggressive_hb_timeout_count:
        description:
            - Consecutive hb failures after which failure is reported to controller,when aggressive failure mode detection is enabled.
            - Field introduced in 20.1.3.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 10.
        type: int
    dp_deq_interval_msec:
        description:
            - Dequeue interval for receive queue from se_dp.
            - Allowed values are 1-1000.
            - Field introduced in 21.1.1.
            - Unit is milliseconds.
            - Allowed in enterprise edition with any value, essentials edition with any value, basic edition with any value, enterprise with cloud services
            - edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 20.
        type: int
    dp_enq_interval_msec:
        description:
            - Enqueue interval for request queue to se_dp.
            - Allowed values are 1-1000.
            - Field introduced in 21.1.1.
            - Unit is milliseconds.
            - Allowed in enterprise edition with any value, essentials edition with any value, basic edition with any value, enterprise with cloud services
            - edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 20.
        type: int
    dp_hb_frequency:
        description:
            - Frequency of se - se hb messages when aggressive failure mode detection is not enabled.
            - Field introduced in 20.1.3.
            - Unit is milliseconds.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 100.
        type: int
    dp_hb_timeout_count:
        description:
            - Consecutive hb failures after which failure is reported to controller, when aggressive failure mode detection is not enabled.
            - Field introduced in 20.1.3.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 10.
        type: int
    dpdk_gro_timeout_interval:
        description:
            - The timeout for gro coalescing interval.
            - 0 indicates non-timer based gro.
            - Allowed values are 0-900.
            - Field introduced in 22.1.1.
            - Unit is microseconds.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 50.
        type: int
    enable_gratarp_permanent:
        description:
            - Enable gratarp for vip_ip.
            - Field introduced in 18.2.3.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    enable_hsm_log:
        description:
            - Enable hsm luna engine logs.
            - Field introduced in 21.1.1.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    enable_hsm_priming:
        description:
            - (this is a beta feature).
            - Enable hsm key priming.
            - If enabled, key handles on the hsm will be synced to se before processing client connections.
            - Field introduced in 17.2.7, 18.1.1.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    enable_multi_lb:
        description:
            - Applicable only for azure cloud with basic sku lb.
            - If set, additional azure lbs will be automatically created if resources in existing lb are exhausted.
            - Field introduced in 17.2.10, 18.1.2.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    enable_pcap_tx_ring:
        description:
            - Enable tx ring support in pcap mode of operation.
            - Tso feature is not supported with tx ring enabled.
            - Deprecated from 18.2.8, instead use pcap_tx_mode.
            - Requires se reboot.
            - Field introduced in 18.2.5.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: bool
    ephemeral_portrange_end:
        description:
            - End local ephemeral port number for outbound connections.
            - Field introduced in 17.2.13, 18.1.5, 18.2.1.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: int
    ephemeral_portrange_start:
        description:
            - Start local ephemeral port number for outbound connections.
            - Field introduced in 17.2.13, 18.1.5, 18.2.1.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: int
    extra_config_multiplier:
        description:
            - Multiplier for extra config to support large vs/pool config.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 0.0.
        type: float
    flow_table_new_syn_max_entries:
        description:
            - Maximum number of flow table entries that have not completed tcp three-way handshake yet.
            - Field introduced in 17.2.5.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 0.
        type: int
    free_list_size:
        description:
            - Number of entries in the free list.
            - Field introduced in 17.2.10, 18.1.2.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 1024.
        type: int
    gratarp_permanent_periodicity:
        description:
            - Gratarp periodicity for vip-ip.
            - Allowed values are 5-30.
            - Field introduced in 18.2.3.
            - Unit is min.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 10.
        type: int
    grpc_channel_connect_timeout:
        description:
            - Timeout in seconds that se waits for a grpc channel to connect to server, before it retries.
            - Allowed values are 5-45.
            - Field introduced in 22.1.1.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 15.
        type: int
    handle_per_pkt_attack:
        description:
            - Configuration to handle per packet attack handling.for example, dns reflection attack is a type of attack where a response packet is sent to the
            - dns vs.this configuration tells if such packets should be dropped without further processing.
            - Field introduced in 20.1.3.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as True.
        type: bool
    hardwaresecuritymodulegroup_ref:
        description:
            - It is a reference to an object of type hardwaresecuritymodulegroup.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
        type: str
    heap_minimum_config_memory:
        description:
            - Minimum required heap memory to apply any configuration.
            - Allowed values are 0-100.
            - Field introduced in 18.1.2.
            - Unit is mb.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 8.
        type: int
    hm_on_standby:
        description:
            - Enable active health monitoring from the standby se for all placed virtual services.
            - Allowed in enterprise edition with any value, essentials edition(allowed values- false), basic edition(allowed values- false), enterprise with
            - cloud services edition.
            - Special default for essentials edition is false, basic edition is false, enterprise is true.
            - Default value when not specified in API or module is interpreted by Avi Controller as True.
        type: bool
    host_attribute_key:
        description:
            - Key of a (key, value) pair identifying a label for a set of nodes usually in container clouds.
            - Needs to be specified together with host_attribute_value.
            - Ses can be configured differently including ha modes across different se groups.
            - May also be used for isolation between different classes of virtualservices.
            - Virtualservices' se group may be specified via annotations/labels.
            - A openshift/kubernetes namespace maybe annotated with a matching se group label as openshift.io/node-selector  apptype=prod.
            - When multiple se groups are used in a cloud with host attributes specified,just a single se group can exist as a match-all se group without a
            - host_attribute_key.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: str
    host_attribute_value:
        description:
            - Value of a (key, value) pair identifying a label for a set of nodes usually in container clouds.
            - Needs to be specified together with host_attribute_key.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: str
    host_gateway_monitor:
        description:
            - Enable the host gateway monitor when service engine is deployed as docker container.
            - Disabled by default.
            - Field introduced in 17.2.4.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    http_rum_console_log:
        description:
            - Enable javascript console logs on the client browser when collecting client insights.
            - Field introduced in 21.1.1.
            - Allowed in enterprise edition with any value, essentials edition(allowed values- false), basic edition(allowed values- false), enterprise with
            - cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    http_rum_min_content_length:
        description:
            - Minimum response size content length to sample for client insights.
            - Field introduced in 21.1.1.
            - Allowed in enterprise edition with any value, essentials edition(allowed values- 64), basic edition(allowed values- 64), enterprise with cloud
            - services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 64.
        type: int
    hybrid_rss_mode:
        description:
            - Toggles se hybrid only mode of operation in dpdk mode with rss configured;where-in each se datapath instance operates as an independent
            - standalonehybrid instance performing both dispatcher and proxy function.
            - Requires reboot.
            - Field introduced in 21.1.3.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    hypervisor:
        description:
            - Override default hypervisor.
            - Enum options - DEFAULT, VMWARE_ESX, KVM, VMWARE_VSAN, XEN.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
        type: str
    ignore_docker_mac_change:
        description:
            - Ignore docker mac change.
            - Field introduced in 21.1.3.
            - Allowed in enterprise edition with any value, essentials edition with any value, basic edition with any value, enterprise with cloud services
            - edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as True.
        type: bool
    ignore_rtt_threshold:
        description:
            - Ignore rtt samples if it is above threshold.
            - Field introduced in 17.1.6,17.2.2.
            - Unit is milliseconds.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 5000.
        type: int
    ingress_access_data:
        description:
            - Program se security group ingress rules to allow vip data access from remote cidr type.
            - Enum options - SG_INGRESS_ACCESS_NONE, SG_INGRESS_ACCESS_ALL, SG_INGRESS_ACCESS_VPC.
            - Field introduced in 17.1.5.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as SG_INGRESS_ACCESS_ALL.
        type: str
    ingress_access_mgmt:
        description:
            - Program se security group ingress rules to allow ssh/icmp management access from remote cidr type.
            - Enum options - SG_INGRESS_ACCESS_NONE, SG_INGRESS_ACCESS_ALL, SG_INGRESS_ACCESS_VPC.
            - Field introduced in 17.1.5.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as SG_INGRESS_ACCESS_ALL.
        type: str
    instance_flavor_info:
        description:
            - Additional information associated with instance_flavor.
            - Field introduced in 20.1.1.
            - Allowed in enterprise edition with any value, essentials edition with any value, basic edition with any value, enterprise with cloud services
            - edition.
        type: dict
    iptables:
        description:
            - Iptable rules.
            - Maximum of 128 items allowed.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: list
        elements: dict
    l7_conns_per_core:
        description:
            - Number of l7 connections that can be cached per core.
            - Field introduced in 21.1.1.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 16384.
        type: int
    l7_resvd_listen_conns_per_core:
        description:
            - Number of reserved l7 listener connections per core.
            - Field introduced in 21.1.1.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 256.
        type: int
    labels:
        description:
            - Labels associated with this se group.
            - Field introduced in 20.1.1.
            - Maximum of 1 items allowed.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: list
        elements: dict
    lbaction_num_requests_to_dispatch:
        description:
            - Number of requests to dispatch from the request.
            - Queue at a regular interval.
            - Field introduced in 21.1.1.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 4.
        type: int
    lbaction_rq_per_request_max_retries:
        description:
            - Maximum retries per request in the request queue.
            - Field introduced in 21.1.1.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 22.
        type: int
    least_load_core_selection:
        description:
            - Select core with least load for new flow.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as True.
        type: bool
    license_tier:
        description:
            - Specifies the license tier which would be used.
            - This field by default inherits the value from cloud.
            - Enum options - ENTERPRISE_16, ENTERPRISE, ENTERPRISE_18, BASIC, ESSENTIALS, ENTERPRISE_WITH_CLOUD_SERVICES.
            - Field introduced in 17.2.5.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: str
    log_agent_compress_logs:
        description:
            - Flag to indicate if log files are compressed upon full on the service engine.
            - Field introduced in 21.1.1.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as True.
        type: bool
    log_agent_debug_enabled:
        description:
            - Enable debug logs by default on service engine.
            - This includes all other debugging logs.
            - Debug logs can also be explcitly enabled from the cli shell.
            - Field introduced in 21.1.1.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    log_agent_file_sz_appl:
        description:
            - Maximum application log file size before rollover.
            - Field introduced in 21.1.1.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 4.
        type: int
    log_agent_file_sz_conn:
        description:
            - Maximum connection log file size before rollover.
            - Field introduced in 21.1.1.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 4.
        type: int
    log_agent_file_sz_debug:
        description:
            - Maximum debug log file size before rollover.
            - Field introduced in 21.1.1.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 4.
        type: int
    log_agent_file_sz_event:
        description:
            - Maximum event log file size before rollover.
            - Field introduced in 21.1.1.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 4.
        type: int
    log_agent_log_storage_min_sz:
        description:
            - Minimum storage allocated for logs irrespective of memory and cores.
            - Field introduced in 21.1.1.
            - Unit is mb.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 1024.
        type: int
    log_agent_max_concurrent_rsync:
        description:
            - Maximum concurrent rsync requests initiated from log-agent to the controller.
            - Field introduced in 21.1.1.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 1024.
        type: int
    log_agent_max_storage_excess_percent:
        description:
            - Excess percentage threshold of disk size to trigger cleanup of logs on the service engine.
            - Field introduced in 21.1.1.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 110.
        type: int
    log_agent_max_storage_ignore_percent:
        description:
            - Maximum storage on the disk not allocated for logs on the service engine.
            - Field introduced in 21.1.1.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 20.0.
        type: float
    log_agent_min_storage_per_vs:
        description:
            - Minimum storage allocated to any given virtualservice on the service engine.
            - Field introduced in 21.1.1.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 10.
        type: int
    log_agent_sleep_interval:
        description:
            - Internal timer to stall log-agent and prevent it from hogging cpu cycles on the service engine.
            - Field introduced in 21.1.1.
            - Unit is milliseconds.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 10.
        type: int
    log_agent_trace_enabled:
        description:
            - Enable trace logs by default on service engine.
            - Configuration operations are logged along with other important logs by service engine.
            - Field introduced in 21.1.1.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as True.
        type: bool
    log_agent_unknown_vs_timer:
        description:
            - Timeout to purge unknown virtual service logs from the service engine.
            - Field introduced in 21.1.1.
            - Unit is sec.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 1800.
        type: int
    log_disksz:
        description:
            - Maximum disk capacity (in mb) to be allocated to an se.
            - This is exclusively used for debug and log data.
            - Unit is mb.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 10000.
        type: int
    log_malloc_failure:
        description:
            - Se will log memory allocation related failure to the se_trace file, wherever available.
            - Field introduced in 20.1.2.
            - Allowed in enterprise edition with any value, essentials edition(allowed values- true), basic edition(allowed values- true), enterprise with
            - cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as True.
        type: bool
    log_message_max_file_list_size:
        description:
            - Maximum number of file names in a log message.
            - Field introduced in 21.1.1.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 64.
        type: int
    realtime_se_metrics:
        description:
            - Enable or deactivate real time se metrics.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: dict
    ha_mode:
        description:
            - High availability mode for all the virtual services using this service engine group.
            - Enum options - HA_MODE_SHARED_PAIR, HA_MODE_SHARED, HA_MODE_LEGACY_ACTIVE_STANDBY.
            - Allowed in enterprise edition with any value, essentials edition(allowed values- ha_mode_legacy_active_standby), basic edition(allowed values-
            - ha_mode_legacy_active_standby), enterprise with cloud services edition.
            - Special default for essentials edition is ha_mode_legacy_active_standby, basic edition is ha_mode_legacy_active_standby, enterprise is
            - ha_mode_shared.
            - Default value when not specified in API or module is interpreted by Avi Controller as HA_MODE_SHARED.
        type: str
    algo:
        description:
            - In compact placement, virtual services are placed on existing ses until max_vs_per_se limit is reached.
            - Enum options - PLACEMENT_ALGO_PACKED, PLACEMENT_ALGO_DISTRIBUTED.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as PLACEMENT_ALGO_PACKED.
        type: str
    max_vs_per_se:
        description:
            - Maximum number of virtual services that can be placed on a single service engine.
            - Allowed values are 1-1000.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 10.
        type: int
    self_se_election:
        description:
            - Enable ses to elect a primary amongst themselves in the absence of a connectivity to controller.
            - Field introduced in 18.1.2.
            - Allowed in enterprise edition with any value, essentials edition(allowed values- false), basic edition(allowed values- false), enterprise with
            - cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    max_se:
        description:
            - Maximum number of services engines in this group.
            - Allowed values are 0-1000.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 10.
        type: int
    extra_shared_config_memory:
        description:
            - Extra config memory to support large geo db configuration.
            - Field introduced in 17.1.1.
            - Unit is mb.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 0.
        type: int
    app_cache_percent:
        description:
            - A percent value of total se memory reserved for applicationcaching.
            - This is an se bootup property and requires se restart.requires se reboot.
            - Allowed values are 0 - 100.
            - Special values are 0- disable.
            - Field introduced in 18.2.3.
            - Unit is percent.
            - Allowed in enterprise edition with any value, essentials edition(allowed values- 0), basic edition(allowed values- 0), enterprise with cloud
            - services edition.
            - Special default for essentials edition is 0, basic edition is 0, enterprise is 10.
            - Default value when not specified in API or module is interpreted by Avi Controller as 10.
        type: int
    connection_memory_percentage:
        description:
            - Percentage of memory for connection state.
            - This will come at the expense of memory used for http in-memory cache.
            - Allowed values are 10-90.
            - Unit is percent.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 50.
        type: int
    license_type:
        description:
            - If no license type is specified then default license enforcement for the cloud type is chosen.
            - Enum options - LIC_BACKEND_SERVERS, LIC_SOCKETS, LIC_CORES, LIC_HOSTS, LIC_SE_BANDWIDTH, LIC_METERED_SE_BANDWIDTH.
            - Field introduced in 17.2.5.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: str
    per_app:
        description:
            - Per-app se mode is designed for deploying dedicated load balancers per app (vs).
            - In this mode, each se is limited to a max of 2 vss.
            - Vcpus in per-app ses count towards licensing usage at 25% rate.
            - Allowed in enterprise edition with any value, essentials edition(allowed values- false), basic edition(allowed values- false), enterprise with
            - cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    se_bandwidth_type:
        description:
            - Select the se bandwidth for the bandwidth license.
            - Enum options - SE_BANDWIDTH_UNLIMITED, SE_BANDWIDTH_25M, SE_BANDWIDTH_200M, SE_BANDWIDTH_1000M, SE_BANDWIDTH_10000M.
            - Field introduced in 17.2.5.
            - Allowed in enterprise edition with any value, essentials edition(allowed values- se_bandwidth_unlimited), basic edition(allowed values-
            - se_bandwidth_unlimited), enterprise with cloud services edition.
        type: str
    max_num_se_dps:
        description:
            - Configures the maximum number of se_dp processes that handles traffic.
            - If not configured, defaults to the number of cpus on the se.
            - If decreased, it will only take effect after se reboot.
            - Allowed values are 1-128.
            - Field introduced in 20.1.1.
            - Allowed in enterprise edition with any value, essentials edition(allowed values- 0), basic edition(allowed values- 0), enterprise with cloud
            - services edition.
        type: int
    use_hyperthreaded_cores:
        description:
            - Enables the use of hyper-threaded cores on se.
            - Requires se reboot.
            - Field introduced in 20.1.1.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as True.
        type: bool
    buffer_se:
        description:
            - Excess service engine capacity provisioned for ha failover.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 1.
        type: int
    max_scaleout_per_vs:
        description:
            - Maximum number of active service engines for the virtual service.
            - Allowed values are 1-64.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 4.
        type: int
    cpu_socket_affinity:
        description:
            - Allocate all the cpu cores for the service engine virtual machines  on the same cpu socket.
            - Applicable only for vcenter cloud.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    dedicated_dispatcher_core:
        description:
            - Dedicate the core that handles packet receive/transmit from the network to just the dispatching function.
            - Don't use it for tcp/ip and ssl functions.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: bool
    non_significant_log_throttle:
        description:
            - This setting limits the number of non-significant logs generated per second per core on this se.
            - Default is 100 logs per second.
            - Set it to zero (0) to deactivate throttling.
            - Field introduced in 17.1.3.
            - Unit is per_second.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 100.
        type: int
    significant_log_throttle:
        description:
            - This setting limits the number of significant logs generated per second per core on this se.
            - Default is 100 logs per second.
            - Set it to zero (0) to deactivate throttling.
            - Field introduced in 17.1.3.
            - Unit is per_second.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 100.
        type: int
    udf_log_throttle:
        description:
            - This setting limits the number of udf logs generated per second per core on this se.
            - Udf logs are generated due to the configured client log filters or the rules with logging enabled.
            - Default is 100 logs per second.
            - Set it to zero (0) to deactivate throttling.
            - Field introduced in 17.1.3.
            - Unit is per_second.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 100.
        type: int
    uuid:
        description:
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: str
    vcenter_clusters:
        description:
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: dict
    vcenter_datastore_mode:
        description:
            - Enum options - VCENTER_DATASTORE_ANY, VCENTER_DATASTORE_LOCAL, VCENTER_DATASTORE_SHARED.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as VCENTER_DATASTORE_ANY.
        type: str
    vcenter_datastores:
        description:
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: list
        elements: dict
    vcenter_datastores_include:
        description:
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    vcenter_folder:
        description:
            - Folder to place all the service engine virtual machines in vcenter.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as AviSeFolder.
        type: str
    vcenter_hosts:
        description:
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: dict
    vcenter_parking_vnic_pg:
        description:
            - Parking port group to be used by 9 vnics at the time of se creation.
            - Field introduced in 22.1.1.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
        type: str
    vcenters:
        description:
            - Vcenter information for scoping at host/cluster level.
            - Field introduced in 20.1.1.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: list
        elements: dict
    custom_tag:
        description:
            - Custom tag will be used to create the tags for se instance in aws.
            - Note this is not the same as the prefix for se name.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
        type: list
        elements: dict
    cloud_ref:
        description:
            - It is a reference to an object of type cloud.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: str
    se_name_prefix:
        description:
            - Prefix to use for virtual machine name of service engines.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as Avi.
        type: str
    accelerated_networking:
        description:
            - Enable accelerated networking option for azure se.
            - Accelerated networking enables single root i/o virtualization (sr-iov) to a se vm.
            - This improves networking performance.
            - Field introduced in 17.2.14,18.1.5,18.2.1.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: bool
    active_standby:
        description:
            - Service engines in active/standby mode for ha failover.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    instance_flavor:
        description:
            - Instance/flavor name for se instance.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: str
    se_deprovision_delay:
        description:
            - Duration to preserve unused service engine virtual machines before deleting them.
            - If traffic to a virtual service were to spike up abruptly, this se would still be available to be utilized again rather than creating a new se.
            - If this value is set to 0, controller will never delete any ses and administrator has to manually cleanup unused ses.
            - Allowed values are 0-525600.
            - Unit is min.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 120.
        type: int
    vcpus_per_se:
        description:
            - Number of vcpus for each of the service engine virtual machines.
            - Changes to this setting do not affect existing ses.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 1.
        type: int
    memory_per_se:
        description:
            - Amount of memory for each of the service engine virtual machines.
            - Changes to this setting do not affect existing ses.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 2048.
        type: int
    disk_per_se:
        description:
            - Amount of disk space for each of the service engine virtual machines.
            - Unit is gb.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 15.
        type: int
    cpu_reserve:
        description:
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    mem_reserve:
        description:
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as True.
        type: bool
    description:
        description:
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: str
    tenant_ref:
        description:
            - It is a reference to an object of type tenant.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: str
    gcp_config:
        description:
            - Google cloud platform, service engine group configuration.
            - Field introduced in 20.1.3.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
        type: dict
    markers:
        description:
            - List of labels to be used for granular rbac.
            - Field introduced in 20.1.7.
            - Allowed in enterprise edition with any value, essentials edition with any value, basic edition with any value, enterprise with cloud services
            - edition.
        type: list
        elements: dict
    max_concurrent_external_hm:
        description:
            - Maximum number of external health monitors that can run concurrently in a service engine.
            - This helps control the cpu and memory use by external health monitors.
            - Special values are 0- value will be internally calculated based on cpu and memory.
            - Field introduced in 18.2.7.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: int
    max_cpu_usage:
        description:
            - When cpu usage on an se exceeds this threshold, virtual services hosted on this se may be rebalanced to other ses to reduce load.
            - A new se may be created as part of this process.
            - Allowed values are 40-90.
            - Unit is percent.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 80.
        type: int
    max_memory_per_mempool:
        description:
            - Max bytes that can be allocated in a single mempool.
            - Field introduced in 18.1.5.
            - Unit is mb.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 64.
        type: int
    max_public_ips_per_lb:
        description:
            - Applicable to azure platform only.
            - Maximum number of public ips per azure lb.
            - Field introduced in 17.2.12, 18.1.2.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 30.
        type: int
    max_queues_per_vnic:
        description:
            - Maximum number of queues per vnic setting to '0' utilises all queues that are distributed across dispatcher cores.
            - Allowed values are 0,1,2,4,8,16.
            - Field introduced in 18.2.7, 20.1.1.
            - Allowed in enterprise edition with any value, essentials edition(allowed values- 1), basic edition(allowed values- 1), enterprise with cloud
            - services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 1.
        type: int
    max_rules_per_lb:
        description:
            - Applicable to azure platform only.
            - Maximum number of rules per azure lb.
            - Field introduced in 17.2.12, 18.1.2.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 150.
        type: int
    memory_for_config_update:
        description:
            - Indicates the percent of memory reserved for config updates.
            - Allowed values are 0-100.
            - Field introduced in 18.1.2.
            - Unit is percent.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 15.
        type: int
    mgmt_network_ref:
        description:
            - Management network to use for avi service engines.
            - It is a reference to an object of type network.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: str
    mgmt_subnet:
        description:
            - Management subnet to use for avi service engines.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: dict
    min_cpu_usage:
        description:
            - When cpu usage on an se falls below the minimum threshold, virtual services hosted on the se may be consolidated onto other underutilized ses.
            - After consolidation, unused service engines may then be eligible for deletion.
            - Allowed values are 20-60.
            - Unit is percent.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 30.
        type: int
    min_scaleout_per_vs:
        description:
            - Minimum number of active service engines for the virtual service.
            - Allowed values are 1-64.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 1.
        type: int
    min_se:
        description:
            - Minimum number of services engines in this group (relevant for se autorebalance only).
            - Allowed values are 0-1000.
            - Field introduced in 17.2.13,18.1.3,18.2.1.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 1.
        type: int
    minimum_connection_memory:
        description:
            - Indicates the percent of memory reserved for connections.
            - Allowed values are 0-100.
            - Field introduced in 18.1.2.
            - Unit is percent.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 20.
        type: int
    n_log_streaming_threads:
        description:
            - Number of threads to use for log streaming.
            - Allowed values are 1-100.
            - Field introduced in 17.2.12, 18.1.2.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 1.
        type: int
    ns_helper_deq_interval_msec:
        description:
            - Dequeue interval for receive queue from ns helper.
            - Allowed values are 1-1000.
            - Field introduced in 21.1.1.
            - Unit is milliseconds.
            - Allowed in enterprise edition with any value, essentials edition with any value, basic edition with any value, enterprise with cloud services
            - edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 20.
        type: int
    ntp_sync_fail_event:
        description:
            - Toggle se ntp synchronization failure events generation.
            - Disabled by default.
            - Field introduced in 22.1.2.
            - Allowed in enterprise edition with any value, essentials edition with any value, basic edition with any value, enterprise with cloud services
            - edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    ntp_sync_status_interval:
        description:
            - Configures the interval at which se synchronization status with ntp server(s) is verified.
            - A value of zero disables se ntp synchronization status validation.
            - Allowed values are 120-900.
            - Special values are 0- disable.
            - Field introduced in 22.1.2.
            - Unit is sec.
            - Allowed in enterprise edition with any value, essentials edition with any value, basic edition with any value, enterprise with cloud services
            - edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 0.
        type: int
    num_dispatcher_cores:
        description:
            - Number of dispatcher cores (0,1,2,4,8 or 16).
            - If set to 0, then number of dispatcher cores is deduced automatically.requires se reboot.
            - Allowed values are 0,1,2,4,8,16.
            - Field introduced in 17.2.12, 18.1.3, 18.2.1.
            - Allowed in enterprise edition with any value, essentials edition(allowed values- 0), basic edition(allowed values- 0), enterprise with cloud
            - services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 0.
        type: int
    num_dispatcher_queues:
        description:
            - Number of queues to each dispatcher.
            - Allowed values are 1-2.
            - Field introduced in 21.1.3.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 1.
        type: int
    objsync_config:
        description:
            - Configuration knobs for interse object distribution.
            - Field introduced in 20.1.3.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
        type: dict
    objsync_port:
        description:
            - Tcp port on se management interface for interse object distribution.
            - Supported only for externally managed security groups.
            - Not supported on full access deployments.
            - Requires se reboot.
            - Field introduced in 20.1.3.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 9001.
        type: int
    openstack_availability_zones:
        description:
            - Field introduced in 17.1.1.
            - Maximum of 5 items allowed.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: list
        elements: str
    openstack_mgmt_network_name:
        description:
            - Avi management network name.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: str
    openstack_mgmt_network_uuid:
        description:
            - Management network uuid.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: str
    os_reserved_memory:
        description:
            - Amount of extra memory to be reserved for use by the operating system on a service engine.
            - Unit is mb.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 0.
        type: int
    per_vs_admission_control:
        description:
            - Enable/disable per vs level admission control.enabling this feature will cause the connection and packet throttling on a particular vs that has
            - high packet buffer consumption.
            - Field introduced in 20.1.3.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    placement_mode:
        description:
            - If placement mode is 'auto', virtual services are automatically placed on service engines.
            - Enum options - PLACEMENT_MODE_AUTO.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as PLACEMENT_MODE_AUTO.
        type: str
    reboot_on_panic:
        description:
            - Reboot the vm or host on kernel panic.
            - Field introduced in 18.2.5.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as True.
        type: bool
    replay_vrf_routes_interval:
        description:
            - Routes in vrf are replayed at the specified interval.
            - This should be increased if there are large number of routes.
            - Allowed values are 0-3000.
            - Field introduced in 22.1.3.
            - Unit is milliseconds.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 1000.
        type: int
    resync_time_interval:
        description:
            - Time interval to re-sync se's time with wall clock time.
            - Allowed values are 8-600000.
            - Field introduced in 20.1.1.
            - Unit is milliseconds.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 65536.
        type: int
    sdb_flush_interval:
        description:
            - Sdb pipeline flush interval.
            - Allowed values are 1-10000.
            - Field introduced in 21.1.1.
            - Unit is milliseconds.
            - Allowed in enterprise edition with any value, essentials edition with any value, basic edition with any value, enterprise with cloud services
            - edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 100.
        type: int
    sdb_pipeline_size:
        description:
            - Sdb pipeline size.
            - Allowed values are 1-10000.
            - Field introduced in 21.1.1.
            - Allowed in enterprise edition with any value, essentials edition with any value, basic edition with any value, enterprise with cloud services
            - edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 100.
        type: int
    sdb_scan_count:
        description:
            - Sdb scan count.
            - Allowed values are 1-1000.
            - Field introduced in 21.1.1.
            - Allowed in enterprise edition with any value, essentials edition with any value, basic edition with any value, enterprise with cloud services
            - edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 1000.
        type: int
    se_delayed_flow_delete:
        description:
            - Delay the cleanup of flowtable entry.
            - To be used under surveillance of avi support.
            - Field introduced in 20.1.2.
            - Allowed in enterprise edition with any value, essentials edition(allowed values- true), basic edition(allowed values- true), enterprise with
            - cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as True.
        type: bool
    se_dos_profile:
        description:
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: dict
    se_dp_hm_drops:
        description:
            - Internal only.
            - Used to simulate se - se hb failure.
            - Field introduced in 20.1.3.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 0.
        type: int
    se_dp_if_state_poll_interval:
        description:
            - Number of jiffies between polling interface state.
            - Field introduced in 21.1.3.
            - Allowed in enterprise edition with any value, essentials edition with any value, basic edition with any value, enterprise with cloud services
            - edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 10.
        type: int
    se_dp_isolation:
        description:
            - Toggle support to run se datapath instances in isolation on exclusive cpus.
            - This improves latency and performance.
            - However, this could reduce the total number of se_dp instances created on that se instance.
            - Supported for >= 8 cpus.
            - Requires se reboot.
            - Field introduced in 20.1.4.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    se_dp_isolation_num_non_dp_cpus:
        description:
            - Number of cpus for non se-dp tasks in se datapath isolation mode.
            - Translates total cpus minus 'num_non_dp_cpus' for datapath use.
            - It is recommended to reserve an even number of cpus for hyper-threaded processors.
            - Requires se reboot.
            - Allowed values are 1-8.
            - Special values are 0- auto.
            - Field introduced in 20.1.4.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 0.
        type: int
    se_dp_log_nf_enqueue_percent:
        description:
            - Internal buffer full indicator on the service engine beyond which the unfiltered logs are abandoned.
            - Field introduced in 21.1.1.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 70.
        type: int
    se_dp_log_udf_enqueue_percent:
        description:
            - Internal buffer full indicator on the service engine beyond which the user filtered logs are abandoned.
            - Field introduced in 21.1.1.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 90.
        type: int
    se_dpdk_pmd:
        description:
            - Determines if dpdk pool mode driver should be used or not   0  automatically determine based on hypervisor/nic type 1  unconditionally use dpdk
            - poll mode driver 2  don't use dpdk poll mode driver.requires se reboot.
            - Allowed values are 0-2.
            - Field introduced in 18.1.3.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 0.
        type: int
    se_emulated_cores:
        description:
            - Use this to emulate more/less cpus than is actually available.
            - One datapath process is started for each core.
            - Field introduced in 21.1.3.
            - Allowed in enterprise edition with any value, essentials edition(allowed values- 0), basic edition(allowed values- 0), enterprise with cloud
            - services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 0.
        type: int
    se_hyperthreaded_mode:
        description:
            - Controls the distribution of se data path processes on cpus which support hyper-threading.
            - Requires hyper-threading to be enabled at host level.
            - Requires se reboot.
            - For more details please refer to se placement kb.
            - Enum options - SE_CPU_HT_AUTO, SE_CPU_HT_SPARSE_DISPATCHER_PRIORITY, SE_CPU_HT_SPARSE_PROXY_PRIORITY, SE_CPU_HT_PACKED_CORES.
            - Field introduced in 20.1.1.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as SE_CPU_HT_AUTO.
        type: str
    se_lro:
        description:
            - Enable or disable large receive optimization for vnics.supported on vmxnet3.requires se reboot.
            - Field introduced in 18.2.5.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: bool
    se_mtu:
        description:
            - Mtu for the vnics of ses in the se group.
            - Allowed values are 512-9000.
            - Field introduced in 18.2.8, 20.1.1.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: int
    se_use_dpdk:
        description:
            - Determines if dpdk library should be used or not   0  automatically determine based on hypervisor type 1  use dpdk if pcap is not enabled 2
            - don't use dpdk.
            - Allowed values are 0-2.
            - Field introduced in 18.1.3.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 0.
        type: int
    use_dp_util_for_scaleout:
        description:
            - If enabled, the datapath cpu utilization is consulted by the auto scale-out logic.
            - Field introduced in 22.1.3.
            - Allowed in enterprise edition with any value, essentials edition with any value, basic edition with any value, enterprise with cloud services
            - edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    use_objsync:
        description:
            - Enable interse objsyc distribution framework.
            - Field introduced in 20.1.3.
            - Allowed in enterprise edition with any value, essentials edition with any value, basic edition with any value, enterprise with cloud services
            - edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as True.
        type: bool
    use_standard_alb:
        description:
            - Use standard sku azure load balancer.
            - By default cloud level flag is set.
            - If not set, it inherits/uses the use_standard_alb flag from the cloud.
            - Field introduced in 18.2.3.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: bool
    user_agent_cache_config:
        description:
            - Configuration for user-agent cache used in bot management.
            - Field introduced in 21.1.1.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
        type: dict
    vs_host_redundancy:
        description:
            - Ensure primary and secondary service engines are deployed on different physical hosts.
            - Allowed in enterprise edition with any value, essentials edition(allowed values- true), basic edition(allowed values- true), enterprise with
            - cloud services edition.
            - Special default for essentials edition is true, basic edition is true, enterprise is true.
            - Default value when not specified in API or module is interpreted by Avi Controller as True.
        type: bool
    vs_scalein_timeout:
        description:
            - Time to wait for the scaled in se to drain existing flows before marking the scalein done.
            - Unit is sec.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 30.
        type: int
    vs_scalein_timeout_for_upgrade:
        description:
            - During se upgrade, time to wait for the scaled-in se to drain existing flows before marking the scalein done.
            - Unit is sec.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 30.
        type: int
    vs_scaleout_timeout:
        description:
            - Time to wait for the scaled out se to become ready before marking the scaleout done.
            - Unit is sec.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 600.
        type: int
    vs_se_scaleout_additional_wait_time:
        description:
            - Wait time for sending scaleout ready notification after virtual service is marked up.
            - In certain deployments, there may be an additional delay to accept traffic.
            - For example, for bgp, some time is needed for route advertisement.
            - Allowed values are 0-300.
            - Field introduced in 18.1.5,18.2.1.
            - Unit is sec.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 0.
        type: int
    vs_se_scaleout_ready_timeout:
        description:
            - Timeout in seconds for service engine to sendscaleout ready notification of a virtual service.
            - Allowed values are 0-90.
            - Field introduced in 18.1.5,18.2.1.
            - Unit is sec.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 60.
        type: int
    vs_switchover_timeout:
        description:
            - During se upgrade in a legacy active/standby segroup, time to wait for the new primary se to accept flows before marking the switchover done.
            - Field introduced in 17.2.13,18.1.4,18.2.1.
            - Unit is sec.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 300.
        type: int
extends_documentation_fragment:
    - vmware.alb.avi
'''

EXAMPLES = \
    """
- hosts: localhost
  collections:
    - vmware.alb
  vars:
    avi_credentials:
      username: "{{ username }}"
      password: "{{ password }}"
      controller: "{{ controller }}"
      api_version: "{{ api_version }}"
  tasks:
    - name: Example to create ServiceEngineGroup object
      vmware.alb.avi_serviceenginegroup:
        avi_credentials: "{{ avi_credentials }}"
        state: present
        name: sample_serviceenginegroup
"""
RETURN = \
    '''
obj:
    description: ServiceEngineGroup (api/serviceenginegroup) object
    returned: success, changed
    type: dict
'''

from ansible.module_utils.basic import AnsibleModule
try:
    from ansible_collections.vmware.alb.plugins.module_utils.utils.ansible_utils import (
        avi_common_argument_spec, avi_ansible_api, ansible_return)
    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False


def main():
    argument_specs = dict(
        state=dict(default='present', choices=['absent', 'present']),
        name=dict(type='str', required=True),
        uuid=dict(type='str'),
        avi_api_update_method=dict(default='put', choices=['put',
                                   'patch']),
        avi_api_patch_op=dict(choices=['add', 'replace', 'delete',
                              'remove']),
        avi_patch_path=dict(type='str'),
        avi_patch_value=dict(type='str'),
        aggressive_failure_detection=dict(type='bool'),
        allow_burst=dict(type='bool'),
        app_cache_threshold=dict(type='int'),
        app_learning_memory_percent=dict(type='int'),
        archive_shm_limit=dict(type='int'),
        async_ssl=dict(type='bool'),
        async_ssl_threads=dict(type='int'),
        auto_rebalance=dict(type='bool'),
        auto_rebalance_capacity_per_se=dict(type='list', elements='int'),
        auto_rebalance_criteria=dict(type='list', elements='str'),
        auto_rebalance_interval=dict(type='int'),
        auto_redistribute_active_standby_load=dict(type='bool'),
        availability_zone_refs=dict(type='list', elements='str'),
        baremetal_dispatcher_handles_flows=dict(type='bool'),
        bgp_peer_monitor_failover_enabled=dict(type='bool'),
        bgp_state_update_interval=dict(type='int'),
        compress_ip_rules_for_each_ns_subnet=dict(type='bool'),
        config_debugs_on_all_cores=dict(type='bool'),
        configpb_attributes=dict(type='dict'),
        core_shm_app_cache=dict(type='bool'),
        core_shm_app_learning=dict(type='bool'),
        custom_securitygroups_data=dict(type='list', elements='str'),
        custom_securitygroups_mgmt=dict(type='list', elements='str'),
        data_network_id=dict(type='str'),
        datascript_timeout=dict(type='int'),
        deactivate_ipv6_discovery=dict(type='bool'),
        deactivate_kni_filtering_at_dispatcher=dict(type='bool'),
        disable_avi_securitygroups=dict(type='bool'),
        disable_csum_offloads=dict(type='bool'),
        disable_flow_probes=dict(type='bool'),
        disable_gro=dict(type='bool'),
        disable_se_memory_check=dict(type='bool'),
        disable_tso=dict(type='bool'),
        distribute_load_active_standby=dict(type='bool'),
        distribute_queues=dict(type='bool'),
        distribute_vnics=dict(type='bool'),
        downstream_send_timeout=dict(type='int'),
        dp_aggressive_deq_interval_msec=dict(type='int'),
        dp_aggressive_enq_interval_msec=dict(type='int'),
        dp_aggressive_hb_frequency=dict(type='int'),
        dp_aggressive_hb_timeout_count=dict(type='int'),
        dp_deq_interval_msec=dict(type='int'),
        dp_enq_interval_msec=dict(type='int'),
        dp_hb_frequency=dict(type='int'),
        dp_hb_timeout_count=dict(type='int'),
        dpdk_gro_timeout_interval=dict(type='int'),
        enable_gratarp_permanent=dict(type='bool'),
        enable_hsm_log=dict(type='bool'),
        enable_hsm_priming=dict(type='bool'),
        enable_multi_lb=dict(type='bool'),
        enable_pcap_tx_ring=dict(type='bool'),
        ephemeral_portrange_end=dict(type='int'),
        ephemeral_portrange_start=dict(type='int'),
        extra_config_multiplier=dict(type='float'),
        flow_table_new_syn_max_entries=dict(type='int'),
        free_list_size=dict(type='int'),
        gratarp_permanent_periodicity=dict(type='int'),
        grpc_channel_connect_timeout=dict(type='int'),
        handle_per_pkt_attack=dict(type='bool'),
        hardwaresecuritymodulegroup_ref=dict(type='str'),
        heap_minimum_config_memory=dict(type='int'),
        hm_on_standby=dict(type='bool'),
        host_attribute_key=dict(type='str'),
        host_attribute_value=dict(type='str'),
        host_gateway_monitor=dict(type='bool'),
        http_rum_console_log=dict(type='bool'),
        http_rum_min_content_length=dict(type='int'),
        hybrid_rss_mode=dict(type='bool'),
        hypervisor=dict(type='str'),
        ignore_docker_mac_change=dict(type='bool'),
        ignore_rtt_threshold=dict(type='int'),
        ingress_access_data=dict(type='str'),
        ingress_access_mgmt=dict(type='str'),
        instance_flavor_info=dict(type='dict'),
        iptables=dict(type='list', elements='dict'),
        l7_conns_per_core=dict(type='int'),
        l7_resvd_listen_conns_per_core=dict(type='int'),
        labels=dict(type='list', elements='dict'),
        lbaction_num_requests_to_dispatch=dict(type='int'),
        lbaction_rq_per_request_max_retries=dict(type='int'),
        least_load_core_selection=dict(type='bool'),
        license_tier=dict(type='str'),
        log_agent_compress_logs=dict(type='bool'),
        log_agent_debug_enabled=dict(type='bool'),
        log_agent_file_sz_appl=dict(type='int'),
        log_agent_file_sz_conn=dict(type='int'),
        log_agent_file_sz_debug=dict(type='int'),
        log_agent_file_sz_event=dict(type='int'),
        log_agent_log_storage_min_sz=dict(type='int'),
        log_agent_max_concurrent_rsync=dict(type='int'),
        log_agent_max_storage_excess_percent=dict(type='int'),
        log_agent_max_storage_ignore_percent=dict(type='float'),
        log_agent_min_storage_per_vs=dict(type='int'),
        log_agent_sleep_interval=dict(type='int'),
        log_agent_trace_enabled=dict(type='bool'),
        log_agent_unknown_vs_timer=dict(type='int'),
        log_disksz=dict(type='int'),
        log_malloc_failure=dict(type='bool'),
        log_message_max_file_list_size=dict(type='int'),
        realtime_se_metrics=dict(type='dict'),
        ha_mode=dict(type='str'),
        algo=dict(type='str'),
        max_vs_per_se=dict(type='int'),
        self_se_election=dict(type='bool'),
        max_se=dict(type='int'),
        extra_shared_config_memory=dict(type='int'),
        app_cache_percent=dict(type='int'),
        connection_memory_percentage=dict(type='int'),
        license_type=dict(type='str'),
        per_app=dict(type='bool'),
        se_bandwidth_type=dict(type='str'),
        max_num_se_dps=dict(type='int'),
        use_hyperthreaded_cores=dict(type='bool'),
        buffer_se=dict(type='int'),
        max_scaleout_per_vs=dict(type='int'),
        cpu_socket_affinity=dict(type='bool'),
        dedicated_dispatcher_core=dict(type='bool'),
        description=dict(type='str'),
        significant_log_throttle=dict(type='int'),
        udf_log_throttle=dict(type='int'),
        non_significant_log_throttle=dict(type='int'),
        vcenter_clusters=dict(type='dict'),
        vcenter_datastore_mode=dict(type='str'),
        vcenter_datastores=dict(type='list', elements='dict'),
        vcenter_datastores_include=dict(type='bool'),
        vcenter_folder=dict(type='str'),
        vcenter_hosts=dict(type='dict'),
        vcenter_parking_vnic_pg=dict(type='str'),
        vcenters=dict(type='list', elements='dict'),
        vcpus_per_se=dict(type='int'),
        custom_tag=dict(type='list', elements='dict'),
        cloud_ref=dict(type='str'),
        se_name_prefix=dict(type='str'),
        accelerated_networking=dict(type='bool'),
        active_standby=dict(type='bool'),
        instance_flavor=dict(type='str'),
        se_deprovision_delay=dict(type='int'),
        memory_per_se=dict(type='int'),
        disk_per_se=dict(type='int'),
        cpu_reserve=dict(type='bool'),
        mem_reserve=dict(type='bool'),
        tenant_ref=dict(type='str'),
        gcp_config=dict(type='dict'),
        markers=dict(type='list', elements='dict'),
        max_concurrent_external_hm=dict(type='int'),
        max_cpu_usage=dict(type='int'),
        max_memory_per_mempool=dict(type='int'),
        max_public_ips_per_lb=dict(type='int'),
        max_queues_per_vnic=dict(type='int'),
        max_rules_per_lb=dict(type='int'),
        memory_for_config_update=dict(type='int'),
        mgmt_network_ref=dict(type='str'),
        mgmt_subnet=dict(type='dict'),
        min_cpu_usage=dict(type='int'),
        min_scaleout_per_vs=dict(type='int'),
        min_se=dict(type='int'),
        minimum_connection_memory=dict(type='int'),
        n_log_streaming_threads=dict(type='int'),
        ns_helper_deq_interval_msec=dict(type='int'),
        ntp_sync_fail_event=dict(type='bool'),
        ntp_sync_status_interval=dict(type='int'),
        num_dispatcher_cores=dict(type='int'),
        num_dispatcher_queues=dict(type='int'),
        objsync_config=dict(type='dict'),
        objsync_port=dict(type='int'),
        openstack_availability_zones=dict(type='list', elements='str'),
        openstack_mgmt_network_name=dict(type='str'),
        openstack_mgmt_network_uuid=dict(type='str'),
        os_reserved_memory=dict(type='int'),
        per_vs_admission_control=dict(type='bool'),
        placement_mode=dict(type='str'),
        reboot_on_panic=dict(type='bool'),
        replay_vrf_routes_interval=dict(type='int'),
        resync_time_interval=dict(type='int'),
        sdb_flush_interval=dict(type='int'),
        sdb_pipeline_size=dict(type='int'),
        sdb_scan_count=dict(type='int'),
        se_delayed_flow_delete=dict(type='bool'),
        se_dos_profile=dict(type='dict'),
        se_dp_hm_drops=dict(type='int'),
        se_dp_if_state_poll_interval=dict(type='int'),
        se_dp_isolation=dict(type='bool'),
        se_dp_isolation_num_non_dp_cpus=dict(type='int'),
        se_dp_log_nf_enqueue_percent=dict(type='int'),
        se_dp_log_udf_enqueue_percent=dict(type='int'),
        se_dpdk_pmd=dict(type='int'),
        se_emulated_cores=dict(type='int'),
        se_hyperthreaded_mode=dict(type='str'),
        se_lro=dict(type='bool'),
        se_mtu=dict(type='int'),
        se_use_dpdk=dict(type='int'),
        use_dp_util_for_scaleout=dict(type='bool'),
        use_objsync=dict(type='bool'),
        use_standard_alb=dict(type='bool'),
        user_agent_cache_config=dict(type='dict'),
        vs_host_redundancy=dict(type='bool'),
        vs_scalein_timeout=dict(type='int'),
        vs_scalein_timeout_for_upgrade=dict(type='int'),
        vs_scaleout_timeout=dict(type='int'),
        vs_se_scaleout_additional_wait_time=dict(type='int'),
        vs_se_scaleout_ready_timeout=dict(type='int'),
        vs_switchover_timeout=dict(type='int'),
    )
    argument_specs.update(avi_common_argument_spec())
    module = AnsibleModule(argument_spec=argument_specs,
                           supports_check_mode=True)
    if not HAS_REQUESTS:
        return module.fail_json(msg=(
            'Python requests package is not installed. '
            'For installation instructions, visit https://pypi.org/project/requests.'))
    return avi_ansible_api(module, 'serviceenginegroup', set([]))


if __name__ == '__main__':
    main()
