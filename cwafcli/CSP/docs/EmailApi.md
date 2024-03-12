# swagger_client.EmailApi

All URIs are relative to *https://api.imperva.com/csp-api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_email**](EmailApi.md#add_email) | **POST** /v1/sites/{siteId}/settings/emails/add | Add an email address to the notification list
[**get_emails**](EmailApi.md#get_emails) | **GET** /v1/sites/{siteId}/settings/emails | Retrieve the notification recipient list
[**remove_email**](EmailApi.md#remove_email) | **POST** /v1/sites/{siteId}/settings/emails/delete | Delete an email address from the notification list

# **add_email**
> EmailList add_email(body, site_id)

Add an email address to the notification list

Adds an email address to the event notification recipient list for a specific website. Notifications are reasonably small and limited in frequency

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EmailApi()
body = '\"test@imperva.com\"' # str | Email address
site_id = 789 # int | The numeric identifier of the site

try:
    # Add an email address to the notification list
    api_response = api_instance.add_email(body, site_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmailApi->add_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)| Email address | 
 **site_id** | **int**| The numeric identifier of the site | 

### Return type

[**EmailList**](EmailList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../SDK/csp-api/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../SDK/csp-api/README.md#documentation-for-models) [[Back to README]](../../SDK/csp-api/README.md)

# **get_emails**
> list[EmailList] get_emails(site_id)

Retrieve the notification recipient list

Retrieves the list of email addresses that are subscribed to event notifications for a specific website.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EmailApi()
site_id = 789 # int | The numeric identifier of the site

try:
    # Retrieve the notification recipient list
    api_response = api_instance.get_emails(site_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmailApi->get_emails: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **int**| The numeric identifier of the site | 

### Return type

[**list[EmailList]**](EmailList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../SDK/csp-api/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../SDK/csp-api/README.md#documentation-for-models) [[Back to README]](../../SDK/csp-api/README.md)

# **remove_email**
> remove_email(body, site_id)

Delete an email address from the notification list

Removes the email address from the event notification recipient list for a specific website.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EmailApi()
body = '\"test@imperva.com\"' # str | Email address
site_id = 789 # int | The numeric identifier of the site

try:
    # Delete an email address from the notification list
    api_instance.remove_email(body, site_id)
except ApiException as e:
    print("Exception when calling EmailApi->remove_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)| Email address | 
 **site_id** | **int**| The numeric identifier of the site | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../../SDK/csp-api/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../SDK/csp-api/README.md#documentation-for-models) [[Back to README]](../../SDK/csp-api/README.md)

