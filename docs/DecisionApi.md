# adzerk_decision_sdk.DecisionApi

All URIs are relative to *https://e-23.adzerk.net*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_decisions**](DecisionApi.md#get_decisions) | **POST** /api/v2 | 


# **get_decisions**
> DecisionResponse get_decisions()



Request Decision(s)

### Example

```python
import time
import adzerk_decision_sdk
from adzerk_decision_sdk.api import decision_api
from adzerk_decision_sdk.model.decision_response import DecisionResponse
from adzerk_decision_sdk.model.decision_request import DecisionRequest
from pprint import pprint
# Defining the host is optional and defaults to https://e-23.adzerk.net
# See configuration.py for a list of all supported configuration parameters.
configuration = adzerk_decision_sdk.Configuration(
    host = "https://e-23.adzerk.net"
)


# Enter a context with an instance of the API client
with adzerk_decision_sdk.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = decision_api.DecisionApi(api_client)
    decision_request = DecisionRequest(
        placements=[
            Placement(
                div_name="div_name_example",
                network_id=1,
                site_id=1,
                ad_types=[
                    1,
                ],
                zone_ids=[
                    1,
                ],
                campaign_id=1,
                flight_id=1,
                ad_id=1,
                click_url="click_url_example",
                properties={},
                event_ids=[
                    1,
                ],
                overrides={},
                content_keys={
                    "key": 1,
                },
                count=1,
                proportionality=True,
                ecpm_partition="ecpm_partition_example",
                ecpm_partitions=[
                    "ecpm_partitions_example",
                ],
                event_multiplier=-100000000,
                skip_selection=True,
                ad_query={},
            ),
        ],
        user=User(
            key="key_example",
        ),
        keywords=[
            "keywords_example",
        ],
        url="url_example",
        referrer="referrer_example",
        ip="ip_example",
        blocked_creatives=[
            1,
        ],
        is_mobile=True,
        include_pricing_data=True,
        notrack=True,
        enable_bot_filtering=True,
        enable_user_dbip=True,
        consent={},
        device_id="device_id_example",
        parallel=True,
        intended_latitude=3.14,
        intended_longitude=3.14,
        radius=3.14,
        include_matched_points=True,
    ) # DecisionRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_decisions(decision_request=decision_request)
        pprint(api_response)
    except adzerk_decision_sdk.ApiException as e:
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

