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
module: avi_cloud
author: Gaurav Rastogi (@grastogi23) <grastogi@avinetworks.com>
short_description: Module for setup of Cloud Avi RESTful Object
description:
    - This module is used to configure Cloud object
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
    autoscale_polling_interval:
        description:
            - Cloudconnector polling interval in seconds for external autoscale groups, minimum 60 seconds.
            - Allowed values are 60-3600.
            - Field introduced in 18.2.2.
            - Unit is seconds.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Allowed in essentials (allowed values- 60), basic (allowed values- 60) edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 60.
        type: int
    aws_configuration:
        description:
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: dict
    azure_configuration:
        description:
            - Field introduced in 17.2.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: dict
    cloudstack_configuration:
        description:
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: dict
    configpb_attributes:
        description:
            - Protobuf versioning for config pbs.
            - Field introduced in 21.1.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: dict
    custom_tags:
        description:
            - Custom tags for all avi created resources in the cloud infrastructure.
            - Field introduced in 17.1.5.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: list
        elements: dict
    dhcp_enabled:
        description:
            - Select the ip address management scheme.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as True.
        type: bool
    dns_provider_ref:
        description:
            - Dns profile for the cloud.
            - It is a reference to an object of type ipamdnsproviderprofile.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: str
    dns_resolution_on_se:
        description:
            - By default, pool member fqdns are resolved on the controller.
            - When this is set, pool member fqdns are instead resolved on service engines in this cloud.
            - This is useful in scenarios where pool member fqdns can only be resolved from service engines and not from the controller.
            - Field introduced in 18.2.6.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Allowed in essentials (allowed values- false), basic (allowed values- false) edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    dns_resolvers:
        description:
            - Dns resolver for the cloud.
            - Field introduced in 20.1.5.
            - Maximum of 1 items allowed.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: list
        elements: dict
    docker_configuration:
        description:
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: dict
    east_west_dns_provider_ref:
        description:
            - Dns profile for east-west services.
            - It is a reference to an object of type ipamdnsproviderprofile.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: str
    east_west_ipam_provider_ref:
        description:
            - Ipam profile for east-west services.
            - Warning - please use virtual subnets in this ipam profile that do not conflict with the underlay networks or any overlay networks in the cluster.
            - For example in aws and gcp, 169.254.0.0/16 is used for storing instance metadata.
            - Hence, it should not be used in this profile.
            - It is a reference to an object of type ipamdnsproviderprofile.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: str
    enable_vip_on_all_interfaces:
        description:
            - Enable vip on all data interfaces for the cloud.
            - Field introduced in 18.2.9, 20.1.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    enable_vip_static_routes:
        description:
            - Use static routes for vip side network resolution during virtualservice placement.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    gcp_configuration:
        description:
            - Google cloud platform configuration.
            - Field introduced in 18.2.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: dict
    ip6_autocfg_enabled:
        description:
            - Enable ipv6 auto configuration.
            - Field introduced in 18.1.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as True.
        type: bool
    ipam_provider_ref:
        description:
            - Ipam profile for the cloud.
            - It is a reference to an object of type ipamdnsproviderprofile.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    license_tier:
        description:
            - Specifies the default license tier which would be used by new se groups.
            - This field by default inherits the value from system configuration.
            - Enum options - ENTERPRISE_16, ENTERPRISE, ENTERPRISE_18, BASIC, ESSENTIALS, ENTERPRISE_WITH_CLOUD_SERVICES.
            - Field introduced in 17.2.5.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    license_type:
        description:
            - If no license type is specified then default license enforcement for the cloud type is chosen.
            - The default mappings are container cloud is max ses, openstack and vmware is cores and linux it is sockets.
            - Enum options - LIC_BACKEND_SERVERS, LIC_SOCKETS, LIC_CORES, LIC_HOSTS, LIC_SE_BANDWIDTH, LIC_METERED_SE_BANDWIDTH.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    linuxserver_configuration:
        description:
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: dict
    maintenance_mode:
        description:
            - Cloud is in maintenance mode.
            - Field introduced in 20.1.7,21.1.3.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    markers:
        description:
            - List of labels to be used for granular rbac.
            - Field introduced in 22.1.1.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: list
        elements: dict
    metrics_polling_interval:
        description:
            - Cloud metrics collector polling interval in seconds.
            - Field introduced in 22.1.1.
            - Unit is seconds.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 300.
        type: int
    mgmt_ip_v4_enabled:
        description:
            - Enable ipv4 on the management interface of the serviceengine.
            - Defaults to dhcp if no static config on network present.
            - Field introduced in 30.2.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as True.
        type: bool
    mgmt_ip_v6_enabled:
        description:
            - Enable ipv6 on the management interface of the serviceengine.
            - Defaults to autocfg if no static config on network present.
            - Field introduced in 30.2.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as True.
        type: bool
    mtu:
        description:
            - Mtu setting for the cloud.
            - Unit is bytes.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as 1500.
        type: int
    name:
        description:
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        required: true
        type: str
    nsxt_configuration:
        description:
            - Nsx-t cloud platform configuration.
            - Field introduced in 20.1.1.
            - Allowed with any value in enterprise, basic, enterprise with cloud services edition.
        type: dict
    ntp_configuration:
        description:
            - Ntp configuration for the cloud.
            - Field introduced in 22.1.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: dict
    obj_name_prefix:
        description:
            - Default prefix for all automatically created objects in this cloud.
            - This prefix can be overridden by the se-group template.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    openstack_configuration:
        description:
            - Field deprecated in 31.1.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: dict
    prefer_static_routes:
        description:
            - Prefer static routes over interface routes during virtualservice placement.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    proxy_configuration:
        description:
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: dict
    rancher_configuration:
        description:
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: dict
    resolve_fqdn_to_ipv6:
        description:
            - Resolve ipv6 address for pool member fqdns.
            - Field introduced in 30.2.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    se_group_template_ref:
        description:
            - The service engine group to use as template.
            - It is a reference to an object of type serviceenginegroup.
            - Field introduced in 18.2.5.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    state_based_dns_registration:
        description:
            - Dns records for vips are added/deleted based on the operational state of the vips.
            - Field introduced in 17.1.12.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Allowed in essentials (allowed values- true), basic (allowed values- true) edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as True.
        type: bool
    tenant_ref:
        description:
            - It is a reference to an object of type tenant.
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    url:
        description:
            - Avi controller URL of the object.
        type: str
    uuid:
        description:
            - Allowed with any value in enterprise, essentials, basic, enterprise with cloud services edition.
        type: str
    vca_configuration:
        description:
            - Allowed with any value in enterprise, enterprise with cloud services edition.
        type: dict
    vcenter_configuration:
        description:
            - Allowed with any value in enterprise, essentials, enterprise with cloud services edition.
        type: dict
    vmc_deployment:
        description:
            - This deployment is vmware on aws cloud.
            - Field introduced in 20.1.5, 21.1.1.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as False.
        type: bool
    vtype:
        description:
            - Cloud type.
            - Enum options - CLOUD_NONE, CLOUD_VCENTER, CLOUD_OPENSTACK, CLOUD_AWS, CLOUD_VCA, CLOUD_APIC, CLOUD_MESOS, CLOUD_LINUXSERVER, CLOUD_DOCKER_UCP,
            - CLOUD_RANCHER, CLOUD_OSHIFT_K8S, CLOUD_AZURE, CLOUD_GCP, CLOUD_NSXT.
            - Allowed with any value in enterprise, enterprise with cloud services edition.
            - Allowed in essentials (allowed values- cloud_none,cloud_vcenter), basic (allowed values- cloud_none,cloud_nsxt) edition.
            - Default value when not specified in API or module is interpreted by Avi Controller as CLOUD_NONE.
        required: true
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

