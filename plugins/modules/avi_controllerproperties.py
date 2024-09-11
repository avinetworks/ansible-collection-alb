#!/usr/bin/python
# module_check: supported

# Avi Version: 17.1.2
# Copyright 2021 VMware, Inc.  All rights reserved. VMware Confidential
# SPDX-License-Identifier: Apache License 2.0

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: avi_controllerproperties
author: Gaurav Rastogi (@grastogi23) <grastogi@avinetworks.com>
short_description: Module for setup of ControllerProperties Avi RESTful Object
description:
    - This module is used to configure ControllerProperties object
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
    alert_manager_use_evms:
        description:
            - Enable to use event manager as source of eventsdisable to use log manager as source of events.
            - Field introduced in 30.2.1.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as True.
        type: bool
    allow_admin_network_updates:
        description:
            - Allow non-admin tenants to update admin vrfcontext and network objects.
            - Field introduced in 18.2.7, 20.1.1.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    allow_ip_forwarding:
        description:
            - Field introduced in 17.1.1.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    allow_unauthenticated_apis:
        description:
            - Allow unauthenticated access for special apis.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    allow_unauthenticated_nodes:
        description:
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    api_idle_timeout:
        description:
            - Allowed values are 0-1440.
            - Unit is min.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 15.
        type: int
    api_perf_logging_threshold:
        description:
            - Threshold to log request timing in portal_performance.log and server-timing response header.
            - Any stage taking longer than 1% of the threshold will be included in the server-timing header.
            - Field introduced in 18.1.4, 18.2.1.
            - Unit is milliseconds.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 10000.
        type: int
    appviewx_compat_mode:
        description:
            - Export configuration in appviewx compatibility mode.
            - Field introduced in 17.1.1.
            - Allowed in enterprise edition with any value, essentials edition(allowed values- false), basic edition(allowed values- false), enterprise with
            - cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    async_patch_merge_period:
        description:
            - Period for which asynchronous patch requests are queued.
            - Allowed values are 30-120.
            - Special values are 0 - deactivated.
            - Field introduced in 18.2.11, 20.1.3.
            - Unit is sec.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 0.
        type: int
    async_patch_request_cleanup_duration:
        description:
            - Duration for which asynchronous patch requests should be kept, after being marked as success or fail.
            - Allowed values are 5-120.
            - Field introduced in 18.2.11, 20.1.3.
            - Unit is min.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 60.
        type: int
    attach_ip_retry_interval:
        description:
            - Unit is sec.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 360.
        type: int
    attach_ip_retry_limit:
        description:
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 4.
        type: int
    bm_use_ansible:
        description:
            - Use ansible for se creation in baremetal.
            - Field introduced in 17.2.2.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as True.
        type: bool
    check_vsvip_fqdn_syntax:
        description:
            - Enforce vsvip fqdn syntax checks.
            - Field introduced in 20.1.6.
            - Allowed in enterprise edition with any value, essentials edition with any value, basic edition with any value, enterprise with cloud services
            - edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as True.
        type: bool
    cleanup_expired_authtoken_timeout_period:
        description:
            - Period for auth token cleanup job.
            - Field introduced in 18.1.1.
            - Unit is min.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 60.
        type: int
    cleanup_sessions_timeout_period:
        description:
            - Period for sessions cleanup job.
            - Field introduced in 18.1.1.
            - Unit is min.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 60.
        type: int
    cloud_discovery_interval:
        description:
            - Time in minutes to wait between consecutive cloud discovery cycles.
            - Allowed values are 1-1440.
            - Field introduced in 22.1.5, 30.2.1.
            - Unit is min.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 5.
        type: int
    cloud_reconcile:
        description:
            - Enable/disable periodic reconcile for all the clouds.
            - Field introduced in 17.2.14,18.1.5,18.2.1.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as True.
        type: bool
    cloud_reconcile_interval:
        description:
            - Time in minutes to wait between consecutive cloud reconcile cycles.
            - Allowed values are 1-1440.
            - Field introduced in 22.1.5, 30.2.1.
            - Unit is min.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 5.
        type: int
    cluster_ip_gratuitous_arp_period:
        description:
            - Period for cluster ip gratuitous arp job.
            - Unit is min.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 60.
        type: int
    configpb_attributes:
        description:
            - Protobuf versioning for config pbs.
            - Field introduced in 21.1.1.
            - Allowed in enterprise edition with any value, essentials edition with any value, basic edition with any value, enterprise with cloud services
            - edition.
        type: dict
    consistency_check_timeout_period:
        description:
            - Period for consistency check job.
            - Field introduced in 18.1.1.
            - Unit is min.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 60.
        type: int
    controller_resource_info_collection_period:
        description:
            - Periodically collect stats.
            - Field introduced in 20.1.3.
            - Unit is min.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 525600.
        type: int
    crashed_se_reboot:
        description:
            - Unit is sec.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 900.
        type: int
    dead_se_detection_timer:
        description:
            - Unit is sec.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 360.
        type: int
    default_minimum_api_timeout:
        description:
            - Minimum api timeout value.if this value is not 60, it will be the default timeout for all apis that do not have a specific timeout.if an api has
            - a specific timeout but is less than this value, this value will become the new timeout.
            - Allowed values are 60-3600.
            - Field introduced in 18.2.6.
            - Unit is sec.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 60.
        type: int
    del_offline_se_after_reboot_delay:
        description:
            - The amount of time the controller will wait before deleting an offline se after it has been rebooted.
            - For unresponsive ses, the total time will be  unresponsive_se_reboot + del_offline_se_after_reboot_delay.
            - For crashed ses, the total time will be crashed_se_reboot + del_offline_se_after_reboot_delay.
            - Field introduced in 20.1.5.
            - Unit is sec.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 300.
        type: int
    detach_ip_retry_interval:
        description:
            - Amount of time to wait after last detach ip failure before attempting next detach ip retry.
            - Field introduced in 21.1.3.
            - Unit is sec.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 60.
        type: int
    detach_ip_retry_limit:
        description:
            - Maximum number of detach ip retries.
            - Field introduced in 21.1.3.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 4.
        type: int
    detach_ip_timeout:
        description:
            - Time to wait before marking detach ip as failed.
            - Field introduced in 21.1.3.
            - Unit is sec.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 300.
        type: int
    dns_refresh_period:
        description:
            - Period for refresh pool and gslb dns job.
            - Unit is min.
            - Allowed in enterprise edition with any value, essentials edition(allowed values- 60), basic edition(allowed values- 60), enterprise with cloud
            - services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 60.
        type: int
    dummy:
        description:
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: int
    edit_system_limits:
        description:
            - Allow editing of system limits.
            - Keep in mind that these system limits have been carefully selected based on rigorous testing in our testig environments.
            - Modifying these limits could destabilize your cluster.
            - Do this at your own risk!.
            - Field introduced in 20.1.1.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    enable_api_sharding:
        description:
            - This setting enables the controller leader to shard api requests to the followers (if any).
            - Field introduced in 18.1.5, 18.2.1.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as True.
        type: bool
    enable_memory_balancer:
        description:
            - Enable/disable memory balancer.
            - Field introduced in 17.2.8.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as True.
        type: bool
    enable_per_process_stop:
        description:
            - Enable stopping of individual processes if process cross the given threshold limit, even when the total controller memory usage is belowits
            - threshold limit.
            - Field introduced in 21.1.1.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    enable_resmgr_log_cache_print:
        description:
            - Enable printing of cached logs inside resource manager.
            - Used for debugging purposes only.
            - Field introduced in 20.1.6.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    event_manager_max_goroutines:
        description:
            - Maximum number of goroutines for event manager process.
            - Allowed values are 1-64.
            - Field introduced in 30.2.1.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 8.
        type: int
    event_manager_max_subscribers:
        description:
            - Maximum number of subscribers for event manager process.
            - Allowed values are 1-6.
            - Special values are 0 - disabled.
            - Field introduced in 30.2.1.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 5.
        type: int
    event_manager_processing_time_threshold:
        description:
            - Log instances for event manager processing delay; recorded whenever event processing delay exceeds configured interval specified in seconds.
            - Allowed values are 1-5.
            - Special values are 0 - disabled.
            - Field introduced in 30.2.1.
            - Unit is sec.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 4.
        type: int
    false_positive_learning_config:
        description:
            - False positive learning configuration.
            - Field introduced in 22.1.1.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
        type: dict
    fatal_error_lease_time:
        description:
            - Unit is sec.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 120.
        type: int
    federated_datastore_cleanup_duration:
        description:
            - Federated datastore will not cleanup diffs unless they are at least this duration in the past.
            - Field introduced in 20.1.1.
            - Unit is hours.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 120.
        type: int
    file_object_cleanup_period:
        description:
            - Period for file object cleanup job.
            - Field introduced in 20.1.1.
            - Unit is min.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 1440.
        type: int
    file_reference_mappings:
        description:
            - List of mapping for file reference and their absolute path.
            - Field deprecated in 30.2.1.
            - Field introduced in 30.1.1.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
        type: list
        elements: dict
    fileobject_max_file_versions:
        description:
            - This is the max number of file versions that will be retained for a file referenced by the local fileobject.
            - Subsequent uploads of file will result in the file rotation of the older version and the latest version retained.
            - Example  when a file upload is done for the first time, there will be a v1 version.
            - Subsequent uploads will get mapped to v1, v2 and v3 versions.
            - On the fourth upload of the file, the v1 will be file rotated and v2, v3 and v4 will be retained.
            - Allowed values are 1-5.
            - Field introduced in 30.2.1.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 3.
        type: int
    gslb_purge_batch_size:
        description:
            - Batch size for the vs_mgr to perform datastrorecleanup during a gslb purge.
            - Allowed values are 50-1200.
            - Field introduced in 22.1.3.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 1000.
        type: int
    gslb_purge_sleep_time_ms:
        description:
            - Sleep time in the vs_mgr during a federatedpurge rpc call.
            - Allowed values are 50-100.
            - Field introduced in 22.1.3.
            - Unit is milliseconds.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 50.
        type: int
    ignore_vrf_in_networksubnetlist:
        description:
            - Ignore the vrf_context filter for /networksubnetlist api.
            - Field introduced in 22.1.4.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    max_dead_se_in_grp:
        description:
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 1.
        type: int
    max_pcap_per_tenant:
        description:
            - Maximum number of pcap files stored per tenant.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 4.
        type: int
    max_se_spawn_interval_delay:
        description:
            - Maximum delay possible to add to se_spawn_retry_interval after successive se spawn failure.
            - Field introduced in 20.1.1.
            - Unit is sec.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 1800.
        type: int
    max_seq_attach_ip_failures:
        description:
            - Maximum number of consecutive attach ip failures that halts vs placement.
            - Field introduced in 17.2.2.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 3.
        type: int
    max_seq_vnic_failures:
        description:
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 3.
        type: int
    max_threads_cc_vip_bg_worker:
        description:
            - Maximum number of threads in threadpool used by cloud connector ccvipbgworker.
            - Allowed values are 1-100.
            - Field introduced in 20.1.3.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 20.
        type: int
    permission_scoped_shared_admin_networks:
        description:
            - Network and vrfcontext objects from the admin tenant will not be shared to non-admin tenants unless admin permissions are granted.
            - Field introduced in 18.2.7, 20.1.1.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    persistence_key_rotate_period:
        description:
            - Period for rotate app persistence keys job.
            - Allowed values are 1-1051200.
            - Special values are 0 - disabled.
            - Unit is min.
            - Allowed in enterprise edition with any value, essentials edition(allowed values- 0), basic edition(allowed values- 0), enterprise with cloud
            - services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 0.
        type: int
    portal_request_burst_limit:
        description:
            - Burst limit on number of incoming requests.
            - 0 to disable.
            - Field introduced in 20.1.1.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 0.
        type: int
    portal_request_rate_limit:
        description:
            - Maximum average number of requests allowed per second.
            - 0 to disable.
            - Field introduced in 20.1.1.
            - Unit is per_second.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 0.
        type: int
    portal_token:
        description:
            - Token used for uploading tech-support to portal.
            - Field introduced in 16.4.6,17.1.2.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: str
    postgres_vacuum_period:
        description:
            - Period for which postgres vacuum are executed.
            - Allowed values are 30-40320.
            - Special values are 0 - deactivated.
            - Field introduced in 22.1.3.
            - Unit is min.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 20160.
        type: int
    process_locked_useraccounts_timeout_period:
        description:
            - Period for process locked user accounts job.
            - Field introduced in 18.1.1.
            - Unit is min.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 1.
        type: int
    process_pki_profile_timeout_period:
        description:
            - Period for process pki profile job.
            - Field introduced in 18.1.1.
            - Unit is min.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 1440.
        type: int
    query_host_fail:
        description:
            - Unit is sec.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 180.
        type: int
    resmgr_log_caching_period:
        description:
            - Period for each cycle of log caching in resource manager.
            - At the end of each cycle, the in memory cached log history will be cleared.
            - Field introduced in 20.1.5.
            - Unit is sec.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 21600.
        type: int
    restrict_cloud_read_access:
        description:
            - Restrict read access to cloud.
            - Field introduced in 22.1.1.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    safenet_hsm_version:
        description:
            - Version of the safenet package installed on the controller.
            - Field introduced in 16.5.2,17.2.3.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: str
    se_create_timeout:
        description:
            - Unit is sec.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 900.
        type: int
    se_failover_attempt_interval:
        description:
            - Interval between attempting failovers to an se.
            - Unit is sec.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 300.
        type: int
    se_from_marketplace:
        description:
            - This setting decides whether se is to be deployed from the cloud marketplace or to be created by the controller.
            - The setting is applicable only when byol license is selected.
            - Enum options - MARKETPLACE, IMAGE_SE.
            - Field introduced in 18.1.4, 18.2.1.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as IMAGE_SE.
        type: str
    se_offline_del:
        description:
            - Unit is sec.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 172000.
        type: int
    se_spawn_retry_interval:
        description:
            - Default retry period before attempting another service engine spawn in se group.
            - Field introduced in 20.1.1.
            - Unit is sec.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 300.
        type: int
    se_upgrade_flow_cleanup_timeout:
        description:
            - Timeout for flows cleanup by serviceengine during upgrade.internal knob  to be exercised under the surveillance of vmware avi support team.
            - Field introduced in 22.1.1.
            - Unit is sec.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 90.
        type: int
    se_vnic_cooldown:
        description:
            - Unit is sec.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 120.
        type: int
    se_vnic_gc_wait_time:
        description:
            - Duration to wait after last vnic addition before proceeding with vnic garbage collection.
            - Used for testing purposes.
            - Field introduced in 20.1.4.
            - Unit is sec.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 300.
        type: int
    secure_channel_cleanup_timeout:
        description:
            - Period for secure channel cleanup job.
            - Unit is min.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 60.
        type: int
    secure_channel_controller_token_timeout:
        description:
            - Unit is min.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 60.
        type: int
    secure_channel_se_token_timeout:
        description:
            - Unit is min.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 60.
        type: int
    seupgrade_copy_buffer_size:
        description:
            - This parameter defines the buffer size during se image downloads in a segroup.
            - It is used to pace the se downloads so that controller network/cpu bandwidth is a bounded operation.
            - Field introduced in 22.1.4.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 512.
        type: int
    seupgrade_copy_pool_size:
        description:
            - This parameter defines the number of simultaneous se image downloads in a segroup.
            - It is used to pace the se downloads so that controller network/cpu bandwidth is a bounded operation.
            - A value of 0 will disable the pacing scheme and all the se(s) in the segroup will attempt to download the image.
            - Field introduced in 18.2.6.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 5.
        type: int
    seupgrade_fabric_pool_size:
        description:
            - The pool size is used to control the number of concurrent segroup upgrades.
            - This field value takes affect upon controller warm reboot.
            - Allowed values are 2-20.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 20.
        type: int
    seupgrade_segroup_min_dead_timeout:
        description:
            - Time to wait before marking segroup upgrade as stuck.
            - Unit is sec.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 360.
        type: int
    shared_ssl_certificates:
        description:
            - Ssl certificates in the admin tenant can be used in non-admin tenants.
            - Field introduced in 18.2.5.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    skopeo_retry_interval:
        description:
            - Time interval (in seconds) between retires for skopeo commands.
            - Field introduced in 30.1.1.
            - Unit is sec.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 5.
        type: int
    skopeo_retry_limit:
        description:
            - Number of times to try skopeo commands for remote image registries.
            - Field introduced in 30.1.1.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 3.
        type: int
    soft_min_mem_per_se_limit:
        description:
            - Soft limit on the minimum se memory that an se needs to have on se register.
            - Field introduced in 30.1.1.
            - Unit is mb.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 1900.
        type: int
    ssl_certificate_expiry_warning_days:
        description:
            - Number of days for ssl certificate expiry warning.
            - Unit is days.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: list
        elements: int
    system_report_cleanup_interval:
        description:
            - Time in minutes to wait between cleanup of systemreports.
            - Allowed values are 15-300.
            - Field introduced in 22.1.6, 30.2.1.
            - Unit is min.
            - Allowed in enterprise edition with any value, essentials edition with any value, basic edition with any value, enterprise with cloud services
            - edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 60.
        type: int
    system_report_limit:
        description:
            - Number of systemreports retained in the system.
            - Once the number of system reports exceed this threshold, the oldest systemreport will be removed and the latest one retained.
            - I.e.
            - The systemreport will be rotated and the reports don't exceed the threshold.
            - Allowed values are 5-50.
            - Field introduced in 22.1.6, 30.2.1.
            - Allowed in enterprise edition with any value, essentials edition with any value, basic edition with any value, enterprise with cloud services
            - edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 10.
        type: int
    unresponsive_se_reboot:
        description:
            - Unit is sec.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 300.
        type: int
    update_dns_entry_retry_limit:
        description:
            - Number of times to retry a dns entry update/delete operation.
            - Field introduced in 21.1.4.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 3.
        type: int
    update_dns_entry_timeout:
        description:
            - Timeout period for a dns entry update/delete operation.
            - Field introduced in 21.1.4.
            - Unit is sec.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 120.
        type: int
    upgrade_dns_ttl:
        description:
            - Time to account for dns ttl during upgrade.
            - This is in addition to vs_scalein_timeout_for_upgrade in se_group.
            - Field introduced in 17.1.1.
            - Unit is sec.
            - Allowed in enterprise edition with any value, essentials edition(allowed values- 5), basic edition(allowed values- 5), enterprise with cloud
            - services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 5.
        type: int
    upgrade_fat_se_lease_time:
        description:
            - Amount of time controller waits for a large-sized se (>=128gb memory) to reconnect after it is rebooted during upgrade.
            - Field introduced in 18.2.10, 20.1.1.
            - Unit is sec.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 1200.
        type: int
    upgrade_lease_time:
        description:
            - Amount of time controller waits for a regular-sized se (<128gb memory) to reconnect after it is rebooted during upgrade.
            - Starting 18.2.10/20.1.1, the default time has increased from 360 seconds to 600 seconds.
            - Unit is sec.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 600.
        type: int
    upgrade_se_per_vs_scale_ops_txn_time:
        description:
            - This parameter defines the upper-bound value of the vs scale-in or vs scale-out operation executed in the sescalein and sescale context.
            - User can tweak this parameter to a higher value if the segroup gets suspended due to sescalein or sescaleout timeout failure typically associated
            - with high number of vs(es) scaled out.
            - Field introduced in 18.2.10, 20.1.1.
            - Unit is sec.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 3.
        type: int
    url:
        description:
            - Avi controller URL of the object.
        type: str
    user_agent_cache_config:
        description:
            - Configuration for user-agent cache used in bot management.
            - Field introduced in 21.1.1.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
        type: dict
    uuid:
        description:
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
        type: str
    vnic_op_fail_time:
        description:
            - Unit is sec.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 180.
        type: int
    vs_awaiting_se_timeout:
        description:
            - Unit is sec.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 60.
        type: int
    vs_key_rotate_period:
        description:
            - Period for rotate vs keys job.
            - Allowed values are 1-1051200.
            - Special values are 0 - disabled.
            - Unit is min.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 360.
        type: int
    vs_scaleout_ready_check_interval:
        description:
            - Interval for checking scaleout_ready status while controller is waiting for scaleoutready rpc from the service engine.
            - Field introduced in 18.2.2.
            - Unit is sec.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 60.
        type: int
    vs_se_attach_ip_fail:
        description:
            - Time to wait before marking attach ip operation on an se as failed.
            - Field introduced in 17.2.2.
            - Unit is sec.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 600.
        type: int
    vs_se_bootup_fail:
        description:
            - Unit is sec.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 480.
        type: int
    vs_se_bootup_fail_patch:
        description:
            - Wait for longer for patch ses to boot up.
            - Field introduced in 30.2.1.
            - Unit is sec.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 600.
        type: int
    vs_se_create_fail:
        description:
            - Unit is sec.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 1500.
        type: int
    vs_se_ping_fail:
        description:
            - Unit is sec.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 60.
        type: int
    vs_se_vnic_fail:
        description:
            - Unit is sec.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 300.
        type: int
    vs_se_vnic_ip_fail:
        description:
            - Unit is sec.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 120.
        type: int
    vsphere_ha_detection_timeout:
        description:
            - Vsphere ha monitor detection timeout.
            - If vsphere_ha_enabled is true and the controller is not able to reach the se, placement will wait for this duration for vsphere_ha_inprogress to
            - be marked true before taking corrective action.
            - Field introduced in 20.1.7, 21.1.3.
            - Unit is sec.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 120.
        type: int
    vsphere_ha_recovery_timeout:
        description:
            - Vsphere ha monitor recovery timeout.
            - Once vsphere_ha_inprogress is set to true (meaning host failure detected and vsphere ha will recover the service engine), placement will wait for
            - at least this duration for the se to reconnect to the controller before taking corrective action.
            - Field introduced in 20.1.7, 21.1.3.
            - Unit is sec.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 480.
        type: int
    vsphere_ha_timer_interval:
        description:
            - Vsphere ha monitor timer interval for sending cc_check_se_status to cloud connector.
            - Field introduced in 20.1.7, 21.1.3.
            - Unit is sec.
            - Allowed in enterprise edition with any value, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 20.
        type: int
    warmstart_se_reconnect_wait_time:
        description:
            - Unit is sec.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 480.
        type: int
    warmstart_vs_resync_wait_time:
        description:
            - Timeout for warmstart vs resync.
            - Field introduced in 18.1.4, 18.2.1.
            - Unit is sec.
            - Allowed in enterprise edition with any value, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 300.
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

