#!/usr/bin/python
# -*- coding: utf-8 -*-

# module_check: supported

# Copyright 2021 VMware, Inc. All rights reserved. VMware Confidential
# SPDX-License-Identifier: Apache License 2.0
from __future__ import absolute_import, division, print_function

__metaclass__ = type
ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}
DOCUMENTATION = """
---
module: avi_serviceenginegroup_advanced
author: Gaurav Rastogi (@grastogi23) <grastogi@avinetworks.com>
short_description: Module for setup of ServiceEngineGroup Avi RESTful Object
description:
    - This module is used to configure ServiceEngineGroup object's advanced features
options:
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
    name:
        description:
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        required: true
        type: str
    configpb_attributes:
        description:
            - Protobuf versioning for config pbs.
            - Field introduced in 21.1.1.
            - Allowed in enterprise edition with any value, essentials edition with any value, basic edition with any value, enterprise with cloud services
            - edition.
        type: dict
    kni_allowed_server_ports:
        description:
            - Port ranges for any servers running in inband linuxserver clouds.
            - Field introduced in 21.1.3.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
        type: list
        elements: dict
    max_skb_frags:
        description:
            - Maximum of number of 4 kb pages allocated to the linux kernel gro subsystem for packet coalescing.
            - This parameter is limited to supported kernels only.
            - Requires se reboot.
            - Allowed values are 1-17.
            - Field introduced in 21.1.3.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 17.
        type: int
    netlink_poller_threads:
        description:
            - Number of threads to poll for netlink messages excluding the thread for default namespace.
            - Requires se reboot.
            - Allowed values are 1-32.
            - Field introduced in 21.1.1.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 2.
        type: int
    netlink_sock_buf_size:
        description:
            - Socket buffer size for the netlink sockets.
            - Requires se reboot.
            - Allowed values are 1-128.
            - Field introduced in 21.1.1.
            - Unit is mega_bytes.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 4.
        type: int
    ngx_free_connection_stack:
        description:
            - Free the connection stack.
            - Field introduced in 21.1.1.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    num_flow_cores_sum_changes_to_ignore:
        description:
            - Number of changes in num flow cores sum to ignore.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 8.
        type: int
    pcap_tx_mode:
        description:
            - Determines the pcap transmit mode of operation.
            - Requires se reboot.
            - Enum options - PCAP_TX_AUTO, PCAP_TX_SOCKET, PCAP_TX_RING.
            - Field introduced in 18.2.8, 20.1.1.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as PCAP_TX_AUTO.
        type: str
    pcap_tx_ring_rd_balancing_factor:
        description:
            - In pcap mode, reserve a configured portion of tx ring resources for itself and the remaining portion for the rx ring to achieve better balance in
            - terms of queue depth.
            - Requires se reboot.
            - Allowed values are 10-100.
            - Field introduced in 20.1.3.
            - Unit is percent.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 10.
        type: int
    se_dp_max_hb_version:
        description:
            - The highest supported se-se heartbeat protocol version.
            - This version is reported by secondary se to primary se in heartbeat response messages.
            - Allowed values are 1-3.
            - Field introduced in 20.1.1.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 3.
        type: int
    se_dp_vnic_queue_stall_event_sleep:
        description:
            - Time (in seconds) service engine waits for after generating a vnic transmit queue stall event before resetting thenic.
            - Field introduced in 18.2.5.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 0.
        type: int
    se_dp_vnic_queue_stall_threshold:
        description:
            - Number of consecutive transmit failures to look for before generating a vnic transmit queue stall event.
            - Field introduced in 18.2.5.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 2000.
        type: int
    se_dp_vnic_queue_stall_timeout:
        description:
            - Time (in milliseconds) to wait for network/nic recovery on detecting a transmit queue stall after which service engine resets the nic.
            - Field introduced in 18.2.5.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 10000.
        type: int
    se_dp_vnic_restart_on_queue_stall_count:
        description:
            - Number of consecutive transmit queue stall events in se_dp_vnic_stall_se_restart_window to look for before restarting se.
            - Field introduced in 18.2.5.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 3.
        type: int
    se_dp_vnic_stall_se_restart_window:
        description:
            - Window of time (in seconds) during which se_dp_vnic_restart_on_queue_stall_count number of consecutive stalls results in a se restart.
            - Field introduced in 18.2.5.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 3600.
        type: int
    se_dump_core_on_assert:
        description:
            - Enable core dump on assert.
            - Field introduced in 21.1.3.
            - Allowed in enterprise edition with any value, essentials edition with any value, basic edition with any value, enterprise with cloud services
            - edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    se_flow_probe_retries:
        description:
            - Flow probe retry count if no replies are received.requires se reboot.
            - Allowed values are 0-5.
            - Field introduced in 18.1.4, 18.2.1.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 2.
        type: int
    se_flow_probe_retry_timer:
        description:
            - Timeout in milliseconds for flow probe retries.requires se reboot.
            - Allowed values are 20-50.
            - Field introduced in 18.2.5.
            - Unit is milliseconds.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 40.
        type: int
    se_group_analytics_policy:
        description:
            - Analytics policy for serviceenginegroup.
            - Field introduced in 20.1.3.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
        type: dict
    se_ip_encap_ipc:
        description:
            - Determines if se-se ipc messages are encapsulated in an ip header       0        automatically determine based on hypervisor type    1        use
            - ip encap unconditionally    ~[0,1]   don't use ip encaprequires se reboot.
            - Field introduced in 20.1.3.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 0.
        type: int
    se_kni_burst_factor:
        description:
            - This knob controls the resource availability and burst size used between se datapath and kni.
            - This helps in minimising packet drops when there is higher kni traffic (non-vip traffic from and to linux).
            - The factor takes the following values      0-default.
            - 1-doubles the burst size and kni resources.
            - 2-quadruples the burst size and kni resources.
            - Allowed values are 0-2.
            - Field introduced in 18.2.6.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 0.
        type: int
    se_l3_encap_ipc:
        description:
            - Determines if se-se ipc messages use se interface ip instead of vip        0        automatically determine based on hypervisor type    1
            - use se interface ip unconditionally    ~[0,1]   don't use se interface iprequires se reboot.
            - Field introduced in 20.1.3.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 0.
        type: int
    se_log_buffer_app_blocking_dequeue:
        description:
            - Internal flag that blocks dataplane until all application logs are flushed to log-agent process.
            - Field introduced in 21.1.1.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    se_log_buffer_conn_blocking_dequeue:
        description:
            - Internal flag that blocks dataplane until all connection logs are flushed to log-agent process.
            - Field introduced in 21.1.1.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    se_log_buffer_events_blocking_dequeue:
        description:
            - Internal flag that blocks dataplane until all outstanding events are flushed to log-agent process.
            - Field introduced in 21.1.1.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as True.
        type: bool
    se_mp_ring_retry_count:
        description:
            - The retry count for the multi-producer enqueue before yielding the cpu.
            - To be used under surveillance of avi support.
            - Field introduced in 20.1.3.
            - Allowed in enterprise edition with any value, essentials edition(allowed values- 500), basic edition(allowed values- 500), enterprise with cloud
            - services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 500.
        type: int
    se_packet_buffer_max:
        description:
            - Internal use only.
            - Used to artificially reduce the available number of packet buffers.
            - Field introduced in 21.1.3.
            - Allowed in enterprise edition with any value, essentials edition with any value, basic edition with any value, enterprise with cloud services
            - edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 0.
        type: int
    se_pcap_lookahead:
        description:
            - Enables lookahead mode of packet receive in pcap mode.
            - Introduced to overcome an issue with hv_netvsc driver.
            - Lookahead mode attempts to ensure that application and kernel's view of the receive rings are consistent.
            - Field introduced in 18.2.3.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    se_pcap_pkt_count:
        description:
            - Max number of packets the pcap interface can hold and if the value is 0 the optimum value will be chosen.
            - The optimum value will be chosen based on se-memory, cloud type and number of interfaces.requires se reboot.
            - Field introduced in 18.2.5.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 0.
        type: int
    se_pcap_pkt_sz:
        description:
            - Max size of each packet in the pcap interface.
            - Requires se reboot.
            - Field introduced in 18.2.5.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 69632.
        type: int
    se_pcap_qdisc_bypass:
        description:
            - Bypass the kernel's traffic control layer, to deliver packets directly to the driver.
            - Enabling this feature results in egress packets not being captured in host tcpdump.
            - Note   brief packet reordering or loss may occur upon toggle.
            - Field introduced in 18.2.6.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as True.
        type: bool
    se_pcap_reinit_frequency:
        description:
            - Frequency in seconds at which periodically a pcap reinit check is triggered.
            - May be used in conjunction with the configuration pcap_reinit_threshold.
            - (valid range   15 mins - 12 hours, 0 - disables).
            - Allowed values are 900-43200.
            - Special values are 0- disable.
            - Field introduced in 17.2.13, 18.1.3, 18.2.1.
            - Unit is sec.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 0.
        type: int
    se_pcap_reinit_threshold:
        description:
            - Threshold for input packet receive errors in pcap mode exceeding which a pcap reinit is triggered.
            - If not set, an unconditional reinit is performed.
            - This value is checked every pcap_reinit_frequency interval.
            - Field introduced in 17.2.13, 18.1.3, 18.2.1.
            - Unit is metric_count.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 0.
        type: int
    se_probe_port:
        description:
            - Tcp port on se where echo service will be run.
            - Field introduced in 17.2.2.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 7.
        type: int
    se_rl_prop:
        description:
            - Rate limiter properties.
            - Field introduced in 20.1.1.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: dict
    se_rum_sampling_nav_interval:
        description:
            - Minimum time to wait on server between taking sampleswhen sampling the navigation timing data from the end user client.
            - Field introduced in 18.2.6.
            - Unit is sec.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 1.
        type: int
    se_rum_sampling_nav_percent:
        description:
            - Percentage of navigation timing data from the end user client, used for sampling to get client insights.
            - Field introduced in 18.2.6.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 1.
        type: int
    se_rum_sampling_res_interval:
        description:
            - Minimum time to wait on server between taking sampleswhen sampling the resource timing data from the end user client.
            - Field introduced in 18.2.6.
            - Unit is sec.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 2.
        type: int
    se_rum_sampling_res_percent:
        description:
            - Percentage of resource timing data from the end user client used for sampling to get client insight.
            - Field introduced in 18.2.6.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 100.
        type: int
    se_sb_dedicated_core:
        description:
            - Sideband traffic will be handled by a dedicated core.requires se reboot.
            - Field introduced in 16.5.2, 17.1.9, 17.2.3.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    se_sb_threads:
        description:
            - Number of sideband threads per se.requires se reboot.
            - Allowed values are 1-128.
            - Field introduced in 16.5.2, 17.1.9, 17.2.3.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 1.
        type: int
    se_thread_multiplier:
        description:
            - Multiplier for se threads based on vcpu.
            - Allowed values are 1-10.
            - Allowed in enterprise edition with any value, essentials edition(allowed values- 1), basic edition(allowed values- 1), enterprise with cloud
            - services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 1.
        type: int
    se_time_tracker_props:
        description:
            - Time tracker properties for latency audit.
            - Field introduced in 22.1.1.
            - Allowed in enterprise edition with any value, essentials edition with any value, basic edition with any value, enterprise with cloud services
            - edition.
        type: dict
    se_tracert_port_range:
        description:
            - Traceroute port range.
            - Field introduced in 17.2.8.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: dict
    se_tunnel_mode:
        description:
            - Determines if direct secondary return (dsr) from secondary se is active or not  0  automatically determine based on hypervisor type.
            - 1  enable tunnel mode - dsr is unconditionally disabled.
            - 2  disable tunnel mode - dsr is unconditionally enabled.
            - Tunnel mode can be enabled or disabled at run-time.
            - Allowed values are 0-2.
            - Field introduced in 17.1.1.
            - Allowed in enterprise edition with any value, essentials edition(allowed values- 0), basic edition(allowed values- 0), enterprise with cloud
            - services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 0.
        type: int
    se_tunnel_udp_port:
        description:
            - Udp port for tunneled packets from secondary to primary se in docker bridge mode.requires se reboot.
            - Field introduced in 17.1.3.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 1550.
        type: int
    se_tx_batch_size:
        description:
            - Number of packets to batch for transmit to the nic.
            - Requires se reboot.
            - Field introduced in 18.2.5.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 64.
        type: int
    se_txq_threshold:
        description:
            - Once the tx queue of the dispatcher reaches this threshold, hardware queues are not polled for further packets.
            - To be used under surveillance of avi support.
            - Allowed values are 512-32768.
            - Field introduced in 20.1.2.
            - Allowed in enterprise edition with any value, essentials edition(allowed values- 2048), basic edition(allowed values- 2048), enterprise with
            - cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 2048.
        type: int
    se_udp_encap_ipc:
        description:
            - Determines if se-se ipc messages are encapsulated in a udp header  0  automatically determine based on hypervisor type.
            - 1  use udp encap unconditionally.requires se reboot.
            - Allowed values are 0-1.
            - Field introduced in 17.1.2.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 0.
        type: int
    se_vnic_tx_sw_queue_flush_frequency:
        description:
            - Configure the frequency in milliseconds of software transmit spillover queue flush when enabled.
            - This is necessary to flush any packets in the spillover queue in the absence of a packet transmit in the normal course of operation.
            - Allowed values are 50-500.
            - Special values are 0- disable.
            - Field introduced in 20.1.1.
            - Unit is milliseconds.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 0.
        type: int
    se_vnic_tx_sw_queue_size:
        description:
            - Configure the size of software transmit spillover queue when enabled.
            - Requires se reboot.
            - Allowed values are 128-2048.
            - Field introduced in 20.1.1.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 256.
        type: int
    se_vs_hb_max_pkts_in_batch:
        description:
            - Maximum number of aggregated vs heartbeat packets to send in a batch.
            - Allowed values are 1-256.
            - Field introduced in 17.1.1.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 64.
        type: int
    se_vs_hb_max_vs_in_pkt:
        description:
            - Maximum number of virtualservices for which heartbeat messages are aggregated in one packet.
            - Allowed values are 1-1024.
            - Field introduced in 17.1.1.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 256.
        type: int
    send_se_ready_timeout:
        description:
            - Timeout for sending se_ready without ns helper registration completion.
            - Allowed values are 10-600.
            - Field introduced in 21.1.1.
            - Unit is seconds.
            - Allowed in enterprise edition with any value, essentials edition with any value, basic edition with any value, enterprise with cloud services
            - edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 300.
        type: int
    service_ip6_subnets:
        description:
            - Ipv6 subnets assigned to the se group.
            - Required for vs group placement.
            - Field introduced in 18.1.1.
            - Maximum of 128 items allowed.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: list
        elements: dict
    service_ip_subnets:
        description:
            - Subnets assigned to the se group.
            - Required for vs group placement.
            - Field introduced in 17.1.1.
            - Maximum of 128 items allowed.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: list
        elements: dict
    shm_minimum_config_memory:
        description:
            - Minimum required shared memory to apply any configuration.
            - Allowed values are 0-100.
            - Field introduced in 18.1.2.
            - Unit is mb.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 4.
        type: int
    ssl_preprocess_sni_hostname:
        description:
            - (beta) preprocess ssl client hello for sni hostname extension.if set to true, this will apply sni child's ssl protocol(s), if they are different
            - from sni parent's allowed ssl protocol(s).
            - Field introduced in 17.2.12, 18.1.3.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as True.
        type: bool
    ssl_sess_cache_per_vs:
        description:
            - Number of ssl sessions that can be cached per vs.
            - Field introduced in 21.1.1.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 4096.
        type: int
    transient_shared_memory_max:
        description:
            - The threshold for the transient shared config memory in the se.
            - Allowed values are 0-100.
            - Field introduced in 20.1.1.
            - Unit is percent.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 30.
        type: int
    upstream_connect_timeout:
        description:
            - Timeout for backend connection.
            - Field introduced in 21.1.1.
            - Unit is milliseconds.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 3600000.
        type: int
    upstream_connpool_enable:
        description:
            - Enable upstream connection pool,.
            - Field introduced in 21.1.1.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as True.
        type: bool
    upstream_read_timeout:
        description:
            - Timeout for data to be received from backend.
            - Field introduced in 21.1.1.
            - Unit is milliseconds.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 3600000.
        type: int
    upstream_send_timeout:
        description:
            - Timeout for upstream to become writable.
            - Field introduced in 21.1.1.
            - Unit is milliseconds.
            - Allowed in enterprise edition with any value, essentials edition(allowed values- 3600000), basic edition(allowed values- 3600000), enterprise
            - with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 3600000.
        type: int
    url:
        description:
            - Avi controller URL of the object.
        type: str
    use_legacy_netlink:
        description:
            - Enable legacy model of netlink notifications.
            - Field introduced in 21.1.1.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    user_defined_metric_age:
        description:
            - Defines in seconds how long before an unused user-defined-metric is garbage collected.
            - Field introduced in 21.1.1.
            - Unit is sec.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 60.
        type: int
    uuid:
        description:
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: str
    vip_asg:
        description:
            - When vip_asg is set, vip configuration will be managed by avi.user will be able to configure vip_asg or vips individually at the time of create.
            - Field introduced in 17.2.12, 18.1.2.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: dict
    vnic_dhcp_ip_check_interval:
        description:
            - Dhcp ip check interval.
            - Allowed values are 1-1000.
            - Field introduced in 21.1.1.
            - Unit is sec.
            - Allowed in enterprise edition with any value, essentials edition with any value, basic edition with any value, enterprise with cloud services
            - edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 6.
        type: int
    vnic_dhcp_ip_max_retries:
        description:
            - Dhcp ip max retries.
            - Field introduced in 21.1.1.
            - Allowed in enterprise edition with any value, essentials edition with any value, basic edition with any value, enterprise with cloud services
            - edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 10.
        type: int
    vnic_ip_delete_interval:
        description:
            - Wait interval before deleting ip.
            - Field introduced in 21.1.1.
            - Unit is sec.
            - Allowed in enterprise edition with any value, essentials edition with any value, basic edition with any value, enterprise with cloud services
            - edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 5.
        type: int
    vnic_probe_interval:
        description:
            - Probe vnic interval.
            - Field introduced in 21.1.1.
            - Unit is sec.
            - Allowed in enterprise edition with any value, essentials edition with any value, basic edition with any value, enterprise with cloud services
            - edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 5.
        type: int
    vnic_rpc_retry_interval:
        description:
            - Time interval for retrying the failed vnic rpc requests.
            - Field introduced in 21.1.1.
            - Unit is sec.
            - Allowed in enterprise edition with any value, essentials edition with any value, basic edition with any value, enterprise with cloud services
            - edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 5.
        type: int
    vnicdb_cmd_history_size:
        description:
            - Size of vnicdb command history.
            - Allowed values are 0-65535.
            - Field introduced in 21.1.1.
            - Allowed in enterprise edition with any value, essentials edition with any value, basic edition with any value, enterprise with cloud services
            - edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 256.
        type: int
    vss_placement:
        description:
            - Parameters to place virtual services on only a subset of the cores of an se.
            - Field introduced in 17.2.5.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: dict
    vss_placement_enabled:
        description:
            - If set, virtual services will be placed on only a subset of the cores of an se.
            - Field introduced in 18.1.1.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    waf_mempool:
        description:
            - Enable memory pool for waf.requires se reboot.
            - Field introduced in 17.2.3.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as True.
        type: bool
    waf_mempool_size:
        description:
            - Memory pool size used for waf.requires se reboot.
            - Field introduced in 17.2.3.
            - Unit is kb.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 64.
        type: int
extends_documentation_fragment:
    - vmware.alb.avi
"""

