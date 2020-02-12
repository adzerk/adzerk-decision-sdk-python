# adzerk_decision_sdk.UserdbApi

All URIs are relative to *https://e-23.adzerk.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_custom_properties**](UserdbApi.md#add_custom_properties) | **POST** /udb/{networkId}/custom | 
[**add_interests**](UserdbApi.md#add_interests) | **GET** /udb/{networkId}/interest/i.gif | 
[**add_retargeting_segment**](UserdbApi.md#add_retargeting_segment) | **GET** /udb/{networkId}/rt/{advertiserId}/{retargetingSegmentId}/i.gif | 
[**forget**](UserdbApi.md#forget) | **DELETE** /udb/{networkId} | 
[**gdpr_consent**](UserdbApi.md#gdpr_consent) | **POST** /udb/{networkId}/consent | 
[**ip_override**](UserdbApi.md#ip_override) | **GET** /udb/{networkId}/ip/i.gif | 
[**match_user**](UserdbApi.md#match_user) | **GET** /udb/{networkId}/sync/i.gif | 
[**opt_out**](UserdbApi.md#opt_out) | **GET** /udb/{networkId}/optout/i.gif | 
[**read**](UserdbApi.md#read) | **GET** /udb/{networkId}/read | 
[**set_user_cookie**](UserdbApi.md#set_user_cookie) | **GET** /udb/{networkId}/set/i.gif | 


# **add_custom_properties**
> add_custom_properties(network_id, user_key, body=body)



Add Custom Properties to a User

### Example

* Api Key Authentication (ApiKeyAuth):
```python
from __future__ import print_function
import time
import adzerk_decision_sdk
from adzerk_decision_sdk.rest import ApiException
from pprint import pprint
configuration = adzerk_decision_sdk.Configuration()
# Configure API key authorization: ApiKeyAuth
configuration.api_key['X-Adzerk-ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Adzerk-ApiKey'] = 'Bearer'

# Defining host is optional and default to https://e-23.adzerk.net
configuration.host = "https://e-23.adzerk.net"
# Create an instance of the API class
api_instance = adzerk_decision_sdk.UserdbApi(adzerk_decision_sdk.ApiClient(configuration))
network_id = 56 # int | Your Network Id
user_key = 'user_key_example' # str | The User's UserDB Key
body = None # object |  (optional)

try:
    api_instance.add_custom_properties(network_id, user_key, body=body)
except ApiException as e:
    print("Exception when calling UserdbApi->add_custom_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_id** | **int**| Your Network Id | 
 **user_key** | **str**| The User&#39;s UserDB Key | 
 **body** | **object**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_interests**
> add_interests(network_id, user_key, interest)



Add Interests to a User

### Example

```python
from __future__ import print_function
import time
import adzerk_decision_sdk
from adzerk_decision_sdk.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = adzerk_decision_sdk.UserdbApi()
network_id = 56 # int | Your Network Id
user_key = 'user_key_example' # str | The User's UserDB Key
interest = 'interest_example' # str | Comma Seperated list of interests

try:
    api_instance.add_interests(network_id, user_key, interest)
except ApiException as e:
    print("Exception when calling UserdbApi->add_interests: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_id** | **int**| Your Network Id | 
 **user_key** | **str**| The User&#39;s UserDB Key | 
 **interest** | **str**| Comma Seperated list of interests | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_retargeting_segment**
> add_retargeting_segment(network_id, advertiser_id, retargeting_segment_id, user_key)



Add User to a Retargeting Segment

### Example

```python
from __future__ import print_function
import time
import adzerk_decision_sdk
from adzerk_decision_sdk.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = adzerk_decision_sdk.UserdbApi()
network_id = 56 # int | Your Network Id
advertiser_id = 56 # int | The Advertiser's ID
retargeting_segment_id = 56 # int | The Segment's ID
user_key = 'user_key_example' # str | The User's UserDB Key

try:
    api_instance.add_retargeting_segment(network_id, advertiser_id, retargeting_segment_id, user_key)
except ApiException as e:
    print("Exception when calling UserdbApi->add_retargeting_segment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_id** | **int**| Your Network Id | 
 **advertiser_id** | **int**| The Advertiser&#39;s ID | 
 **retargeting_segment_id** | **int**| The Segment&#39;s ID | 
 **user_key** | **str**| The User&#39;s UserDB Key | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forget**
> forget(network_id, user_key)



Forget User

### Example

* Api Key Authentication (ApiKeyAuth):
```python
from __future__ import print_function
import time
import adzerk_decision_sdk
from adzerk_decision_sdk.rest import ApiException
from pprint import pprint
configuration = adzerk_decision_sdk.Configuration()
# Configure API key authorization: ApiKeyAuth
configuration.api_key['X-Adzerk-ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Adzerk-ApiKey'] = 'Bearer'

# Defining host is optional and default to https://e-23.adzerk.net
configuration.host = "https://e-23.adzerk.net"
# Create an instance of the API class
api_instance = adzerk_decision_sdk.UserdbApi(adzerk_decision_sdk.ApiClient(configuration))
network_id = 56 # int | Your Network Id
user_key = 'user_key_example' # str | The User's UserDB Key

try:
    api_instance.forget(network_id, user_key)
except ApiException as e:
    print("Exception when calling UserdbApi->forget: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_id** | **int**| Your Network Id | 
 **user_key** | **str**| The User&#39;s UserDB Key | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gdpr_consent**
> gdpr_consent(network_id, gdpr_consent=gdpr_consent)



GDPR Consent

### Example

* Api Key Authentication (ApiKeyAuth):
```python
from __future__ import print_function
import time
import adzerk_decision_sdk
from adzerk_decision_sdk.rest import ApiException
from pprint import pprint
configuration = adzerk_decision_sdk.Configuration()
# Configure API key authorization: ApiKeyAuth
configuration.api_key['X-Adzerk-ApiKey'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Adzerk-ApiKey'] = 'Bearer'

# Defining host is optional and default to https://e-23.adzerk.net
configuration.host = "https://e-23.adzerk.net"
# Create an instance of the API class
api_instance = adzerk_decision_sdk.UserdbApi(adzerk_decision_sdk.ApiClient(configuration))
network_id = 56 # int | Your Network Id
gdpr_consent = adzerk_decision_sdk.GdprConsent() # GdprConsent |  (optional)

try:
    api_instance.gdpr_consent(network_id, gdpr_consent=gdpr_consent)
except ApiException as e:
    print("Exception when calling UserdbApi->gdpr_consent: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_id** | **int**| Your Network Id | 
 **gdpr_consent** | [**GdprConsent**](GdprConsent.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ip_override**
> object ip_override(network_id, user_key, ip)



IP Address Override

### Example

```python
from __future__ import print_function
import time
import adzerk_decision_sdk
from adzerk_decision_sdk.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = adzerk_decision_sdk.UserdbApi()
network_id = 56 # int | Your Network Id
user_key = 'user_key_example' # str | The User's UserDB Key
ip = 'ip_example' # str | This is the IP to exclude

try:
    api_response = api_instance.ip_override(network_id, user_key, ip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserdbApi->ip_override: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_id** | **int**| Your Network Id | 
 **user_key** | **str**| The User&#39;s UserDB Key | 
 **ip** | **str**| This is the IP to exclude | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated UserDB record |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **match_user**
> match_user(network_id, user_key, partner_id, user_id)



User Matching

### Example

```python
from __future__ import print_function
import time
import adzerk_decision_sdk
from adzerk_decision_sdk.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = adzerk_decision_sdk.UserdbApi()
network_id = 56 # int | Your Network Id
user_key = 'user_key_example' # str | The User's UserDB Key
partner_id = 56 # int | The ID of the RTB provider in Adzerk. Contact Support if you don't have the ID.
user_id = 56 # int | This is the UserID the individual RTB provider has of the user. This is NOT the UserDB userkey.

try:
    api_instance.match_user(network_id, user_key, partner_id, user_id)
except ApiException as e:
    print("Exception when calling UserdbApi->match_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_id** | **int**| Your Network Id | 
 **user_key** | **str**| The User&#39;s UserDB Key | 
 **partner_id** | **int**| The ID of the RTB provider in Adzerk. Contact Support if you don&#39;t have the ID. | 
 **user_id** | **int**| This is the UserID the individual RTB provider has of the user. This is NOT the UserDB userkey. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **opt_out**
> opt_out(network_id, user_key)



Opt-Out a User

### Example

```python
from __future__ import print_function
import time
import adzerk_decision_sdk
from adzerk_decision_sdk.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = adzerk_decision_sdk.UserdbApi()
network_id = 56 # int | Your Network Id
user_key = 'user_key_example' # str | The User's UserDB Key

try:
    api_instance.opt_out(network_id, user_key)
except ApiException as e:
    print("Exception when calling UserdbApi->opt_out: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_id** | **int**| Your Network Id | 
 **user_key** | **str**| The User&#39;s UserDB Key | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Sucess |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read**
> object read(network_id, user_key)



Read a User's UserDB Record

### Example

```python
from __future__ import print_function
import time
import adzerk_decision_sdk
from adzerk_decision_sdk.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = adzerk_decision_sdk.UserdbApi()
network_id = 56 # int | Your Network Id
user_key = 'user_key_example' # str | The User's UserDB Key

try:
    api_response = api_instance.read(network_id, user_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserdbApi->read: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_id** | **int**| Your Network Id | 
 **user_key** | **str**| The User&#39;s UserDB Key | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The UserDB record |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_user_cookie**
> set_user_cookie(network_id, user_key)



Set User Cookie

### Example

```python
from __future__ import print_function
import time
import adzerk_decision_sdk
from adzerk_decision_sdk.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = adzerk_decision_sdk.UserdbApi()
network_id = 56 # int | Your Network Id
user_key = 'user_key_example' # str | UserDB Id for the user

try:
    api_instance.set_user_cookie(network_id, user_key)
except ApiException as e:
    print("Exception when calling UserdbApi->set_user_cookie: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_id** | **int**| Your Network Id | 
 **user_key** | **str**| UserDB Id for the user | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

