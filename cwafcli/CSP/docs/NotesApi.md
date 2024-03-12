# swagger_client.NotesApi

All URIs are relative to *https://api.imperva.com/csp-api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_domain_note**](NotesApi.md#add_domain_note) | **POST** /v1/sites/{siteId}/domains/{domainId}/notes | Add notes to a discovered domain.
[**delete_note**](NotesApi.md#delete_note) | **DELETE** /v1/sites/{siteId}/domains/{domainId}/notes | Delete notes from a discovered domain
[**get_domain_notes**](NotesApi.md#get_domain_notes) | **GET** /v1/sites/{siteId}/domains/{domainId}/notes | Retrieve user notes for a discovered domain

# **add_domain_note**
> list[FullNote] add_domain_note(body, site_id, domain_id)

Add notes to a discovered domain.

Add a quick note to a domain to help in future analysis and investigation. You can add as many notes as you like. If the API key used is for a parent account, and the website belongs to a sub account, the caid of the sub account must be specified.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NotesApi()
body = '\"Review domain later.\"' # str | Content of the note.
site_id = 789 # int | The numeric identifier of the site
domain_id = 'domain_id_example' # str | Domain reference id as received from getDomains operation.

try:
    # Add notes to a discovered domain.
    api_response = api_instance.add_domain_note(body, site_id, domain_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotesApi->add_domain_note: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)| Content of the note. | 
 **site_id** | **int**| The numeric identifier of the site | 
 **domain_id** | **str**| Domain reference id as received from getDomains operation. | 

### Return type

[**list[FullNote]**](FullNote.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../SDK/csp-api/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../SDK/csp-api/README.md#documentation-for-models) [[Back to README]](../../SDK/csp-api/README.md)

# **delete_note**
> delete_note(site_id, domain_id)

Delete notes from a discovered domain

Delete all notes for a domain. All notes attached to a domain will be removed! If the API key used is for a parent account, and the website belongs to a sub account, the caid of the sub account must be specified.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NotesApi()
site_id = 789 # int | The numeric identifier of the site
domain_id = 'domain_id_example' # str | Domain reference id as received from getDomains operation

try:
    # Delete notes from a discovered domain
    api_instance.delete_note(site_id, domain_id)
except ApiException as e:
    print("Exception when calling NotesApi->delete_note: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **int**| The numeric identifier of the site | 
 **domain_id** | **str**| Domain reference id as received from getDomains operation | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../../SDK/csp-api/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../SDK/csp-api/README.md#documentation-for-models) [[Back to README]](../../SDK/csp-api/README.md)

# **get_domain_notes**
> list[FullNote] get_domain_notes(site_id, domain_id)

Retrieve user notes for a discovered domain

Retrieves the list of user-added notes for a domain aimed to help in future analysis in investigation If the API key used is for a parent account, and the website belongs to a sub account, the caid of the sub account must be specified.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NotesApi()
site_id = 789 # int | The numeric identifier of the site
domain_id = 'domain_id_example' # str | Domain reference id as received from getDomains operation

try:
    # Retrieve user notes for a discovered domain
    api_response = api_instance.get_domain_notes(site_id, domain_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NotesApi->get_domain_notes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **int**| The numeric identifier of the site | 
 **domain_id** | **str**| Domain reference id as received from getDomains operation | 

### Return type

[**list[FullNote]**](FullNote.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../SDK/csp-api/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../SDK/csp-api/README.md#documentation-for-models) [[Back to README]](../../SDK/csp-api/README.md)