EXAMPLES = """
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
    - name: Example to configure ServiceEngineGroup object's advanced fields
      vmware.alb.avi_serviceenginegroup_advanced:
        avi_credentials: "{{ avi_credentials }}"
        name: sample_serviceenginegroup
"""
RETURN = """
obj:
    description: ServiceEngineGroup (api/serviceenginegroup) object
    returned: success, changed
    type: dict
"""

from ansible.module_utils.basic import AnsibleModule
try:
    from ansible_collections.vmware.alb.plugins.module_utils.utils.ansible_utils import (
        avi_common_argument_spec,
        avi_obj_cmp,
        ansible_return,
        purge_optional_fields,
        AviCheckModeResponse,
    )
    from ansible_collections.vmware.alb.plugins.module_utils.avi_api import (
        ApiSession,
        AviCredentials,
        ObjectNotFound,
    )
    import yaml
    from copy import deepcopy

    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False


def main():
    argument_specs = dict(
        name=dict(type="str", required=True),
        uuid=dict(type="str"),
        avi_api_update_method=dict(default="put", choices=["put", "patch"]),
        avi_api_patch_op=dict(choices=["add", "replace", "delete", "remove"]),
        avi_patch_path=dict(type="str"),
        avi_patch_value=dict(type="str"),
        configpb_attributes=dict(type="dict"),
        kni_allowed_server_ports=dict(type="list", elements="dict"),
        max_skb_frags=dict(type="int"),
        netlink_poller_threads=dict(type="int"),
        netlink_sock_buf_size=dict(type="int"),
        ngx_free_connection_stack=dict(type="bool"),
        num_flow_cores_sum_changes_to_ignore=dict(type="int"),
        pcap_tx_mode=dict(type="str"),
        pcap_tx_ring_rd_balancing_factor=dict(type="int"),
        se_dp_max_hb_version=dict(type="int"),
        se_dp_vnic_queue_stall_event_sleep=dict(type="int"),
        se_dp_vnic_queue_stall_threshold=dict(type="int"),
        se_dp_vnic_queue_stall_timeout=dict(type="int"),
        se_dp_vnic_restart_on_queue_stall_count=dict(type="int"),
        se_dp_vnic_stall_se_restart_window=dict(type="int"),
        se_dump_core_on_assert=dict(type="bool"),
        se_flow_probe_retries=dict(type="int"),
        se_flow_probe_retry_timer=dict(type="int"),
        se_group_analytics_policy=dict(type="dict"),
        se_ip_encap_ipc=dict(type="int"),
        se_kni_burst_factor=dict(type="int"),
        se_l3_encap_ipc=dict(type="int"),
        se_log_buffer_app_blocking_dequeue=dict(type="bool"),
        se_log_buffer_conn_blocking_dequeue=dict(type="bool"),
        se_log_buffer_events_blocking_dequeue=dict(type="bool"),
        se_mp_ring_retry_count=dict(type="int"),
        se_packet_buffer_max=dict(type="int"),
        se_pcap_lookahead=dict(type="bool"),
        se_pcap_pkt_count=dict(type="int"),
        se_pcap_pkt_sz=dict(type="int"),
        se_pcap_qdisc_bypass=dict(type="bool"),
        se_pcap_reinit_frequency=dict(type="int"),
        se_pcap_reinit_threshold=dict(type="int"),
        se_probe_port=dict(type="int"),
        se_rl_prop=dict(type="dict"),
        se_rum_sampling_nav_interval=dict(type="int"),
        se_rum_sampling_nav_percent=dict(type="int"),
        se_rum_sampling_res_interval=dict(type="int"),
        se_rum_sampling_res_percent=dict(type="int"),
        se_sb_dedicated_core=dict(type="bool"),
        se_sb_threads=dict(type="int"),
        se_thread_multiplier=dict(type="int"),
        se_time_tracker_props=dict(type="dict"),
        se_tracert_port_range=dict(type="dict"),
        se_tunnel_mode=dict(type="int"),
        se_tunnel_udp_port=dict(type="int"),
        se_tx_batch_size=dict(type="int"),
        se_txq_threshold=dict(type="int"),
        se_udp_encap_ipc=dict(type="int"),
        se_vnic_tx_sw_queue_flush_frequency=dict(type="int"),
        se_vnic_tx_sw_queue_size=dict(type="int"),
        se_vs_hb_max_pkts_in_batch=dict(type="int"),
        se_vs_hb_max_vs_in_pkt=dict(type="int"),
        send_se_ready_timeout=dict(type="int"),
        service_ip6_subnets=dict(type="list", elements="dict"),
        service_ip_subnets=dict(type="list", elements="dict"),
        shm_minimum_config_memory=dict(type="int"),
        ssl_preprocess_sni_hostname=dict(type="bool"),
        ssl_sess_cache_per_vs=dict(type="int"),
        transient_shared_memory_max=dict(type="int"),
        upstream_connect_timeout=dict(type="int"),
        upstream_connpool_enable=dict(type="bool"),
        upstream_read_timeout=dict(type="int"),
        upstream_send_timeout=dict(type="int"),
        url=dict(type="str"),
        use_legacy_netlink=dict(type="bool"),
        user_defined_metric_age=dict(type="int"),
        vip_asg=dict(type="dict"),
        vnic_dhcp_ip_check_interval=dict(type="int"),
        vnic_dhcp_ip_max_retries=dict(type="int"),
        vnic_ip_delete_interval=dict(type="int"),
        vnic_probe_interval=dict(type="int"),
        vnic_rpc_retry_interval=dict(type="int"),
        vnicdb_cmd_history_size=dict(type="int"),
        vss_placement=dict(type="dict"),
        vss_placement_enabled=dict(type="bool"),
        waf_mempool=dict(type="bool"),
        waf_mempool_size=dict(type="int"),
    )
    argument_specs.update(avi_common_argument_spec())
    module = AnsibleModule(argument_spec=argument_specs, supports_check_mode=True)
    if not HAS_REQUESTS:
        return module.fail_json(
            msg="Python requests package is not installed. For installation instructions, visit https://pypi.org/project/requests."
        )
    changed = False
    avi_patch_op = module.params["avi_api_patch_op"]
    uuid = module.params.get("uuid", None)
    obj_type = "serviceenginegroup"
    obj_path = "%s/%s" % (obj_type, uuid)
    api_creds = AviCredentials()
    api_creds.update_from_ansible_module(module)
    api = ApiSession.get_session(
        api_creds.controller,
        api_creds.username,
        password=api_creds.password,
        timeout=api_creds.timeout,
        tenant=api_creds.tenant,
        tenant_uuid=api_creds.tenant_uuid,
        token=api_creds.token,
        port=api_creds.port,
    )

    # Get the api version.
    # avi_update_method = module.params.get('avi_api_update_method', 'put')

    avi_patch_op = module.params.get("avi_api_patch_op", "add")
    avi_patch_path = module.params.get("avi_patch_path")
    avi_patch_value = module.params.get("avi_patch_value", None)
    api_version = api_creds.api_version
    name = module.params.get("name", None)

    # Added Support to get uuid

    check_mode = module.check_mode
    if uuid and obj_type:
        obj_path = "%s/%s" % (obj_type, uuid)
    else:
        obj_path = "%s/" % obj_type
    obj = deepcopy(module.params)
    tenant = obj.pop("tenant", "")
    tenant_uuid = obj.pop("tenant_uuid", "")

    # obj.pop('cloud_ref', None)

    POP_FIELDS = [
        "state",
        "controller",
        "username",
        "password",
        "api_version",
        "avi_credentials",
        "avi_api_update_method",
        "avi_api_patch_op",
        "avi_patch_path",
        "avi_patch_value",
        "api_context",
        "tenant",
        "tenant_uuid",
        "avi_deactivate_session_cache_as_fact",
    ]

    for k in POP_FIELDS:
        obj.pop(k, None)
        purge_optional_fields(obj, module)

    if uuid:

        # Get the object based on uuid.

        try:
            existing_obj = api.get(
                obj_path,
                tenant=tenant,
                tenant_uuid=tenant_uuid,
                params={"include_refs": "", "include_name": ""},
                api_version=api_version,
            )
            existing_obj = existing_obj.json()
        except ObjectNotFound:
            existing_obj = None
    elif name:
        params = {"include_refs": "", "include_name": ""}
        if obj.get("cloud_ref", None):

            # this is the case when gets have to be scoped with cloud

            cloud = obj["cloud_ref"].split("name=")[1]
            params["cloud_ref.name"] = cloud
        existing_obj = api.get_object_by_name(
            obj_type,
            name,
            tenant=tenant,
            tenant_uuid=tenant_uuid,
            params=params,
            api_version=api_version,
        )

        # Need to check if tenant_ref was provided and the object returned
        # is actually in admin tenant.

        if (existing_obj and "tenant_ref" in obj and "tenant_ref" in existing_obj and obj["tenant_ref"] is not None):
            existing_obj_tenant = existing_obj["tenant_ref"].split("#")[1]
            obj_tenant = obj["tenant_ref"].split("name=")[1]
            if obj_tenant != existing_obj_tenant:
                existing_obj = None
    else:

        # added api version to avi api call.

        existing_obj = api.get(
            obj_path,
            tenant=tenant,
            tenant_uuid=tenant_uuid,
            params={"include_refs": "", "include_name": ""},
            api_version=api_version,
        ).json()
    rsp = None
    req = None
    if existing_obj:

        # this is case of modify as object exists. should find out
        # if changed is true or not

        if name is not None:
            obj_uuid = existing_obj["uuid"]
            obj_path = "%s/%s" % (obj_type, obj_uuid)
        changed = not avi_obj_cmp(obj, existing_obj)
        if check_mode:

            # No need to process any further.

            rsp = AviCheckModeResponse(obj=existing_obj)
        else:
            if changed:
                obj.pop("name", None)
                patch_data = {}
                if avi_patch_path:
                    if avi_patch_value:
                        avi_patch_value = yaml.load(avi_patch_value)
                    patch_data = {
                        "json_patch": [
                            {
                                "op": avi_patch_op,
                                "path": avi_patch_path,
                                "value": avi_patch_value,
                            }
                        ]
                    }
                else:

                    patch_data.update({avi_patch_op: obj})
                try:
                    rsp = api.patch(
                        obj_path,
                        data=patch_data,
                        tenant=tenant,
                        tenant_uuid=tenant_uuid,
                        api_version=api_version,
                    )
                    obj = rsp.json()
                    changed = not avi_obj_cmp(obj, existing_obj)
                except ObjectNotFound:
                    changed = False
                    rsp = None

    return ansible_return(
        module,
        rsp,
        changed,
        req,
        existing_obj=existing_obj,
        api_context=api.get_context(),
    )


if __name__ == "__main__":
    main()
