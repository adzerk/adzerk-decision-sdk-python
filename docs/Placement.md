# Placement


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**div_name** | **str** | A unique name for the placement defined by you | [optional] 
**network_id** | **int** | The numeric network id | [optional] 
**site_id** | **int** | The numeric site id | [optional] 
**ad_types** | **[int]** | One or more integer ad types. More info [here](https://dev.adzerk.com/docs/ad-sizes) | [optional] 
**zone_ids** | **[int], none_type** | Zone IDs to use | [optional] 
**campaign_id** | **int, none_type** | A numeric campaign id; if specified, only consider ads in that campaign | [optional] 
**flight_id** | **int, none_type** | A numeric ad (flight-creative map) id; if specified, only serve that ad if possible | [optional] 
**ad_id** | **int, none_type** | A numeric ad (flight-creative map) id; if specified, only serve that ad if possible | [optional] 
**click_url** | **str, none_type** | The ad&#39;s click-through URL | [optional] 
**properties** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | A map of key/value pairs used for [Custom Targeting](https://dev.adzerk.com/docs/custom-targeting) | [optional] 
**event_ids** | **[int], none_type** | An array of numeric event types. Requests tracking URLs for custom events. See here for [Event Tracking IDs](https://dev.adzerk.com/v1.0/docs/custom-event-tracking) | [optional] 
**overrides** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** | An object that overrides values for an advertiser, campaign, flight or ad. Used especially for header bidding | [optional] 
**content_keys** | **{str: (int,)}, none_type** | A map of key/value pairs used with [ContentDB](https://dev.adzerk.com/docs/contentdb-1). The format is &#x60;\&quot;contentKeys\&quot;: {\&quot;schema\&quot;: \&quot;contentKey\&quot;}&#x60; | [optional] 
**count** | **int, none_type** | (BETA) The number of ads to return per placement. Integer between 1 and 20 | [optional] 
**proportionality** | **bool, none_type** | (BETA) If true, fills ads in a multi-winner placement in proportion to the flight&#39;s goals | [optional] 
**ecpm_partition** | **str, none_type** | (BETA) The name of the eCPM Partition that should be used to source eCPM data for auctions | [optional] 
**ecpm_partitions** | **[str], none_type** | (BETA) The names of the eCPM Partitions that should be used to source eCPM data for auctions | [optional] 
**event_multiplier** | **int, none_type** |  | [optional] 
**skip_selection** | **bool, none_type** |  | [optional] 
**ad_query** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


