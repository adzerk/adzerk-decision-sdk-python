# Placement

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**div_name** | **str** | A unique name for the placement defined by you | [optional] 
**network_id** | **int** | The numeric network id | [optional] 
**site_id** | **int** | The numeric site id | [optional] 
**ad_types** | **list[int]** | One or more integer ad types. More info [here](https://dev.adzerk.com/docs/ad-sizes) | [optional] 
**zone_ids** | **list[int]** | Zone IDs to use | [optional] 
**campaign_id** | **int** | A numeric campaign id; if specified, only consider ads in that campaign | [optional] 
**flight_id** | **int** | A numeric ad (flight-creative map) id; if specified, only serve that ad if possible | [optional] 
**ad_id** | **int** | A numeric ad (flight-creative map) id; if specified, only serve that ad if possible | [optional] 
**click_url** | **str** | The ad&#39;s click-through URL | [optional] 
**properties** | [**object**](.md) | A map of key/value pairs used for [Custom Targeting](https://dev.adzerk.com/docs/custom-targeting) | [optional] 
**event_ids** | **list[int]** | An array of numeric event types. Requests tracking URLs for custom events. See here for [Event Tracking IDs](https://dev.adzerk.com/v1.0/docs/custom-event-tracking) | [optional] 
**overrides** | [**object**](.md) | An object that overrides values for an advertiser, campaign, flight or ad. Used especially for header bidding | [optional] 
**content_keys** | **dict(str, str)** | A map of key/value pairs used with [ContentDB](https://dev.adzerk.com/docs/contentdb-1). The format is &#x60;\&quot;contentKeys\&quot;: {\&quot;schema\&quot;: \&quot;contentKey\&quot;}&#x60; | [optional] 
**count** | **int** | (BETA) The number of ads to return per placement. Integer between 1 and 20 | [optional] 
**proportionality** | **bool** | (BETA) If true, fills ads in a multi-winner placement in proportion to the flight&#39;s goals | [optional] 
**ecpm_partition** | **str** | (BETA) The name of the eCPM Partition that should be used to source eCPM data for auctions | [optional] 
**ecpm_partitions** | **list[str]** | (BETA) The names of the eCPM Partitions that should be used to source eCPM data for auctions | [optional] 
**event_multiplier** | **int** |  | [optional] 
**skip_selection** | **bool** |  | [optional] 
**ad_query** | [**object**](.md) |  | [optional] 
**floor_price** | **float** |  | [optional] 
**floor_cpc** | **float** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


