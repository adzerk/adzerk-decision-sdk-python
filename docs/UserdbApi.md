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


# **add_custom_properties**
> file_type add_custom_properties(network_id, user_key)



Add Custom Properties to a User

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import adzerk_decision_sdk
from adzerk_decision_sdk.api import userdb_api
from pprint import pprint
# Defining the host is optional and defaults to https://e-23.adzerk.net
# See configuration.py for a list of all supported configuration parameters.
configuration = adzerk_decision_sdk.Configuration(
    host = "https://e-23.adzerk.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with adzerk_decision_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = userdb_api.UserdbApi(api_client)
    network_id = 1 # int | Your Network Id
    user_key = "userKey_example" # str | The User's UserDB Key
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.add_custom_properties(network_id, user_key)
        pprint(api_response)
    except adzerk_decision_sdk.ApiException as e:
        print("Exception when calling UserdbApi->add_custom_properties: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.add_custom_properties(network_id, user_key, body=body)
        pprint(api_response)
    except adzerk_decision_sdk.ApiException as e:
        print("Exception when calling UserdbApi->add_custom_properties: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_id** | **int**| Your Network Id |
 **user_key** | **str**| The User&#39;s UserDB Key |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**|  | [optional]

### Return type

**file_type**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: image/gif


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_interests**
> file_type add_interests(network_id, user_key, interest)



Add Interests to a User

### Example

```python
import time
import adzerk_decision_sdk
from adzerk_decision_sdk.api import userdb_api
from pprint import pprint
# Defining the host is optional and defaults to https://e-23.adzerk.net
# See configuration.py for a list of all supported configuration parameters.
configuration = adzerk_decision_sdk.Configuration(
    host = "https://e-23.adzerk.net"
)


# Enter a context with an instance of the API client
with adzerk_decision_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = userdb_api.UserdbApi(api_client)
    network_id = 1 # int | Your Network Id
    user_key = "userKey_example" # str | The User's UserDB Key
    interest = "interest_example" # str | Comma Seperated list of interests

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.add_interests(network_id, user_key, interest)
        pprint(api_response)
    except adzerk_decision_sdk.ApiException as e:
        print("Exception when calling UserdbApi->add_interests: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_id** | **int**| Your Network Id |
 **user_key** | **str**| The User&#39;s UserDB Key |
 **interest** | **str**| Comma Seperated list of interests |

### Return type

**file_type**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/gif


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_retargeting_segment**
> file_type add_retargeting_segment(network_id, advertiser_id, retargeting_segment_id, user_key)



Add User to a Retargeting Segment

### Example

```python
import time
import adzerk_decision_sdk
from adzerk_decision_sdk.api import userdb_api
from pprint import pprint
# Defining the host is optional and defaults to https://e-23.adzerk.net
# See configuration.py for a list of all supported configuration parameters.
configuration = adzerk_decision_sdk.Configuration(
    host = "https://e-23.adzerk.net"
)


# Enter a context with an instance of the API client
with adzerk_decision_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = userdb_api.UserdbApi(api_client)
    network_id = 1 # int | Your Network Id
    advertiser_id = 1 # int | The Advertiser's ID
    retargeting_segment_id = 1 # int | The Segment's ID
    user_key = "userKey_example" # str | The User's UserDB Key

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.add_retargeting_segment(network_id, advertiser_id, retargeting_segment_id, user_key)
        pprint(api_response)
    except adzerk_decision_sdk.ApiException as e:
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

**file_type**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/gif


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
import time
import adzerk_decision_sdk
from adzerk_decision_sdk.api import userdb_api
from pprint import pprint
# Defining the host is optional and defaults to https://e-23.adzerk.net
# See configuration.py for a list of all supported configuration parameters.
configuration = adzerk_decision_sdk.Configuration(
    host = "https://e-23.adzerk.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with adzerk_decision_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = userdb_api.UserdbApi(api_client)
    network_id = 1 # int | Your Network Id
    user_key = "userKey_example" # str | The User's UserDB Key

    # example passing only required values which don't have defaults set
    try:
        api_instance.forget(network_id, user_key)
    except adzerk_decision_sdk.ApiException as e:
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
> file_type gdpr_consent(network_id)



GDPR Consent

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import adzerk_decision_sdk
from adzerk_decision_sdk.api import userdb_api
from adzerk_decision_sdk.model.consent_request import ConsentRequest
from pprint import pprint
# Defining the host is optional and defaults to https://e-23.adzerk.net
# See configuration.py for a list of all supported configuration parameters.
configuration = adzerk_decision_sdk.Configuration(
    host = "https://e-23.adzerk.net"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with adzerk_decision_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = userdb_api.UserdbApi(api_client)
    network_id = 1 # int | Your Network Id
    consent_request = ConsentRequest(
        user_key="user_key_example",
        consent={},
    ) # ConsentRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.gdpr_consent(network_id)
        pprint(api_response)
    except adzerk_decision_sdk.ApiException as e:
        print("Exception when calling UserdbApi->gdpr_consent: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.gdpr_consent(network_id, consent_request=consent_request)
        pprint(api_response)
    except adzerk_decision_sdk.ApiException as e:
        print("Exception when calling UserdbApi->gdpr_consent: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_id** | **int**| Your Network Id |
 **consent_request** | [**ConsentRequest**](ConsentRequest.md)|  | [optional]

### Return type

**file_type**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: image/gif


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ip_override**
> file_type ip_override(network_id, user_key, ip)



IP Address Override

### Example

```python
import time
import adzerk_decision_sdk
from adzerk_decision_sdk.api import userdb_api
from pprint import pprint
# Defining the host is optional and defaults to https://e-23.adzerk.net
# See configuration.py for a list of all supported configuration parameters.
configuration = adzerk_decision_sdk.Configuration(
    host = "https://e-23.adzerk.net"
)


# Enter a context with an instance of the API client
with adzerk_decision_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = userdb_api.UserdbApi(api_client)
    network_id = 1 # int | Your Network Id
    user_key = "userKey_example" # str | The User's UserDB Key
    ip = "ip_example" # str | This is the IP to exclude

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.ip_override(network_id, user_key, ip)
        pprint(api_response)
    except adzerk_decision_sdk.ApiException as e:
        print("Exception when calling UserdbApi->ip_override: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_id** | **int**| Your Network Id |
 **user_key** | **str**| The User&#39;s UserDB Key |
 **ip** | **str**| This is the IP to exclude |

### Return type

**file_type**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/gif


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated UserDB record |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **match_user**
> file_type match_user(network_id, user_key, partner_id, user_id)



User Matching

### Example

```python
import time
import adzerk_decision_sdk
from adzerk_decision_sdk.api import userdb_api
from pprint import pprint
# Defining the host is optional and defaults to https://e-23.adzerk.net
# See configuration.py for a list of all supported configuration parameters.
configuration = adzerk_decision_sdk.Configuration(
    host = "https://e-23.adzerk.net"
)


# Enter a context with an instance of the API client
with adzerk_decision_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = userdb_api.UserdbApi(api_client)
    network_id = 1 # int | Your Network Id
    user_key = "userKey_example" # str | The User's UserDB Key
    partner_id = 1 # int | The ID of the RTB provider in Adzerk. Contact Support if you don't have the ID.
    user_id = 1 # int | This is the UserID the individual RTB provider has of the user. This is NOT the UserDB userkey.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.match_user(network_id, user_key, partner_id, user_id)
        pprint(api_response)
    except adzerk_decision_sdk.ApiException as e:
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

**file_type**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/gif


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **opt_out**
> file_type opt_out(network_id, user_key)



Opt-Out a User

### Example

```python
import time
import adzerk_decision_sdk
from adzerk_decision_sdk.api import userdb_api
from pprint import pprint
# Defining the host is optional and defaults to https://e-23.adzerk.net
# See configuration.py for a list of all supported configuration parameters.
configuration = adzerk_decision_sdk.Configuration(
    host = "https://e-23.adzerk.net"
)


# Enter a context with an instance of the API client
with adzerk_decision_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = userdb_api.UserdbApi(api_client)
    network_id = 1 # int | Your Network Id
    user_key = "userKey_example" # str | The User's UserDB Key

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.opt_out(network_id, user_key)
        pprint(api_response)
    except adzerk_decision_sdk.ApiException as e:
        print("Exception when calling UserdbApi->opt_out: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_id** | **int**| Your Network Id |
 **user_key** | **str**| The User&#39;s UserDB Key |

### Return type

**file_type**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/gif


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Sucess |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} read(network_id, user_key)



Read a User's UserDB Record

### Example

```python
import time
import adzerk_decision_sdk
from adzerk_decision_sdk.api import userdb_api
from pprint import pprint
# Defining the host is optional and defaults to https://e-23.adzerk.net
# See configuration.py for a list of all supported configuration parameters.
configuration = adzerk_decision_sdk.Configuration(
    host = "https://e-23.adzerk.net"
)


# Enter a context with an instance of the API client
with adzerk_decision_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = userdb_api.UserdbApi(api_client)
    network_id = 1 # int | Your Network Id
    user_key = "userKey_example" # str | The User's UserDB Key

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.read(network_id, user_key)
        pprint(api_response)
    except adzerk_decision_sdk.ApiException as e:
        print("Exception when calling UserdbApi->read: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_id** | **int**| Your Network Id |
 **user_key** | **str**| The User&#39;s UserDB Key |

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

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

