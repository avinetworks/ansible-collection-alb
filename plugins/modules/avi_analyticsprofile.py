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
module: avi_analyticsprofile
author: Gaurav Rastogi (@grastogi23) <grastogi@avinetworks.com>
short_description: Module for setup of AnalyticsProfile Avi RESTful Object
description:
    - This module is used to configure AnalyticsProfile object
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
    apdex_response_threshold:
        description:
            - If a client receives an http response in less than the satisfactory latency threshold, the request is considered satisfied.
            - It is considered tolerated if it is not satisfied and less than tolerated latency factor multiplied by the satisfactory latency threshold.
            - Greater than this number and the client's request is considered frustrated.
            - Allowed values are 1-30000.
            - Unit is milliseconds.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Allowed in essentials (allowed values- 500), basic (allowed values- 500) edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 500.
        type: int
    apdex_response_tolerated_factor:
        description:
            - Client tolerated response latency factor.
            - Client must receive a response within this factor times the satisfactory threshold (apdex_response_threshold) to be considered tolerated.
            - Allowed values are 1-1000.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Allowed in essentials (allowed values- 4), basic (allowed values- 4) edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 4.0.
        type: float
    apdex_rtt_threshold:
        description:
            - Satisfactory client to avi round trip time(rtt).
            - Allowed values are 1-2000.
            - Unit is milliseconds.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Allowed in essentials (allowed values- 250), basic (allowed values- 250) edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 250.
        type: int
    apdex_rtt_tolerated_factor:
        description:
            - Tolerated client to avi round trip time(rtt) factor.
            - It is a multiple of apdex_rtt_tolerated_factor.
            - Allowed values are 1-1000.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Allowed in essentials (allowed values- 4), basic (allowed values- 4) edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 4.0.
        type: float
    apdex_rum_threshold:
        description:
            - If a client is able to load a page in less than the satisfactory latency threshold, the pageload is considered satisfied.
            - It is considered tolerated if it is greater than satisfied but less than the tolerated latency multiplied by satisifed latency.
            - Greater than this number and the client's request is considered frustrated.
            - A pageload includes the time for dns lookup, download of all http objects, and page render time.
            - Allowed values are 1-30000.
            - Unit is milliseconds.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Allowed in essentials (allowed values- 5000), basic (allowed values- 5000) edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 5000.
        type: int
    apdex_rum_tolerated_factor:
        description:
            - Virtual service threshold factor for tolerated page load time (plt) as multiple of apdex_rum_threshold.
            - Allowed values are 1-1000.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Allowed in essentials (allowed values- 4), basic (allowed values- 4) edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 4.0.
        type: float
    apdex_server_response_threshold:
        description:
            - A server http response is considered satisfied if latency is less than the satisfactory latency threshold.
            - The response is considered tolerated when it is greater than satisfied but less than the tolerated latency factor * s_latency.
            - Greater than this number and the server response is considered frustrated.
            - Allowed values are 1-30000.
            - Unit is milliseconds.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Allowed in essentials (allowed values- 400), basic (allowed values- 400) edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 400.
        type: int
    apdex_server_response_tolerated_factor:
        description:
            - Server tolerated response latency factor.
            - Servermust response within this factor times the satisfactory threshold (apdex_server_response_threshold) to be considered tolerated.
            - Allowed values are 1-1000.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Allowed in essentials (allowed values- 4), basic (allowed values- 4) edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 4.0.
        type: float
    apdex_server_rtt_threshold:
        description:
            - Satisfactory client to avi round trip time(rtt).
            - Allowed values are 1-2000.
            - Unit is milliseconds.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Allowed in essentials (allowed values- 125), basic (allowed values- 125) edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 125.
        type: int
    apdex_server_rtt_tolerated_factor:
        description:
            - Tolerated client to avi round trip time(rtt) factor.
            - It is a multiple of apdex_rtt_tolerated_factor.
            - Allowed values are 1-1000.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Allowed in essentials (allowed values- 4), basic (allowed values- 4) edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 4.0.
        type: float
    client_log_config:
        description:
            - Configure which logs are sent to the avi controller from ses and how they are processed.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: dict
    client_log_streaming_config:
        description:
            - Configure to stream logs to an external server.
            - Field introduced in 17.1.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: dict
    configpb_attributes:
        description:
            - Protobuf versioning for config pbs.
            - Field introduced in 21.1.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: dict
    conn_lossy_ooo_threshold:
        description:
            - A connection between client and avi is considered lossy when more than this percentage of out of order packets are received.
            - Allowed values are 1-100.
            - Unit is percent.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Allowed in essentials (allowed values- 50), basic (allowed values- 50) edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 50.
        type: int
    conn_lossy_timeo_rexmt_threshold:
        description:
            - A connection between client and avi is considered lossy when more than this percentage of packets are retransmitted due to timeout.
            - Allowed values are 1-100.
            - Unit is percent.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Allowed in essentials (allowed values- 20), basic (allowed values- 20) edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 20.
        type: int
    conn_lossy_total_rexmt_threshold:
        description:
            - A connection between client and avi is considered lossy when more than this percentage of packets are retransmitted.
            - Allowed values are 1-100.
            - Unit is percent.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Allowed in essentials (allowed values- 50), basic (allowed values- 50) edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 50.
        type: int
    conn_lossy_zero_win_size_event_threshold:
        description:
            - A client connection is considered lossy when percentage of times a packet could not be trasmitted due to tcp zero window is above this threshold.
            - Allowed values are 0-100.
            - Unit is percent.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Allowed in essentials (allowed values- 2), basic (allowed values- 2) edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 2.
        type: int
    conn_server_lossy_ooo_threshold:
        description:
            - A connection between avi and server is considered lossy when more than this percentage of out of order packets are received.
            - Allowed values are 1-100.
            - Unit is percent.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Allowed in essentials (allowed values- 50), basic (allowed values- 50) edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 50.
        type: int
    conn_server_lossy_timeo_rexmt_threshold:
        description:
            - A connection between avi and server is considered lossy when more than this percentage of packets are retransmitted due to timeout.
            - Allowed values are 1-100.
            - Unit is percent.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Allowed in essentials (allowed values- 20), basic (allowed values- 20) edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 20.
        type: int
    conn_server_lossy_total_rexmt_threshold:
        description:
            - A connection between avi and server is considered lossy when more than this percentage of packets are retransmitted.
            - Allowed values are 1-100.
            - Unit is percent.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Allowed in essentials (allowed values- 50), basic (allowed values- 50) edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 50.
        type: int
    conn_server_lossy_zero_win_size_event_threshold:
        description:
            - A server connection is considered lossy when percentage of times a packet could not be trasmitted due to tcp zero window is above this threshold.
            - Allowed values are 0-100.
            - Unit is percent.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Allowed in essentials (allowed values- 2), basic (allowed values- 2) edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 2.
        type: int
    description:
        description:
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    enable_adaptive_config:
        description:
            - Enable adaptive configuration for optimizing resource usage.
            - Field introduced in 20.1.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as True.
        type: bool
    enable_advanced_analytics:
        description:
            - Enables advanced analytics features like anomaly detection.
            - If set to false, anomaly computation (and associated rules/events) for vs, pool and server metrics will be deactivated.
            - However, setting it to false reduces cpu and memory requirements for analytics subsystem.
            - Field introduced in 17.2.13, 18.1.5, 18.2.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Allowed in essentials (allowed values- false), basic (allowed values- false) edition.
            - Special default for essentials edition is false, basic edition is false, enterprise edition is true.
            - Default value when not specified in API or module is interpreted by Avi Controller as True.
        type: bool
    enable_ondemand_metrics:
        description:
            - Virtual service (vs) metrics are processed only when there is live data traffic on the vs.
            - In case, vs is idle for a period of time as specified by ondemand_metrics_idle_timeout then metrics processing is suspended for that vs.
            - Field introduced in 20.1.3.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as True.
        type: bool
    enable_se_analytics:
        description:
            - Enable node (service engine) level analytics forvs metrics.
            - Field introduced in 20.1.3.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as True.
        type: bool
    enable_server_analytics:
        description:
            - Enables analytics on backend servers.
            - This may be desired in container environment when there are large number of ephemeral servers.
            - Additionally, no healthscore of servers is computed when server analytics is enabled.
            - Field introduced in 20.1.3.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as True.
        type: bool
    enable_vs_analytics:
        description:
            - Enable virtualservice (frontend) analytics.
            - This flag enables metrics and healthscore for virtualservice.
            - Field introduced in 20.1.3.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as True.
        type: bool
    exclude_client_close_before_request_as_error:
        description:
            - Exclude client closed connection before an http request could be completed from being classified as an error.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Allowed in essentials (allowed values- false), basic (allowed values- false) edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    exclude_dns_policy_drop_as_significant:
        description:
            - Exclude dns policy drops from the list of errors.
            - Field introduced in 17.2.2.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Allowed in essentials (allowed values- false), basic (allowed values- false) edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    exclude_gs_down_as_error:
        description:
            - Exclude queries to gslb services that are operationally down from the list of errors.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Allowed in essentials (allowed values- false), basic (allowed values- false) edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    exclude_http_error_codes:
        description:
            - List of http status codes to be excluded from being classified as an error.
            - Error connections or responses impacts health score, are included as significant logs, and may be classified as part of a dos attack.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: list
        elements: int
    exclude_invalid_dns_domain_as_error:
        description:
            - Exclude dns queries to domains outside the domains configured in the dns application profile from the list of errors.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Allowed in essentials (allowed values- false), basic (allowed values- false) edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    exclude_invalid_dns_query_as_error:
        description:
            - Exclude invalid dns queries from the list of errors.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Allowed in essentials (allowed values- false), basic (allowed values- false) edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    exclude_issuer_revoked_ocsp_responses_as_error:
        description:
            - Exclude the issuer-revoked ocsp responses from the list of errors.
            - Field introduced in 20.1.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Allowed in essentials (allowed values- true), basic (allowed values- true) edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as True.
        type: bool
    exclude_no_dns_record_as_error:
        description:
            - Exclude queries to domains that did not have configured services/records from the list of errors.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Allowed in essentials (allowed values- false), basic (allowed values- false) edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    exclude_no_valid_gs_member_as_error:
        description:
            - Exclude queries to gslb services that have no available members from the list of errors.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Allowed in essentials (allowed values- false), basic (allowed values- false) edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    exclude_persistence_change_as_error:
        description:
            - Exclude persistence server changed while load balancing' from the list of errors.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Allowed in essentials (allowed values- false), basic (allowed values- false) edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    exclude_revoked_ocsp_responses_as_error:
        description:
            - Exclude the revoked ocsp certificate status responses from the list of errors.
            - Field introduced in 20.1.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Allowed in essentials (allowed values- true), basic (allowed values- true) edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as True.
        type: bool
    exclude_server_dns_error_as_error:
        description:
            - Exclude server dns error response from the list of errors.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Allowed in essentials (allowed values- false), basic (allowed values- false) edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    exclude_server_tcp_reset_as_error:
        description:
            - Exclude server tcp reset from errors.
            - It is common for applications like ms exchange.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Allowed in essentials (allowed values- false), basic (allowed values- false) edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    exclude_sip_error_codes:
        description:
            - List of sip status codes to be excluded from being classified as an error.
            - Field introduced in 17.2.13, 18.1.5, 18.2.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: list
        elements: int
    exclude_stale_ocsp_responses_as_error:
        description:
            - Exclude the stale ocsp certificate status responses from the list of errors.
            - Field introduced in 20.1.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Allowed in essentials (allowed values- true), basic (allowed values- true) edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as True.
        type: bool
    exclude_syn_retransmit_as_error:
        description:
            - Exclude 'server unanswered syns' from the list of errors.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Allowed in essentials (allowed values- false), basic (allowed values- false) edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    exclude_tcp_reset_as_error:
        description:
            - Exclude tcp resets by client from the list of potential errors.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Allowed in essentials (allowed values- false), basic (allowed values- false) edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    exclude_unavailable_ocsp_responses_as_error:
        description:
            - Exclude the unavailable ocsp responses from the list of errors.
            - Field introduced in 20.1.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Allowed in essentials (allowed values- true), basic (allowed values- true) edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as True.
        type: bool
    exclude_unsupported_dns_query_as_error:
        description:
            - Exclude unsupported dns queries from the list of errors.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Allowed in essentials (allowed values- false), basic (allowed values- false) edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    healthscore_max_server_limit:
        description:
            - Skips health score computation of pool servers when number of servers in a pool is more than this setting.
            - Allowed values are 0-5000.
            - Special values are 0- server health score is deactivated.
            - Field introduced in 17.2.13, 18.1.4.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Allowed in essentials (allowed values- 0), basic (allowed values- 0) edition.
            - Special default for essentials edition is 0, basic edition is 0, enterprise edition is 20.
            - Default value when not specified in API or module is interpreted by Avi Controller as 20.
        type: int
    hs_event_throttle_window:
        description:
            - Time window (in secs) within which only unique health change events should occur.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Allowed in essentials (allowed values- 1209600), basic (allowed values- 1209600) edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 1209600.
        type: int
    hs_max_anomaly_penalty:
        description:
            - Maximum penalty that may be deducted from health score for anomalies.
            - Allowed values are 0-100.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Allowed in essentials (allowed values- 10), basic (allowed values- 10) edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 10.
        type: int
    hs_max_resources_penalty:
        description:
            - Maximum penalty that may be deducted from health score for high resource utilization.
            - Allowed values are 0-100.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Allowed in essentials (allowed values- 25), basic (allowed values- 25) edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 25.
        type: int
    hs_max_security_penalty:
        description:
            - Maximum penalty that may be deducted from health score based on security assessment.
            - Allowed values are 0-100.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Allowed in essentials (allowed values- 100), basic (allowed values- 100) edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 100.
        type: int
    hs_min_dos_rate:
        description:
            - Dos connection rate below which the dos security assessment will not kick in.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Allowed in essentials (allowed values- 1000), basic (allowed values- 1000) edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 1000.
        type: int
    hs_performance_boost:
        description:
            - Adds free performance score credits to health score.
            - It can be used for compensating health score for known slow applications.
            - Allowed values are 0-100.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Allowed in essentials (allowed values- 0), basic (allowed values- 0) edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 0.
        type: int
    hs_pscore_traffic_threshold_l4_client:
        description:
            - Threshold number of connections in 5min, below which apdexr, apdexc, rum_apdex, and other network quality metrics are not computed.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Allowed in essentials (allowed values- 10), basic (allowed values- 10) edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 10.0.
        type: float
    hs_pscore_traffic_threshold_l4_server:
        description:
            - Threshold number of connections in 5min, below which apdexr, apdexc, rum_apdex, and other network quality metrics are not computed.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Allowed in essentials (allowed values- 10), basic (allowed values- 10) edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 10.0.
        type: float
    hs_security_certscore_expired:
        description:
            - Score assigned when the certificate has expired.
            - Allowed values are 0-5.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Allowed in essentials (allowed values- 0.0), basic (allowed values- 0.0) edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 0.0.
        type: float
    hs_security_certscore_gt30d:
        description:
            - Score assigned when the certificate expires in more than 30 days.
            - Allowed values are 0-5.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Allowed in essentials (allowed values- 5.0), basic (allowed values- 5.0) edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 5.0.
        type: float
    hs_security_certscore_le07d:
        description:
            - Score assigned when the certificate expires in less than or equal to 7 days.
            - Allowed values are 0-5.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Allowed in essentials (allowed values- 2.0), basic (allowed values- 2.0) edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 2.0.
        type: float
    hs_security_certscore_le30d:
        description:
            - Score assigned when the certificate expires in less than or equal to 30 days.
            - Allowed values are 0-5.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Allowed in essentials (allowed values- 4.0), basic (allowed values- 4.0) edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 4.0.
        type: float
    hs_security_chain_invalidity_penalty:
        description:
            - Penalty for allowing certificates with invalid chain.
            - Allowed values are 0-5.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Allowed in essentials (allowed values- 1.0), basic (allowed values- 1.0) edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 1.0.
        type: float
    hs_security_cipherscore_eq000b:
        description:
            - Score assigned when the minimum cipher strength is 0 bits.
            - Allowed values are 0-5.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Allowed in essentials (allowed values- 0.0), basic (allowed values- 0.0) edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 0.0.
        type: float
    hs_security_cipherscore_ge128b:
        description:
            - Score assigned when the minimum cipher strength is greater than equal to 128 bits.
            - Allowed values are 0-5.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Allowed in essentials (allowed values- 5.0), basic (allowed values- 5.0) edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 5.0.
        type: float
    hs_security_cipherscore_lt128b:
        description:
            - Score assigned when the minimum cipher strength is less than 128 bits.
            - Allowed values are 0-5.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Allowed in essentials (allowed values- 3.5), basic (allowed values- 3.5) edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 3.5.
        type: float
    hs_security_encalgo_score_none:
        description:
            - Score assigned when no algorithm is used for encryption.
            - Allowed values are 0-5.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Allowed in essentials (allowed values- 0.0), basic (allowed values- 0.0) edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 0.0.
        type: float
    hs_security_encalgo_score_rc4:
        description:
            - Score assigned when rc4 algorithm is used for encryption.
            - Allowed values are 0-5.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Allowed in essentials (allowed values- 2.5), basic (allowed values- 2.5) edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 2.5.
        type: float
    hs_security_hsts_penalty:
        description:
            - Penalty for not enabling hsts.
            - Allowed values are 0-5.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Allowed in essentials (allowed values- 1.0), basic (allowed values- 1.0) edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 1.0.
        type: float
    hs_security_nonpfs_penalty:
        description:
            - Penalty for allowing non-pfs handshakes.
            - Allowed values are 0-5.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Allowed in essentials (allowed values- 1.0), basic (allowed values- 1.0) edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 1.0.
        type: float
    hs_security_ocsp_revoked_score:
        description:
            - Score assigned when ocsp certificate status is set to revoked or issuer revoked.
            - Allowed values are 0.0-5.0.
            - Field introduced in 20.1.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Allowed in essentials (allowed values- 0.0), basic (allowed values- 0.0) edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 0.0.
        type: float
    hs_security_selfsignedcert_penalty:
        description:
            - Deprecated.
            - Allowed values are 0-5.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Allowed in essentials (allowed values- 1.0), basic (allowed values- 1.0) edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 1.0.
        type: float
    hs_security_ssl30_score:
        description:
            - Score assigned when supporting ssl3.0 encryption protocol.
            - Allowed values are 0-5.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Allowed in essentials (allowed values- 3.5), basic (allowed values- 3.5) edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 3.5.
        type: float
    hs_security_tls10_score:
        description:
            - Score assigned when supporting tls1.0 encryption protocol.
            - Allowed values are 0-5.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Allowed in essentials (allowed values- 5.0), basic (allowed values- 5.0) edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 5.0.
        type: float
    hs_security_tls11_score:
        description:
            - Score assigned when supporting tls1.1 encryption protocol.
            - Allowed values are 0-5.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Allowed in essentials (allowed values- 5.0), basic (allowed values- 5.0) edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 5.0.
        type: float
    hs_security_tls12_score:
        description:
            - Score assigned when supporting tls1.2 encryption protocol.
            - Allowed values are 0-5.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Allowed in essentials (allowed values- 5.0), basic (allowed values- 5.0) edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 5.0.
        type: float
    hs_security_tls13_score:
        description:
            - Score assigned when supporting tls1.3 encryption protocol.
            - Allowed values are 0-5.
            - Field introduced in 18.2.6.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Allowed in essentials (allowed values- 5.0), basic (allowed values- 5.0) edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 5.0.
        type: float
    hs_security_weak_signature_algo_penalty:
        description:
            - Penalty for allowing weak signature algorithm(s).
            - Allowed values are 0-5.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Allowed in essentials (allowed values- 1.0), basic (allowed values- 1.0) edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 1.0.
        type: float
    latency_audit_props:
        description:
            - Deprecated in 22.1.1.
            - Field introduced in 21.1.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: dict
    markers:
        description:
            - List of labels to be used for granular rbac.
            - Field introduced in 20.1.5.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: list
        elements: dict
    name:
        description:
            - The name of the analytics profile.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        required: true
        type: str
    ondemand_metrics_idle_timeout:
        description:
            - This flag sets the time duration of no live data traffic after which virtual service metrics processing is suspended.
            - It is applicable only when enable_ondemand_metrics is set to false.
            - Field introduced in 18.1.1.
            - Unit is seconds.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 1800.
        type: int
    ranges:
        description:
            - List of http status code ranges to be excluded from being classified as an error.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: list
        elements: dict
    resp_code_block:
        description:
            - Block of http response codes to be excluded from being classified as an error.
            - Enum options - AP_HTTP_RSP_4XX, AP_HTTP_RSP_5XX.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: list
        elements: str
    sensitive_log_profile:
        description:
            - Rules applied to the http application log for filtering sensitive information.
            - Field introduced in 17.2.10, 18.1.2.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: dict
    sip_log_depth:
        description:
            - Maximum number of sip messages added in logs for a sip transaction.
            - By default, this value is 20.
            - Allowed values are 1-1000.
            - Field introduced in 17.2.13, 18.1.5, 18.2.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Allowed in essentials (allowed values- 20), basic (allowed values- 20) edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 20.
        type: int
    tenant_ref:
        description:
            - It is a reference to an object of type tenant.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    time_tracker_props:
        description:
            - Time tracker properties for connection establishment audit.
            - Field introduced in 22.1.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: dict
    url:
        description:
            - Avi controller URL of the object.
        type: str
    uuid:
        description:
            - Uuid of the analytics profile.
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

