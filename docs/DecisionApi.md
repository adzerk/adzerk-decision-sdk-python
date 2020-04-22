# adzerk_decision_sdk.DecisionApi

All URIs are relative to *https://e-23.adzerk.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_decisions**](DecisionApi.md#get_decisions) | **POST** /api/v2 | 


# **get_decisions**
> DecisionResponse get_decisions(decision_request=decision_request)



Request Decision(s)

### Example

```python
from __future__ import print_function
import time
import adzerk_decision_sdk
from adzerk_decision_sdk.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with adzerk_decision_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = adzerk_decision_sdk.DecisionApi(api_client)
    decision_request = {"placements": [{ "divName": "header", "networkId": 23, "siteId": 667480, "adTypes": [5] }] } # DecisionRequest |  (optional)

    try:
        api_response = api_instance.get_decisions(decision_request=decision_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DecisionApi->get_decisions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **decision_request** | [**DecisionRequest**](DecisionRequest.md)|  | [optional] 

### Return type

[**DecisionResponse**](DecisionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request |  -  |
**200** | Successful decision request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

