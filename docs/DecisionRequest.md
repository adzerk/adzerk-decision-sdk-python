# DecisionRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**placements** | [**list[Placement]**](Placement.md) | One or more Placement objects | 
**user** | [**User**](User.md) |  | [optional] 
**keywords** | **list[str]** | Keywords for keyword Targeting. Such as &#x60;\&quot;keywords\&quot;: [\&quot;foo\&quot;, \&quot;bar\&quot;, \&quot;baz\&quot;]&#x60;. | [optional] 
**url** | **str** | The current page URL | [optional] 
**referrer** | **str** | The referrer URL | [optional] 
**ip** | **str** | The IP address. Required for [Geo-Targeting](https://dev.adzerk.com/docs/geo-location) | [optional] 
**blocked_creatives** | **list[int]** | Numeric creative ids to disregard for ad selection | [optional] 
**is_mobile** | **bool** | If true, only ads containing a single image will be returned | [optional] 
**include_pricing_data** | **bool** | If true, return pricing data for the decision in the response | [optional] 
**notrack** | **bool** | If true, only return ads that are set to honor Do Not Track | [optional] 
**enable_bot_filtering** | **bool** | If making a client-side request, set to true. Defaults to false to ensure a server isn&#39;t seen as a bot. See [here](https://dev.adzerk.com/docs/tracking-overview#section-bot-filtering) for more info | [optional] 
**enable_user_dbip** | **bool** | If true, override the IP address of the request with the IP address supplied on the UserKey. If no IP address is found on the UserKey, this will fall back to the IP address on the request. Requires UserDB | [optional] 
**consent** | [**object**](.md) | Object that sets the data consent preferences. Other consent settings are available in the GDPR settings documentation. | [optional] 
**device_id** | **str** | RTB requests only - sets an Identifier for Advertisers (IFA or IDFA) | [optional] 
**parallel** | **bool** |  | [optional] 
**intended_latitude** | **float** |  | [optional] 
**intended_longitude** | **float** |  | [optional] 
**radius** | **float** |  | [optional] 
**include_matched_points** | **bool** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


