# swagger_client.PreApprovedDomainsApi

All URIs are relative to *https://api.imperva.com/csp-api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_pre_approved_domain**](PreApprovedDomainsApi.md#add_pre_approved_domain) | **POST** /v1/sites/{siteId}/preapprovedlist | Add a domain to pre-approved list
[**delete_pre_approved_domain**](PreApprovedDomainsApi.md#delete_pre_approved_domain) | **DELETE** /v1/sites/{siteId}/preapprovedlist/{preApprovedDomainId} | Delete the pre-approved domain
[**get_pre_approved_domain**](PreApprovedDomainsApi.md#get_pre_approved_domain) | **GET** /v1/sites/{siteId}/preapprovedlist/{preApprovedDomainId} | Retrieve the pre-approved domain
[**get_pre_approved_domains**](PreApprovedDomainsApi.md#get_pre_approved_domains) | **GET** /v1/sites/{siteId}/preapprovedlist | Retrieve list of pre-approved domains

# **add_pre_approved_domain**
> PreApprovedDomain add_pre_approved_domain(body, site_id)

Add a domain to pre-approved list

Adds a known domain to a pre-approved list.   When the domain is discovered by Client-Side Protection, it is automatically approved and marked as Allowed.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PreApprovedDomainsApi()
body = swagger_client.ShallowPreApprovedDomain() # ShallowPreApprovedDomain | The known domain user wants to pre-approve
site_id = 789 # int | The numeric identifier of the site

try:
    # Add a domain to pre-approved list
    api_response = api_instance.add_pre_approved_domain(body, site_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PreApprovedDomainsApi->add_pre_approved_domain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ShallowPreApprovedDomain**](ShallowPreApprovedDomain.md)| The known domain user wants to pre-approve | 
 **site_id** | **int**| The numeric identifier of the site | 

### Return type

[**PreApprovedDomain**](PreApprovedDomain.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../SDK/csp-api/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../SDK/csp-api/README.md#documentation-for-models) [[Back to README]](../../SDK/csp-api/README.md)

# **delete_pre_approved_domain**
> delete_pre_approved_domain(site_id, pre_approved_domain_id)

Delete the pre-approved domain

Removes the domain from the pre-approved list.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PreApprovedDomainsApi()
site_id = 789 # int | The numeric identifier of the site
pre_approved_domain_id = 'pre_approved_domain_id_example' # str | The Imperva domain ID of the pre-approved domain. You can retrieve the domain ID using the GET HTTP method.)

try:
    # Delete the pre-approved domain
    api_instance.delete_pre_approved_domain(site_id, pre_approved_domain_id)
except ApiException as e:
    print("Exception when calling PreApprovedDomainsApi->delete_pre_approved_domain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **int**| The numeric identifier of the site | 
 **pre_approved_domain_id** | **str**| The Imperva domain ID of the pre-approved domain. You can retrieve the domain ID using the GET HTTP method.) | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../../SDK/csp-api/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../SDK/csp-api/README.md#documentation-for-models) [[Back to README]](../../SDK/csp-api/README.md)

# **get_pre_approved_domain**
> PreApprovedDomain get_pre_approved_domain(site_id, pre_approved_domain_id)

Retrieve the pre-approved domain

Retrieve the domain from the pre-approved list.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PreApprovedDomainsApi()
site_id = 789 # int | The numeric identifier of the site
pre_approved_domain_id = 'pre_approved_domain_id_example' # str | The Imperva domain ID of the pre-approved domain. You can retrieve the domain ID using the GET HTTP method.)

try:
    # Retrieve the pre-approved domain
    api_response = api_instance.get_pre_approved_domain(site_id, pre_approved_domain_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PreApprovedDomainsApi->get_pre_approved_domain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **int**| The numeric identifier of the site | 
 **pre_approved_domain_id** | **str**| The Imperva domain ID of the pre-approved domain. You can retrieve the domain ID using the GET HTTP method.) | 

### Return type

[**PreApprovedDomain**](PreApprovedDomain.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../SDK/csp-api/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../SDK/csp-api/README.md#documentation-for-models) [[Back to README]](../../SDK/csp-api/README.md)

# **get_pre_approved_domains**
> list[PreApprovedDomain] get_pre_approved_domains(site_id)

Retrieve list of pre-approved domains

Retrieves the list of domains approved by user before they were discovered by the system.   When these domains are discovered by Client-Side Protection, they are automatically approved and marked as Allowed.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PreApprovedDomainsApi()
site_id = 789 # int | The numeric identifier of the site

try:
    # Retrieve list of pre-approved domains
    api_response = api_instance.get_pre_approved_domains(site_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PreApprovedDomainsApi->get_pre_approved_domains: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **int**| The numeric identifier of the site | 

### Return type

[**list[PreApprovedDomain]**](PreApprovedDomain.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../SDK/csp-api/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../SDK/csp-api/README.md#documentation-for-models) [[Back to README]](../../SDK/csp-api/README.md)