- name: Create a VMware cloud with write access mode
  vmware.alb.avi_cloud:
    avi_credentials: "{{ avi_credentials }}"
    apic_mode: false
    dhcp_enabled: true
    enable_vip_static_routes: false
    license_type: LIC_CORES
    mtu: 1500
    name: VCenter Cloud
    prefer_static_routes: false
    tenant_ref: /api/tenant?name=admin
    vcenter_configuration:
      datacenter_ref: /api/vimgrdcruntime/datacenter-2-10.10.20.100
      management_network: /api/vimgrnwruntime/dvportgroup-103-10.10.20.100
      password: password
      privilege: WRITE_ACCESS
      username: user
      vcenter_url: 192.168.15.18
    vtype: CLOUD_VCENTER
"""

RETURN = '''
obj:
    description: Cloud (api/cloud) object
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
        autoscale_polling_interval=dict(type='int',),
        aws_configuration=dict(type='dict',),
        azure_configuration=dict(type='dict',),
        cloudstack_configuration=dict(type='dict',),
        configpb_attributes=dict(type='dict',),
        custom_tags=dict(type='list', elements='dict',),
        dhcp_enabled=dict(type='bool',),
        dns_provider_ref=dict(type='str',),
        dns_resolution_on_se=dict(type='bool',),
        dns_resolvers=dict(type='list', elements='dict',),
        docker_configuration=dict(type='dict',),
        east_west_dns_provider_ref=dict(type='str',),
        east_west_ipam_provider_ref=dict(type='str',),
        enable_vip_on_all_interfaces=dict(type='bool',),
        enable_vip_static_routes=dict(type='bool',),
        gcp_configuration=dict(type='dict',),
        ip6_autocfg_enabled=dict(type='bool',),
        ipam_provider_ref=dict(type='str',),
        license_tier=dict(type='str',),
        license_type=dict(type='str',),
        linuxserver_configuration=dict(type='dict',),
        maintenance_mode=dict(type='bool',),
        markers=dict(type='list', elements='dict',),
        metrics_polling_interval=dict(type='int',),
        mgmt_ip_v4_enabled=dict(type='bool',),
        mgmt_ip_v6_enabled=dict(type='bool',),
        mtu=dict(type='int',),
        name=dict(type='str', required=True),
        nsxt_configuration=dict(type='dict',),
        ntp_configuration=dict(type='dict',),
        obj_name_prefix=dict(type='str',),
        openstack_configuration=dict(type='dict',),
        prefer_static_routes=dict(type='bool',),
        proxy_configuration=dict(type='dict',),
        rancher_configuration=dict(type='dict',),
        resolve_fqdn_to_ipv6=dict(type='bool',),
        se_group_template_ref=dict(type='str',),
        state_based_dns_registration=dict(type='bool',),
        tenant_ref=dict(type='str',),
        url=dict(type='str',),
        uuid=dict(type='str',),
        vca_configuration=dict(type='dict',),
        vcenter_configuration=dict(type='dict',),
        vmc_deployment=dict(type='bool',),
        vtype=dict(type='str', required=True),
    )
    argument_specs.update(avi_common_argument_spec())
    module = AnsibleModule(
        argument_spec=argument_specs, supports_check_mode=True)
    if not HAS_REQUESTS:
        return module.fail_json(msg=(
            'Python requests package is not installed. '
            'For installation instructions, visit https://pypi.org/project/requests.'))
    return avi_ansible_api(module, 'cloud',
                           set())


if __name__ == '__main__':
    main()
