# Domain

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Domain reference id used in different operations. | [optional] 
**domain** | **str** | Domain name | [optional] 
**status** | [**DomainStatus**](DomainStatus.md) |  | [optional] 
**domain_risk** | [**DomainRisk**](DomainRisk.md) |  | [optional] 
**notes** | [**list[FullNote]**](FullNote.md) | List of notes associated with the domain. Added by the API user as a quick note for convenience. | [optional] 
**time_bucket** | **int** |  | [optional] 
**significance** | **int** | If the service is part of the profile and/or frequently requested. The two values are 1 or 0. 1 &#x3D; significant. 0 &#x3D; not significant. | [optional] 
**resource_types** | **list[str]** |  | [optional] 
**browser_stats** | **dict(str, int)** | Statistics of browsers of clients that used the domain. | [optional] 
**country_stats** | **dict(str, int)** | Statistics of countries of clients that used the domain. | [optional] 
**ips_sample** | **list[str]** | A sample of IP sources detected in the CSP reports. | [optional] 
**sources** | **int** | IP sources detected in the sampled CSP reports. | [optional] 
**frequent** | **bool** | If the service is frequently requested. | [optional] 
**part_of_profile** | **bool** | Domain is likely a part of the profile. The profile is the list of domains and services that are embedded in the website, directly or through 3rd-party dependency. | [optional] 
**discovered_at** | **int** | Date when domain was discovered in milliseconds. | [optional] 
**last_seen_ms** | **int** | Date when domain was last seen in milliseconds. | [optional] 
**domain_info** | [**DomainInfo**](DomainInfo.md) |  | [optional] 
**domain_reports** | [**list[DomainReport]**](DomainReport.md) | Aggregated domain report data. | [optional] 
**obfuscation_report** | [**DomainObfuscationReport**](DomainObfuscationReport.md) |  | [optional] 
**domain_popularity** | **str** | Domain popularity. | [optional] 
**instant_block_enabled** | **bool** | Indicates whether or not Instant Block is enabled for this domain. | [optional] 

[[Back to Model list]](../../SDK/csp-api/README.md#documentation-for-models) [[Back to API list]](../../SDK/csp-api/README.md#documentation-for-api-endpoints) [[Back to README]](../../SDK/csp-api/README.md)

