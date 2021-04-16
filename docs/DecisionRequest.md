# DecisionRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**placements** | [**[Placement]**](Placement.md) | One or more Placement objects | 
**user** | [**User**](User.md) |  | [optional] 
**keywords** | **[str], none_type** | Keywords for keyword Targeting. Such as &#x60;\&quot;keywords\&quot;: [\&quot;foo\&quot;, \&quot;bar\&quot;, \&quot;baz\&quot;]&#x60;. | [optional] 
**url** | **str, none_type** | The current page URL | [optional] 
**referrer** | **str, none_type** | The referrer URL | [optional] 
**ip** | **str, none_type** | The IP address. Required for [Geo-Targeting](https://dev.adzerk.com/docs/geo-location) | [optional] 
**blocked_creatives** | **[int], none_type** | Numeric creative ids to disregard for ad selection | [optional] 
**is_mobile** | **bool, none_type** | If true, only ads containing a single image will be returned | [optional] 
**include_pricing_data** | **bool, none_type** | If true, return pricing data for the decision in the response | [optional] 
**notrack** | **bool, none_type** | If true, only return ads that are set to honor Do Not Track | [optional] 
**enable_bot_filtering** | **bool, none_type** | If making a client-side request, set to true. Defaults to false to ensure a server isn&#39;t seen as a bot. See [here](https://dev.adzerk.com/docs/tracking-overview#section-bot-filtering) for more info | [optional] 
**enable_user_dbip** | **bool, none_type** | If true, override the IP address of the request with the IP address supplied on the UserKey. If no IP address is found on the UserKey, this will fall back to the IP address on the request. Requires UserDB | [optional] 
**consent** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | Object that sets the data consent preferences. Other consent settings are available in the GDPR settings documentation. | [optional] 
**device_id** | **str, none_type** | RTB requests only - sets an Identifier for Advertisers (IFA or IDFA) | [optional] 
**parallel** | **bool, none_type** |  | [optional] 
**intended_latitude** | **float, none_type** |  | [optional] 
**intended_longitude** | **float, none_type** |  | [optional] 
**radius** | **float, none_type** |  | [optional] 
**include_matched_points** | **bool, none_type** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