- name: Create a custom Analytics profile object
  vmware.alb.avi_analyticsprofile:
    avi_credentials: "{{ avi_credentials }}"
    apdex_response_threshold: 500
    apdex_response_tolerated_factor: 4.0
    apdex_rtt_threshold: 250
    apdex_rtt_tolerated_factor: 4.0
    apdex_rum_threshold: 5000
    apdex_rum_tolerated_factor: 4.0
    apdex_server_response_threshold: 400
    apdex_server_response_tolerated_factor: 4.0
    apdex_server_rtt_threshold: 125
    apdex_server_rtt_tolerated_factor: 4.0
    conn_lossy_ooo_threshold: 50
    conn_lossy_timeo_rexmt_threshold: 20
    conn_lossy_total_rexmt_threshold: 50
    conn_lossy_zero_win_size_event_threshold: 2
    conn_server_lossy_ooo_threshold: 50
    conn_server_lossy_timeo_rexmt_threshold: 20
    conn_server_lossy_total_rexmt_threshold: 50
    conn_server_lossy_zero_win_size_event_threshold: 2
    enable_se_analytics: true
    enable_server_analytics: true
    exclude_client_close_before_request_as_error: false
    exclude_persistence_change_as_error: false
    exclude_server_tcp_reset_as_error: false
    exclude_syn_retransmit_as_error: false
    exclude_tcp_reset_as_error: false
    hs_event_throttle_window: 1209600
    hs_max_anomaly_penalty: 10
    hs_max_resources_penalty: 25
    hs_max_security_penalty: 100
    hs_min_dos_rate: 1000
    hs_performance_boost: 20
    hs_pscore_traffic_threshold_l4_client: 10.0
    hs_pscore_traffic_threshold_l4_server: 10.0
    hs_security_certscore_expired: 0.0
    hs_security_certscore_gt30d: 5.0
    hs_security_certscore_le07d: 2.0
    hs_security_certscore_le30d: 4.0
    hs_security_chain_invalidity_penalty: 1.0
    hs_security_cipherscore_eq000b: 0.0
    hs_security_cipherscore_ge128b: 5.0
    hs_security_cipherscore_lt128b: 3.5
    hs_security_encalgo_score_none: 0.0
    hs_security_encalgo_score_rc4: 2.5
    hs_security_hsts_penalty: 0.0
    hs_security_nonpfs_penalty: 1.0
    hs_security_selfsignedcert_penalty: 1.0
    hs_security_ssl30_score: 3.5
    hs_security_tls10_score: 5.0
    hs_security_tls11_score: 5.0
    hs_security_tls12_score: 5.0
    hs_security_weak_signature_algo_penalty: 1.0
    name: jason-analytics-profile
    tenant_ref: /api/tenant?name=Demo
