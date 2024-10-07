# Advanced Load Balancer (formerly Avi) Ansible Collection

[![Apache licensed](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://github.com/vmware/ansible-collection-alb/blob/eng/LICENSE)
[![Collection](https://img.shields.io/badge/collection-vmware.alb-blue.svg)](https://galaxy.ansible.com/vmware/alb/)
[![CI](https://github.com/vmware/ansible-collection-alb/actions/workflows/ci.yaml/badge.svg?branch=)](https://github.com/vmware/ansible-collection-alb/actions/workflows/ci.yaml)

<!--start requires_ansible-->
## Ansible version compatibility

This collection has been tested against following Ansible versions: **>=2.9.10**.

<!--end requires_ansible-->

## Python Support

* Collection supports >= 3.5

## Installation and Usage

Ansible must be installed
```
pip install ansible
```

Install ALB collection using `ansible-galaxy` CLI:
```
ansible-galaxy collection install vmware.alb
```

Install ALB collection using `requirements.yml` file:

Create `requirements.yml` file using below contents
```yaml
collections:
- name: vmware.alb
```

Install the collection:
```
ansible-galaxy collection install -r requirements.yml
```

### Required Python libraries

ALB collection depends upon following third party libraries:

- ovftool Please downlod the ovftool from: https://www.vmware.com/support/developer/ovf

### How to install ovftool
```
cd /home/user/downloads
chmod 755 VMware-ovftool-4.4.0-15722219-lin.x86_64.bundle
sudo ./VMware-ovftool-4.4.0-15722219-lin.x86_64.bundle
```

### Installing required libraries

After ALB collection installation we need to install the required python libraries using following command:
```
pip install -r ~/.ansible/collections/ansible_collections/vmware/alb/requirements.txt
```

### Modules
Name | Description
--- | ---
[vmware.alb.avi_actiongroupconfig](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_actiongroupconfig.rst)|Module to create update or delete ActionGroupConfig
[vmware.alb.avi_albservicesconfig](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_albservicesconfig.rst)|Module to create update or delete ALBServicesConfig
[vmware.alb.avi_albservicesfiledownload](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_albservicesfiledownload.rst)|Module to create update or delete ALBServicesFileDownload
[vmware.alb.avi_albservicesfileupload](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_albservicesfileupload.rst)|Module to create update or delete ALBServicesFileUpload
[vmware.alb.avi_albservicesjob](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_albservicesjob.rst)|Module to create update or delete ALBServicesJob
[vmware.alb.avi_alertconfig](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_alertconfig.rst)|Module to create update or delete AlertConfig
[vmware.alb.avi_alertemailconfig](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_alertemailconfig.rst)|Module to create update or delete AlertEmailConfig
[vmware.alb.avi_alertscriptconfig](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_alertscriptconfig.rst)|Module to create update or delete AlertScriptConfig
[vmware.alb.avi_alertsyslogconfig](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_alertsyslogconfig.rst)|Module to create update or delete AlertSyslogConfig
[vmware.alb.avi_analyticsprofile](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_analyticsprofile.rst)|Module to create update or delete AnalyticsProfile
[vmware.alb.avi_api_fileservice](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_api_fileservice.rst)|Module to create update or delete ApiFileservice
[vmware.alb.avi_api_image](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_api_image.rst)|Module to create update or delete ApiImage
[vmware.alb.avi_api_session](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_api_session.rst)|Module to create update or delete ApiSession
[vmware.alb.avi_api_version](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_api_version.rst)|Module to create update or delete ApiVersion
[vmware.alb.avi_applicationpersistenceprofile](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_applicationpersistenceprofile.rst)|Module to create update or delete ApplicationPersistenceProfile
[vmware.alb.avi_applicationprofile](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_applicationprofile.rst)|Module to create update or delete ApplicationProfile
[vmware.alb.avi_authmappingprofile](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_authmappingprofile.rst)|Module to create update or delete AuthMappingProfile
[vmware.alb.avi_authprofile](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_authprofile.rst)|Module to create update or delete AuthProfile
[vmware.alb.avi_autoscalelaunchconfig](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_autoscalelaunchconfig.rst)|Module to create update or delete AutoScaleLaunchConfig
[vmware.alb.avi_availabilityzone](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_availabilityzone.rst)|Module to create update or delete AvailabilityZone
[vmware.alb.avi_backup](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_backup.rst)|Module to create update or delete Backup
[vmware.alb.avi_backupconfiguration](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_backupconfiguration.rst)|Module to create update or delete BackupConfiguration
[vmware.alb.avi_bootstrap_controller](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_bootstrap_controller.rst)|Module to create update or delete BootstrapController
[vmware.alb.avi_botconfigconsolidator](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_botconfigconsolidator.rst)|Module to create update or delete BotConfigConsolidator
[vmware.alb.avi_botdetectionpolicy](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_botdetectionpolicy.rst)|Module to create update or delete BotDetectionPolicy
[vmware.alb.avi_botipreputationtypemapping](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_botipreputationtypemapping.rst)|Module to create update or delete BotIPReputationTypeMapping
[vmware.alb.avi_botmapping](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_botmapping.rst)|Module to create update or delete BotMapping
[vmware.alb.avi_certificatemanagementprofile](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_certificatemanagementprofile.rst)|Module to create update or delete CertificateManagementProfile
[vmware.alb.avi_cloud](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_cloud.rst)|Module to create update or delete Cloud
[vmware.alb.avi_cloudconnectoruser](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_cloudconnectoruser.rst)|Module to create update or delete CloudConnectorUser
[vmware.alb.avi_cloudproperties](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_cloudproperties.rst)|Module to create update or delete CloudProperties
[vmware.alb.avi_cluster](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_cluster.rst)|Module to create update or delete Cluster
[vmware.alb.avi_clusterclouddetails](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_clusterclouddetails.rst)|Module to create update or delete ClusterCloudDetails
[vmware.alb.avi_controllerportalregistration](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_controllerportalregistration.rst)|Module to create update or delete ControllerPortalRegistration
[vmware.alb.avi_controllerproperties](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_controllerproperties.rst)|Module to create update or delete ControllerProperties
[vmware.alb.avi_controllersite](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_controllersite.rst)|Module to create update or delete ControllerSite
[vmware.alb.avi_csrfpolicy](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_csrfpolicy.rst)|Module to create update or delete CSRFPolicy
[vmware.alb.avi_customipamdnsprofile](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_customipamdnsprofile.rst)|Module to create update or delete CustomIpamDnsProfile
[vmware.alb.avi_deploy_controller](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_deploy_controller.rst)|Module to create update or delete DeployController
[vmware.alb.avi_dnspolicy](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_dnspolicy.rst)|Module to create update or delete DnsPolicy
[vmware.alb.avi_dynamicdnsrecord](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_dynamicdnsrecord.rst)|Module to create update or delete DynamicDnsRecord
[vmware.alb.avi_errorpagebody](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_errorpagebody.rst)|Module to create update or delete ErrorPageBody
[vmware.alb.avi_errorpageprofile](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_errorpageprofile.rst)|Module to create update or delete ErrorPageProfile
[vmware.alb.avi_federationcheckpoint](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_federationcheckpoint.rst)|Module to create update or delete FederationCheckpoint
[vmware.alb.avi_fileobject](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_fileobject.rst)|Module to create update or delete FileObject
[vmware.alb.avi_geodb](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_geodb.rst)|Module to create update or delete GeoDB
[vmware.alb.avi_gslb](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_gslb.rst)|Module to create update or delete Gslb
[vmware.alb.avi_gslbgeodbprofile](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_gslbgeodbprofile.rst)|Module to create update or delete GslbGeoDbProfile
[vmware.alb.avi_gslbservice](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_gslbservice.rst)|Module to create update or delete GslbService
[vmware.alb.avi_gslbservice_patch_member](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_gslbservice_patch_member.rst)|Module to create update or delete GslbservicePatchMember
[vmware.alb.avi_hardwaresecuritymodulegroup](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_hardwaresecuritymodulegroup.rst)|Module to create update or delete HardwareSecurityModuleGroup
[vmware.alb.avi_healthmonitor](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_healthmonitor.rst)|Module to create update or delete HealthMonitor
[vmware.alb.avi_httppolicyset](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_httppolicyset.rst)|Module to create update or delete HTTPPolicySet
[vmware.alb.avi_icapprofile](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_icapprofile.rst)|Module to create update or delete IcapProfile
[vmware.alb.avi_image](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_image.rst)|Module to create update or delete Image
[vmware.alb.avi_inventoryfaultconfig](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_inventoryfaultconfig.rst)|Module to create update or delete InventoryFaultConfig
[vmware.alb.avi_ipaddrgroup](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_ipaddrgroup.rst)|Module to create update or delete IpAddrGroup
[vmware.alb.avi_ipamdnsproviderprofile](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_ipamdnsproviderprofile.rst)|Module to create update or delete IpamDnsProviderProfile
[vmware.alb.avi_ipreputationdb](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_ipreputationdb.rst)|Module to create update or delete IPReputationDB
[vmware.alb.avi_jwtserverprofile](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_jwtserverprofile.rst)|Module to create update or delete JWTServerProfile
[vmware.alb.avi_l4policyset](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_l4policyset.rst)|Module to create update or delete L4PolicySet
[vmware.alb.avi_labelgroup](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_labelgroup.rst)|Module to create update or delete LabelGroup
[vmware.alb.avi_licenseledgerdetails](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_licenseledgerdetails.rst)|Module to create update or delete LicenseLedgerDetails
[vmware.alb.avi_licensestatus](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_licensestatus.rst)|Module to create update or delete LicenseStatus
[vmware.alb.avi_memorybalancerrequest](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_memorybalancerrequest.rst)|Module to create update or delete MemoryBalancerRequest
[vmware.alb.avi_microservicegroup](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_microservicegroup.rst)|Module to create update or delete MicroServiceGroup
[vmware.alb.avi_natpolicy](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_natpolicy.rst)|Module to create update or delete NatPolicy
[vmware.alb.avi_network](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_network.rst)|Module to create update or delete Network
[vmware.alb.avi_networkprofile](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_networkprofile.rst)|Module to create update or delete NetworkProfile
[vmware.alb.avi_networksecuritypolicy](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_networksecuritypolicy.rst)|Module to create update or delete NetworkSecurityPolicy
[vmware.alb.avi_networkservice](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_networkservice.rst)|Module to create update or delete NetworkService
[vmware.alb.avi_nsxtsegmentruntime](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_nsxtsegmentruntime.rst)|Module to create update or delete NsxtSegmentRuntime
[vmware.alb.avi_pkiprofile](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_pkiprofile.rst)|Module to create update or delete PKIProfile
[vmware.alb.avi_pool](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_pool.rst)|Module to create update or delete Pool
[vmware.alb.avi_poolgroup](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_poolgroup.rst)|Module to create update or delete PoolGroup
[vmware.alb.avi_poolgroupdeploymentpolicy](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_poolgroupdeploymentpolicy.rst)|Module to create update or delete PoolGroupDeploymentPolicy
[vmware.alb.avi_prioritylabels](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_prioritylabels.rst)|Module to create update or delete PriorityLabels
[vmware.alb.avi_protocolparser](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_protocolparser.rst)|Module to create update or delete ProtocolParser
[vmware.alb.avi_pulse_registration](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_pulse_registration.rst)|Module to create update or delete PulseRegistration
[vmware.alb.avi_role](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_role.rst)|Module to create update or delete Role
[vmware.alb.avi_saml_api_session](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_saml_api_session.rst)|Module to create update or delete SamlApiSession
[vmware.alb.avi_scheduler](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_scheduler.rst)|Module to create update or delete Scheduler
[vmware.alb.avi_securitymanagerdata](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_securitymanagerdata.rst)|Module to create update or delete SecurityManagerData
[vmware.alb.avi_securitypolicy](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_securitypolicy.rst)|Module to create update or delete SecurityPolicy
[vmware.alb.avi_seproperties](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_seproperties.rst)|Module to create update or delete SeProperties
[vmware.alb.avi_serverautoscalepolicy](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_serverautoscalepolicy.rst)|Module to create update or delete ServerAutoScalePolicy
[vmware.alb.avi_serviceauthprofile](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_serviceauthprofile.rst)|Module to create update or delete ServiceAuthProfile
[vmware.alb.avi_serviceengine](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_serviceengine.rst)|Module to create update or delete ServiceEngine
[vmware.alb.avi_serviceenginegroup](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_serviceenginegroup.rst)|Module to create update or delete Serviceenginegroup
[vmware.alb.avi_serviceenginegroup](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_serviceenginegroup.rst)|Module to create update or delete ServiceEngineGroup
[vmware.alb.avi_serviceenginegroup_advanced](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_serviceenginegroup_advanced.rst)|Module to create update or delete ServiceenginegroupAdvanced
[vmware.alb.avi_siteversion](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_siteversion.rst)|Module to create update or delete SiteVersion
[vmware.alb.avi_snmptrapprofile](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_snmptrapprofile.rst)|Module to create update or delete SnmpTrapProfile
[vmware.alb.avi_sslkeyandcertificate](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_sslkeyandcertificate.rst)|Module to create update or delete SSLKeyAndCertificate
[vmware.alb.avi_sslprofile](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_sslprofile.rst)|Module to create update or delete SSLProfile
[vmware.alb.avi_ssopolicy](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_ssopolicy.rst)|Module to create update or delete SSOPolicy
[vmware.alb.avi_statediffoperation](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_statediffoperation.rst)|Module to create update or delete StatediffOperation
[vmware.alb.avi_statediffsnapshot](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_statediffsnapshot.rst)|Module to create update or delete StatediffSnapshot
[vmware.alb.avi_stringgroup](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_stringgroup.rst)|Module to create update or delete StringGroup
[vmware.alb.avi_systemconfiguration](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_systemconfiguration.rst)|Module to create update or delete SystemConfiguration
[vmware.alb.avi_systemlimits](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_systemlimits.rst)|Module to create update or delete SystemLimits
[vmware.alb.avi_systemreport](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_systemreport.rst)|Module to create update or delete SystemReport
[vmware.alb.avi_taskjournal](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_taskjournal.rst)|Module to create update or delete TaskJournal
[vmware.alb.avi_tenant](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_tenant.rst)|Module to create update or delete Tenant
[vmware.alb.avi_tenantsystemconfiguration](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_tenantsystemconfiguration.rst)|Module to create update or delete TenantSystemConfiguration
[vmware.alb.avi_testsedatastorelevel1](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_testsedatastorelevel1.rst)|Module to create update or delete TestSeDatastoreLevel1
[vmware.alb.avi_testsedatastorelevel2](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_testsedatastorelevel2.rst)|Module to create update or delete TestSeDatastoreLevel2
[vmware.alb.avi_testsedatastorelevel3](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_testsedatastorelevel3.rst)|Module to create update or delete TestSeDatastoreLevel3
[vmware.alb.avi_trafficcloneprofile](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_trafficcloneprofile.rst)|Module to create update or delete TrafficCloneProfile
[vmware.alb.avi_trustedhostprofile](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_trustedhostprofile.rst)|Module to create update or delete TrustedHostProfile
[vmware.alb.avi_update_se_data_vnics](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_update_se_data_vnics.rst)|Module to create update or delete UpdateSeDataVnics
[vmware.alb.avi_upgradestatusinfo](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_upgradestatusinfo.rst)|Module to create update or delete UpgradeStatusInfo
[vmware.alb.avi_upgradestatussummary](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_upgradestatussummary.rst)|Module to create update or delete UpgradeStatusSummary
[vmware.alb.avi_user](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_user.rst)|Module to create update or delete User
[vmware.alb.avi_useraccount](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_useraccount.rst)|Module to create update or delete Useraccount
[vmware.alb.avi_useraccountprofile](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_useraccountprofile.rst)|Module to create update or delete UserAccountProfile
[vmware.alb.avi_vcenterserver](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_vcenterserver.rst)|Module to create update or delete VCenterServer
[vmware.alb.avi_virtualservice](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_virtualservice.rst)|Module to create update or delete VirtualService
[vmware.alb.avi_vrfcontext](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_vrfcontext.rst)|Module to create update or delete VrfContext
[vmware.alb.avi_vsdatascriptset](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_vsdatascriptset.rst)|Module to create update or delete VSDataScriptSet
[vmware.alb.avi_vsgs](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_vsgs.rst)|Module to create update or delete VsGs
[vmware.alb.avi_vsvip](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_vsvip.rst)|Module to create update or delete VsVip
[vmware.alb.avi_wafapplicationsignatureprovider](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_wafapplicationsignatureprovider.rst)|Module to create update or delete WafApplicationSignatureProvider
[vmware.alb.avi_wafpolicy](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_wafpolicy.rst)|Module to create update or delete WafPolicy
[vmware.alb.avi_wafpolicypsmgroup](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_wafpolicypsmgroup.rst)|Module to create update or delete WafPolicyPSMGroup
[vmware.alb.avi_wafprofile](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_wafprofile.rst)|Module to create update or delete WafProfile
[vmware.alb.avi_webapput](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_webapput.rst)|Module to create update or delete WebappUT
[vmware.alb.avi_webhook](https://github.com/vmware/ansible-collection-alb/blob//docs/avi_webhook.rst)|Module to create update or delete Webhook
<!--end collection content-->

### Testing with `ansible-test`

Refer [testing](https://github.com/vmware/ansible-collection-alb/blob//testing.md) for more information.

## Publishing New Version

Examples
--------

    - hosts: localhost
      connection: local
      collections:
        - vmware.alb
      tasks:
        - name: Example to create a Pool object
          avi_pool:
            avi_credentials:
              username: "admin"
              password: "something"
              controller: "192.168.15.18"
              api_version: "21.1.1"
            name: app1-pool
            lb_algorithm: LB_ALGORITHM_LEAST_LOAD
            servers:
            - ip:
                 addr: "192.168.12.15"
                 type: 'V4'

Example usage of external credentials/variable file while using alb module
```
# creds.yml
avi_credentials:
    controller: "192.168.1.11"
    username: "admin"
    password: "password"
    api_version: 20.1.5
```
```
# example.yml
- hosts: localhost
  connection: local
  collections:
    - vmware.alb
  vars_files:
    - creds.yml
  tasks:
    - name: Example to create a Pool object
      avi_pool:
        avi_credentials: "{{ avi_credentials |  default(omit) }}"
        name: app1-pool
        lb_algorithm: LB_ALGORITHM_LEAST_LOAD
        servers:
        - ip:
             addr: "192.168.12.15"
             type: 'V4'
```
Example for using aviconfig role:
```
# config.yml
avi_config:
  pool:
    - name: role1-pool
      lb_algorithm: LB_ALGORITHM_LEAST_LOAD
      servers:
        - ip:
             addr: 192.160.1.10
             type: 'V4'
```
```
# collection.yml
- hosts: localhost
  connection: local
  collections:
    - vmware.alb
  tasks:
    - name: Create pool using aviconfig role
      import_role:
        name: aviconfig
      vars:
          avi_config_file: "config.yml"
          avi_creds_file: "creds.yml"
          # avi_creds_file parameter is only valid for aviconfig role.
          # For importing credentials from external file in modules,
          # please use vars_files parameter as shown in previous example
```

**Notes**
Please use Python >= 3.8 if you are using avi_serviceenginegroup module as it has more than 255 arguments
