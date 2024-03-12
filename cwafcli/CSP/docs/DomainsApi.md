# swagger_client.DomainsApi

All URIs are relative to *https://api.imperva.com/csp-api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_domain**](DomainsApi.md#get_domain) | **GET** /v1/sites/{siteId}/domains/{domainId} | Retrieve information about specific domain
[**get_domain_allowance**](DomainsApi.md#get_domain_allowance) | **GET** /v1/sites/{siteId}/domains/{domainId}/status | Retrieve status details of a discovered domain
[**get_domains**](DomainsApi.md#get_domains) | **GET** /v1/sites/{siteId}/domains | Retrieve list of all discovered domains
[**set_domain_allowance**](DomainsApi.md#set_domain_allowance) | **PUT** /v1/sites/{siteId}/domains/{domainId}/status | Overwrite status of the a discovered domain

# **get_domain**
> Domain get_domain(site_id, domain_id)

Retrieve information about specific domain

Get full information about the domain and its status. If the API key used is for a parent account, and the website belongs to a sub account, the caid of the sub account must be specified.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DomainsApi()
site_id = 789 # int | The numeric identifier of the site
domain_id = 'domain_id_example' # str | Domain reference id as received from getDomains operation

try:
    # Retrieve information about specific domain
    api_response = api_instance.get_domain(site_id, domain_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainsApi->get_domain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **int**| The numeric identifier of the site | 
 **domain_id** | **str**| Domain reference id as received from getDomains operation | 

### Return type

[**Domain**](Domain.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../SDK/csp-api/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../SDK/csp-api/README.md#documentation-for-models) [[Back to README]](../../SDK/csp-api/README.md)

# **get_domain_allowance**
> DomainStatus get_domain_allowance(site_id, domain_id)

Retrieve status details of a discovered domain

Retrieves status details of the domain including whether the domain is blocked or allowed, and reviewed or unreviewed.   When the website is in \"enforce\" mode, all requests from the website to blocked domains are blocked.    By default, all newly discovered domains are allowed if the website is in \"monitor\" mode, and blocked if the website is in \"enforce\" mode. If the API key used is for a parent account, and the website belongs to a sub account, the caid of the sub account must be specified.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DomainsApi()
site_id = 789 # int | The numeric identifier of the site
domain_id = 'domain_id_example' # str | Domain reference id as received from getDomains operation.

try:
    # Retrieve status details of a discovered domain
    api_response = api_instance.get_domain_allowance(site_id, domain_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainsApi->get_domain_allowance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **int**| The numeric identifier of the site | 
 **domain_id** | **str**| Domain reference id as received from getDomains operation. | 

### Return type

[**DomainStatus**](DomainStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../SDK/csp-api/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../SDK/csp-api/README.md#documentation-for-models) [[Back to README]](../../SDK/csp-api/README.md)

# **get_domains**
> list[Domain] get_domains(site_id, significant=significant, expand=expand, resource=resource, start=start, length=length)

Retrieve list of all discovered domains

Every domain accessed from the site is recorded in this list. Client-Side Protection gathers all available information the domain to help with analysis. If the API key used is for a parent account, and the website belongs to a sub account, the caid of the sub account must be specified.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DomainsApi()
site_id = 789 # int | The numeric identifier of the site
significant = true # bool | Show only significant domains. If the service is part of the profile and/or frequently requested. The two values are 1 or 0. 1 = significant. 0 = not significant. (optional)
expand = true # bool | Expand domain object to include additional information. Adds #domainInfo and #domainReports fields. (optional)
resource = 'resource_example' # str | Show only domains with specific resource type (optional)
start = -1 # int | Start index of domains (optional) (default to -1)
length = -1 # int | Length of requested domains (optional) (default to -1)

try:
    # Retrieve list of all discovered domains
    api_response = api_instance.get_domains(site_id, significant=significant, expand=expand, resource=resource, start=start, length=length)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainsApi->get_domains: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **int**| The numeric identifier of the site | 
 **significant** | **bool**| Show only significant domains. If the service is part of the profile and/or frequently requested. The two values are 1 or 0. 1 &#x3D; significant. 0 &#x3D; not significant. | [optional] 
 **expand** | **bool**| Expand domain object to include additional information. Adds #domainInfo and #domainReports fields. | [optional] 
 **resource** | **str**| Show only domains with specific resource type | [optional] 
 **start** | **int**| Start index of domains | [optional] [default to -1]
 **length** | **int**| Length of requested domains | [optional] [default to -1]

### Return type

[**list[Domain]**](Domain.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../SDK/csp-api/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../SDK/csp-api/README.md#documentation-for-models) [[Back to README]](../../SDK/csp-api/README.md)

# **set_domain_allowance**
> DomainStatus set_domain_allowance(body, site_id, domain_id)

Overwrite status of the a discovered domain

Sets the domain status to block or allow.   When the website is in \"enforce\" mode, all requests from the website to blocked domains are blocked.    By default, all newly discovered domains are allowed if the website is in \"monitor\" mode, and blocked if the website is in \"enforce\" mode. If the API key used is for a parent account, and the website belongs to a sub account, the caid of the sub account must be specified.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DomainsApi()
body = swagger_client.DomainStatus() # DomainStatus | 
site_id = 789 # int | The numeric identifier of the site
domain_id = 'domain_id_example' # str | Domain reference id as received from getDomains operation

try:
    # Overwrite status of the a discovered domain
    api_response = api_instance.set_domain_allowance(body, site_id, domain_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DomainsApi->set_domain_allowance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DomainStatus**](DomainStatus.md)|  | 
 **site_id** | **int**| The numeric identifier of the site | 
 **domain_id** | **str**| Domain reference id as received from getDomains operation | 

### Return type

[**DomainStatus**](DomainStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../SDK/csp-api/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../SDK/csp-api/README.md#documentation-for-models) [[Back to README]](../../SDK/csp-api/README.md)