"""

RETURN = '''
obj:
    description: AnalyticsProfile (api/analyticsprofile) object
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
        apdex_response_threshold=dict(type='int',),
        apdex_response_tolerated_factor=dict(type='float',),
        apdex_rtt_threshold=dict(type='int',),
        apdex_rtt_tolerated_factor=dict(type='float',),
        apdex_rum_threshold=dict(type='int',),
        apdex_rum_tolerated_factor=dict(type='float',),
        apdex_server_response_threshold=dict(type='int',),
        apdex_server_response_tolerated_factor=dict(type='float',),
        apdex_server_rtt_threshold=dict(type='int',),
        apdex_server_rtt_tolerated_factor=dict(type='float',),
        client_log_config=dict(type='dict',),
        client_log_streaming_config=dict(type='dict',),
        configpb_attributes=dict(type='dict',),
        conn_lossy_ooo_threshold=dict(type='int',),
        conn_lossy_timeo_rexmt_threshold=dict(type='int',),
        conn_lossy_total_rexmt_threshold=dict(type='int',),
        conn_lossy_zero_win_size_event_threshold=dict(type='int',),
        conn_server_lossy_ooo_threshold=dict(type='int',),
        conn_server_lossy_timeo_rexmt_threshold=dict(type='int',),
        conn_server_lossy_total_rexmt_threshold=dict(type='int',),
        conn_server_lossy_zero_win_size_event_threshold=dict(type='int',),
        description=dict(type='str',),
        enable_adaptive_config=dict(type='bool',),
        enable_advanced_analytics=dict(type='bool',),
        enable_ondemand_metrics=dict(type='bool',),
        enable_se_analytics=dict(type='bool',),
        enable_server_analytics=dict(type='bool',),
        enable_vs_analytics=dict(type='bool',),
        exclude_client_close_before_request_as_error=dict(type='bool',),
        exclude_dns_policy_drop_as_significant=dict(type='bool',),
        exclude_gs_down_as_error=dict(type='bool',),
        exclude_http_error_codes=dict(type='list', elements='int',),
        exclude_invalid_dns_domain_as_error=dict(type='bool',),
        exclude_invalid_dns_query_as_error=dict(type='bool',),
        exclude_issuer_revoked_ocsp_responses_as_error=dict(type='bool',),
        exclude_no_dns_record_as_error=dict(type='bool',),
        exclude_no_valid_gs_member_as_error=dict(type='bool',),
        exclude_persistence_change_as_error=dict(type='bool',),
        exclude_revoked_ocsp_responses_as_error=dict(type='bool',),
        exclude_server_dns_error_as_error=dict(type='bool',),
        exclude_server_tcp_reset_as_error=dict(type='bool',),
        exclude_sip_error_codes=dict(type='list', elements='int',),
        exclude_stale_ocsp_responses_as_error=dict(type='bool',),
        exclude_syn_retransmit_as_error=dict(type='bool',),
        exclude_tcp_reset_as_error=dict(type='bool',),
        exclude_unavailable_ocsp_responses_as_error=dict(type='bool',),
        exclude_unsupported_dns_query_as_error=dict(type='bool',),
        healthscore_max_server_limit=dict(type='int',),
        hs_event_throttle_window=dict(type='int',),
        hs_max_anomaly_penalty=dict(type='int',),
        hs_max_resources_penalty=dict(type='int',),
        hs_max_security_penalty=dict(type='int',),
        hs_min_dos_rate=dict(type='int',),
        hs_performance_boost=dict(type='int',),
        hs_pscore_traffic_threshold_l4_client=dict(type='float',),
        hs_pscore_traffic_threshold_l4_server=dict(type='float',),
        hs_security_certscore_expired=dict(type='float',),
        hs_security_certscore_gt30d=dict(type='float',),
        hs_security_certscore_le07d=dict(type='float',),
        hs_security_certscore_le30d=dict(type='float',),
        hs_security_chain_invalidity_penalty=dict(type='float',),
        hs_security_cipherscore_eq000b=dict(type='float',),
        hs_security_cipherscore_ge128b=dict(type='float',),
        hs_security_cipherscore_lt128b=dict(type='float',),
        hs_security_encalgo_score_none=dict(type='float',),
        hs_security_encalgo_score_rc4=dict(type='float',),
        hs_security_hsts_penalty=dict(type='float',),
        hs_security_nonpfs_penalty=dict(type='float',),
        hs_security_ocsp_revoked_score=dict(type='float',),
        hs_security_selfsignedcert_penalty=dict(type='float',),
        hs_security_ssl30_score=dict(type='float',),
        hs_security_tls10_score=dict(type='float',),
        hs_security_tls11_score=dict(type='float',),
        hs_security_tls12_score=dict(type='float',),
        hs_security_tls13_score=dict(type='float',),
        hs_security_weak_signature_algo_penalty=dict(type='float',),
        latency_audit_props=dict(type='dict',),
        markers=dict(type='list', elements='dict',),
        name=dict(type='str', required=True),
        ondemand_metrics_idle_timeout=dict(type='int',),
        ranges=dict(type='list', elements='dict',),
        resp_code_block=dict(type='list', elements='str',),
        sensitive_log_profile=dict(type='dict',),
        sip_log_depth=dict(type='int',),
        tenant_ref=dict(type='str',),
        time_tracker_props=dict(type='dict',),
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
    return avi_ansible_api(module, 'analyticsprofile',
                           set())


if __name__ == '__main__':
    main()