- name: Example to create ControllerProperties object
  vmware.alb.avi_controllerproperties:
    avi_credentials: "{{ avi_credentials }}"
    state: present
    name: sample_controllerproperties
"""

RETURN = '''
obj:
    description: ControllerProperties (api/controllerproperties) object
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
        alert_manager_use_evms=dict(type='bool',),
        allow_admin_network_updates=dict(type='bool',),
        allow_ip_forwarding=dict(type='bool',),
        allow_unauthenticated_apis=dict(type='bool',),
        allow_unauthenticated_nodes=dict(type='bool',),
        api_idle_timeout=dict(type='int',),
        api_perf_logging_threshold=dict(type='int',),
        appviewx_compat_mode=dict(type='bool',),
        async_patch_merge_period=dict(type='int',),
        async_patch_request_cleanup_duration=dict(type='int',),
        attach_ip_retry_interval=dict(type='int',),
        attach_ip_retry_limit=dict(type='int',),
        bm_use_ansible=dict(type='bool',),
        check_vsvip_fqdn_syntax=dict(type='bool',),
        cleanup_expired_authtoken_timeout_period=dict(type='int',),
        cleanup_sessions_timeout_period=dict(type='int',),
        cloud_discovery_interval=dict(type='int',),
        cloud_reconcile=dict(type='bool',),
        cloud_reconcile_interval=dict(type='int',),
        cluster_ip_gratuitous_arp_period=dict(type='int',),
        configpb_attributes=dict(type='dict',),
        consistency_check_timeout_period=dict(type='int',),
        controller_resource_info_collection_period=dict(type='int',),
        crashed_se_reboot=dict(type='int',),
        dead_se_detection_timer=dict(type='int',),
        default_minimum_api_timeout=dict(type='int',),
        del_offline_se_after_reboot_delay=dict(type='int',),
        detach_ip_retry_interval=dict(type='int',),
        detach_ip_retry_limit=dict(type='int',),
        detach_ip_timeout=dict(type='int',),
        dns_refresh_period=dict(type='int',),
        dummy=dict(type='int',),
        edit_system_limits=dict(type='bool',),
        enable_api_sharding=dict(type='bool',),
        enable_memory_balancer=dict(type='bool',),
        enable_per_process_stop=dict(type='bool',),
        enable_resmgr_log_cache_print=dict(type='bool',),
        event_manager_max_goroutines=dict(type='int',),
        event_manager_max_subscribers=dict(type='int',),
        event_manager_processing_time_threshold=dict(type='int',),
        false_positive_learning_config=dict(type='dict',),
        fatal_error_lease_time=dict(type='int',),
        federated_datastore_cleanup_duration=dict(type='int',),
        file_object_cleanup_period=dict(type='int',),
        file_reference_mappings=dict(type='list', elements='dict',),
        fileobject_max_file_versions=dict(type='int',),
        gslb_purge_batch_size=dict(type='int',),
        gslb_purge_sleep_time_ms=dict(type='int',),
        ignore_vrf_in_networksubnetlist=dict(type='bool',),
        max_dead_se_in_grp=dict(type='int',),
        max_pcap_per_tenant=dict(type='int',),
        max_se_spawn_interval_delay=dict(type='int',),
        max_seq_attach_ip_failures=dict(type='int',),
        max_seq_vnic_failures=dict(type='int',),
        max_threads_cc_vip_bg_worker=dict(type='int',),
        permission_scoped_shared_admin_networks=dict(type='bool',),
        persistence_key_rotate_period=dict(type='int',),
        portal_request_burst_limit=dict(type='int',),
        portal_request_rate_limit=dict(type='int',),
        portal_token=dict(type='str', no_log=True,),
        postgres_vacuum_period=dict(type='int',),
        process_locked_useraccounts_timeout_period=dict(type='int',),
        process_pki_profile_timeout_period=dict(type='int',),
        query_host_fail=dict(type='int',),
        resmgr_log_caching_period=dict(type='int',),
        restrict_cloud_read_access=dict(type='bool',),
        safenet_hsm_version=dict(type='str',),
        se_create_timeout=dict(type='int',),
        se_failover_attempt_interval=dict(type='int',),
        se_from_marketplace=dict(type='str',),
        se_offline_del=dict(type='int',),
        se_spawn_retry_interval=dict(type='int',),
        se_upgrade_flow_cleanup_timeout=dict(type='int',),
        se_vnic_cooldown=dict(type='int',),
        se_vnic_gc_wait_time=dict(type='int',),
        secure_channel_cleanup_timeout=dict(type='int',),
        secure_channel_controller_token_timeout=dict(type='int',),
        secure_channel_se_token_timeout=dict(type='int',),
        seupgrade_copy_buffer_size=dict(type='int',),
        seupgrade_copy_pool_size=dict(type='int',),
        seupgrade_fabric_pool_size=dict(type='int',),
        seupgrade_segroup_min_dead_timeout=dict(type='int',),
        shared_ssl_certificates=dict(type='bool',),
        skopeo_retry_interval=dict(type='int',),
        skopeo_retry_limit=dict(type='int',),
        soft_min_mem_per_se_limit=dict(type='int',),
        ssl_certificate_expiry_warning_days=dict(type='list', elements='int',),
        system_report_cleanup_interval=dict(type='int',),
        system_report_limit=dict(type='int',),
        unresponsive_se_reboot=dict(type='int',),
        update_dns_entry_retry_limit=dict(type='int',),
        update_dns_entry_timeout=dict(type='int',),
        upgrade_dns_ttl=dict(type='int',),
        upgrade_fat_se_lease_time=dict(type='int',),
        upgrade_lease_time=dict(type='int',),
        upgrade_se_per_vs_scale_ops_txn_time=dict(type='int',),
        url=dict(type='str',),
        user_agent_cache_config=dict(type='dict',),
        uuid=dict(type='str',),
        vnic_op_fail_time=dict(type='int',),
        vs_awaiting_se_timeout=dict(type='int',),
        vs_key_rotate_period=dict(type='int',),
        vs_scaleout_ready_check_interval=dict(type='int',),
        vs_se_attach_ip_fail=dict(type='int',),
        vs_se_bootup_fail=dict(type='int',),
        vs_se_bootup_fail_patch=dict(type='int',),
        vs_se_create_fail=dict(type='int',),
        vs_se_ping_fail=dict(type='int',),
        vs_se_vnic_fail=dict(type='int',),
        vs_se_vnic_ip_fail=dict(type='int',),
        vsphere_ha_detection_timeout=dict(type='int',),
        vsphere_ha_recovery_timeout=dict(type='int',),
        vsphere_ha_timer_interval=dict(type='int',),
        warmstart_se_reconnect_wait_time=dict(type='int',),
        warmstart_vs_resync_wait_time=dict(type='int',),
    )
    argument_specs.update(avi_common_argument_spec())
    module = AnsibleModule(
        argument_spec=argument_specs, supports_check_mode=True)
    if not HAS_REQUESTS:
        return module.fail_json(msg=(
            'Python requests package is not installed. '
            'For installation instructions, visit https://pypi.org/project/requests.'))
    return avi_ansible_api(module, 'controllerproperties',
                           ['portal_token'])


if __name__ == '__main__':
    main()
