# adzerk_decision_sdk.DecisionApi

All URIs are relative to *https://e-23.adzerk.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_decisions**](DecisionApi.md#get_decisions) | **POST** /api/v2 | 


# **get_decisions**
> Response get_decisions(body=body)



Request Decision(s)

### Example

```python
from __future__ import print_function
import time
import adzerk_decision_sdk
from adzerk_decision_sdk.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = adzerk_decision_sdk.DecisionApi()
body = {"placements": [{ "divName": "header", "networkId": 23, "siteId": 667480, "adTypes": [5] }] } # object |  (optional)

try:
    api_response = api_instance.get_decisions(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DecisionApi->get_decisions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **object**|  | [optional] 

### Return type

[**Response**](Response.md)

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

