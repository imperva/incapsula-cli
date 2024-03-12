# swagger_client.WebsitesApi

All URIs are relative to *https://api.imperva.com/csp-api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_discovery_status**](WebsitesApi.md#get_discovery_status) | **GET** /v1/sites/{siteId}/discovery | Retrieve discovery status of a website
[**get_enforcement_mode**](WebsitesApi.md#get_enforcement_mode) | **GET** /v1/sites/{siteId}/mode | Retrieve protection mode of a website
[**get_google_tracking_ids**](WebsitesApi.md#get_google_tracking_ids) | **GET** /v1/sites/{siteId}/tracking-ids | Retrieve list of Google tracking IDs detected for this website
[**get_site**](WebsitesApi.md#get_site) | **GET** /v1/sites/{siteId} | Retrieve website configuration and status details
[**get_site_reputation**](WebsitesApi.md#get_site_reputation) | **GET** /v1/sites/{siteId}/domain_reputation | Retrieve Osint scores for this website
[**get_site_settings**](WebsitesApi.md#get_site_settings) | **GET** /v1/sites/{siteId}/settings | Retrieve website settings
[**get_sites**](WebsitesApi.md#get_sites) | **GET** /v1/sites | Retrieve all websites for current account
[**set_discovery_status**](WebsitesApi.md#set_discovery_status) | **PUT** /v1/sites/{siteId}/discovery | Change discovery status of a website
[**set_enforcement_mode**](WebsitesApi.md#set_enforcement_mode) | **PUT** /v1/sites/{siteId}/mode | Change protection mode of a website
[**set_site**](WebsitesApi.md#set_site) | **PUT** /v1/sites/{siteId} | Change website configuration and status details

# **get_discovery_status**
> DiscoveryStatus get_discovery_status(site_id)

Retrieve discovery status of a website

Indicates if Client-Side Protection discovery is active or suspended.    When paused, Client-Side Protection stops monitoring for new domains and doesn’t inject the Content-Security-Policy header in the website response. You can still review domains and update the website settings. If the API key used is for a parent account, and the website belongs to a sub account, the caid of the sub account must be specified.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WebsitesApi()
site_id = 789 # int | The numeric identifier of the site.

try:
    # Retrieve discovery status of a website
    api_response = api_instance.get_discovery_status(site_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebsitesApi->get_discovery_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **int**| The numeric identifier of the site. | 

### Return type

[**DiscoveryStatus**](DiscoveryStatus.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../SDK/csp-api/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../SDK/csp-api/README.md#documentation-for-models) [[Back to README]](../../SDK/csp-api/README.md)

# **get_enforcement_mode**
> Mode get_enforcement_mode(site_id)

Retrieve protection mode of a website

Retrieves the protection mode of a website.    When in Enforce Mode, all resources you set to Block are not available in your application and new resources are automatically blocked. If the API key used is for a parent account, and the website belongs to a sub account, the caid of the sub account must be specified.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WebsitesApi()
site_id = 789 # int | The numeric identifier of the site.

try:
    # Retrieve protection mode of a website
    api_response = api_instance.get_enforcement_mode(site_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebsitesApi->get_enforcement_mode: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **int**| The numeric identifier of the site. | 

### Return type

[**Mode**](Mode.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../SDK/csp-api/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../SDK/csp-api/README.md#documentation-for-models) [[Back to README]](../../SDK/csp-api/README.md)

# **get_google_tracking_ids**
> list[Analytics] get_google_tracking_ids(site_id)

Retrieve list of Google tracking IDs detected for this website

Retrieves the list of Google Analytics tracking IDs that were detected, indicating which account Google Analytics data is being sent to from your website.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WebsitesApi()
site_id = 789 # int | The numeric identifier of the site

try:
    # Retrieve list of Google tracking IDs detected for this website
    api_response = api_instance.get_google_tracking_ids(site_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebsitesApi->get_google_tracking_ids: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **int**| The numeric identifier of the site | 

### Return type

[**list[Analytics]**](Analytics.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../SDK/csp-api/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../SDK/csp-api/README.md#documentation-for-models) [[Back to README]](../../SDK/csp-api/README.md)

# **get_site**
> Site get_site(site_id)

Retrieve website configuration and status details

Retrieves Client-Side Protection configuration and status details for a specific website. If the API key used is for a parent account, and the website belongs to a sub account, the caid of the sub account must be specified.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WebsitesApi()
site_id = 789 # int | The numeric identifier of the site.

try:
    # Retrieve website configuration and status details
    api_response = api_instance.get_site(site_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebsitesApi->get_site: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **int**| The numeric identifier of the site. | 

### Return type

[**Site**](Site.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../SDK/csp-api/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../SDK/csp-api/README.md#documentation-for-models) [[Back to README]](../../SDK/csp-api/README.md)

# **get_site_reputation**
> SiteReputation get_site_reputation(site_id)

Retrieve Osint scores for this website

Retrieves Osint scores for each domain from Osint Domain Reputation Service for this website, Osint score indicates the risk level of a domain.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WebsitesApi()
site_id = 789 # int | The numeric identifier of the site

try:
    # Retrieve Osint scores for this website
    api_response = api_instance.get_site_reputation(site_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebsitesApi->get_site_reputation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **int**| The numeric identifier of the site | 

### Return type

[**SiteReputation**](SiteReputation.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../SDK/csp-api/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../SDK/csp-api/README.md#documentation-for-models) [[Back to README]](../../SDK/csp-api/README.md)

# **get_site_settings**
> SiteSettings get_site_settings(site_id)

Retrieve website settings

Retrieves Client-Side Protection settings for a specific website, such as the list of email address in the event notification recipient list. If the API key used is for a parent account, and the website belongs to a sub account, the caid of the sub account must be specified.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WebsitesApi()
site_id = 789 # int | The numeric identifier of the site.

try:
    # Retrieve website settings
    api_response = api_instance.get_site_settings(site_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebsitesApi->get_site_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **int**| The numeric identifier of the site. | 

### Return type

[**SiteSettings**](SiteSettings.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../SDK/csp-api/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../SDK/csp-api/README.md#documentation-for-models) [[Back to README]](../../SDK/csp-api/README.md)

# **get_sites**
> dict(str, Site) get_sites()

Retrieve all websites for current account

Retrieves the list of all websites in your account, as well as their Client-Side Protection configuration and status details. If the API key used is for a parent account, and the website belongs to a sub account, the caid of the sub account must be specified.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WebsitesApi()

try:
    # Retrieve all websites for current account
    api_response = api_instance.get_sites()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebsitesApi->get_sites: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**dict(str, Site)**](Site.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../SDK/csp-api/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../SDK/csp-api/README.md#documentation-for-models) [[Back to README]](../../SDK/csp-api/README.md)

# **set_discovery_status**
> Discovery set_discovery_status(body, site_id)

Change discovery status of a website

Suspend or restart the discovery of new services.    When paused, Client-Side Protection stops monitoring for new domains and doesn’t inject the Content-Security-Policy header in the website response. You can still review domains and update the website settings. If the API key used is for a parent account, and the website belongs to a sub account, the caid of the sub account must be specified.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WebsitesApi()
body = 'body_example' # str | discovery status
site_id = 789 # int | The numeric identifier of the site.

try:
    # Change discovery status of a website
    api_response = api_instance.set_discovery_status(body, site_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebsitesApi->set_discovery_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)| discovery status | 
 **site_id** | **int**| The numeric identifier of the site. | 

### Return type

[**Discovery**](Discovery.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../SDK/csp-api/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../SDK/csp-api/README.md#documentation-for-models) [[Back to README]](../../SDK/csp-api/README.md)

# **set_enforcement_mode**
> set_enforcement_mode(body, site_id, if_unmodified_since=if_unmodified_since, if_match=if_match)

Change protection mode of a website

Enables you to switch between Monitor Mode and Enforce Mode.    When in Enforce Mode, all resources you set to Block are not available in your application and new resources are automatically blocked. If the API key used is for a parent account, and the website belongs to a sub account, the caid of the sub account must be specified.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WebsitesApi()
body = 'body_example' # str | enforcement mode, 'enforce' to enable enforcement, 'monitor' to switch site to monitor mode.
site_id = 789 # int | The numeric identifier of the site
if_unmodified_since = '2013-10-20T19:20:30+01:00' # datetime | Block only if no new domains were discovered since the specified date. (optional)
if_match = 'if_match_example' # str | Block only if the list of domains discovered by Client-Side Protection matches the list fetched by client from get domains call. The value for If-Match header must be taken from the value of ETag of the GET /domains call. Recommended use with 'W/' prefix for fuzzy comparison: only block when the difference between lists is reasonably insignificant.for example: 'If-Match: W/\"etagvalue\"'  (optional)

try:
    # Change protection mode of a website
    api_instance.set_enforcement_mode(body, site_id, if_unmodified_since=if_unmodified_since, if_match=if_match)
except ApiException as e:
    print("Exception when calling WebsitesApi->set_enforcement_mode: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)| enforcement mode, &#x27;enforce&#x27; to enable enforcement, &#x27;monitor&#x27; to switch site to monitor mode. | 
 **site_id** | **int**| The numeric identifier of the site | 
 **if_unmodified_since** | **datetime**| Block only if no new domains were discovered since the specified date. | [optional] 
 **if_match** | **str**| Block only if the list of domains discovered by Client-Side Protection matches the list fetched by client from get domains call. The value for If-Match header must be taken from the value of ETag of the GET /domains call. Recommended use with &#x27;W/&#x27; prefix for fuzzy comparison: only block when the difference between lists is reasonably insignificant.for example: &#x27;If-Match: W/\&quot;etagvalue\&quot;&#x27;  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../SDK/csp-api/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../SDK/csp-api/README.md#documentation-for-models) [[Back to README]](../../SDK/csp-api/README.md)

# **set_site**
> SetSite set_site(body, site_id)

Change website configuration and status details

Change Client-Side Protection configuration and status details for a specific website.  This will change the discovery status, protection mode and emails list all at once for the site. If the API key used is for a parent account, and the website belongs to a sub account, the caid of the sub account must be specified.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WebsitesApi()
body = swagger_client.SetSite() # SetSite | 
site_id = 789 # int | The numeric identifier of the site.

try:
    # Change website configuration and status details
    api_response = api_instance.set_site(body, site_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebsitesApi->set_site: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SetSite**](SetSite.md)|  | 
 **site_id** | **int**| The numeric identifier of the site. | 

### Return type

[**SetSite**](SetSite.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../../SDK/csp-api/README.md#documentation-for-api-endpoints) [[Back to Model list]](../../SDK/csp-api/README.md#documentation-for-models) [[Back to README]](../../SDK/csp-api/README.md)

