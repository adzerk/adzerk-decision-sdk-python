# coding: utf-8

"""
    Adzerk Decision API

    Adzerk Decision API  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from adzerk_decision_sdk.configuration import Configuration


class Placement(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'div_name': 'str',
        'network_id': 'int',
        'site_id': 'int',
        'ad_types': 'list[int]',
        'zone_ids': 'list[int]',
        'campaign_id': 'int',
        'flight_id': 'int',
        'ad_id': 'int',
        'click_url': 'str',
        'properties': 'object',
        'event_ids': 'list[int]',
        'overrides': 'object',
        'content_keys': 'dict(str, int)',
        'count': 'int',
        'proportionality': 'bool',
        'ecpm_partition': 'str',
        'ecpm_partitions': 'list[str]',
        'event_multiplier': 'int',
        'skip_selection': 'bool',
        'ad_query': 'object',
        'floor_price': 'float',
        'floor_cpc': 'float'
    }

    attribute_map = {
        'div_name': 'divName',
        'network_id': 'networkId',
        'site_id': 'siteId',
        'ad_types': 'adTypes',
        'zone_ids': 'zoneIds',
        'campaign_id': 'campaignId',
        'flight_id': 'flightId',
        'ad_id': 'adId',
        'click_url': 'clickUrl',
        'properties': 'properties',
        'event_ids': 'eventIds',
        'overrides': 'overrides',
        'content_keys': 'contentKeys',
        'count': 'count',
        'proportionality': 'proportionality',
        'ecpm_partition': 'ecpmPartition',
        'ecpm_partitions': 'ecpmPartitions',
        'event_multiplier': 'eventMultiplier',
        'skip_selection': 'skipSelection',
        'ad_query': 'adQuery',
        'floor_price': 'floorPrice',
        'floor_cpc': 'floorCpc'
    }

    def __init__(self, div_name=None, network_id=None, site_id=None, ad_types=None, zone_ids=None, campaign_id=None, flight_id=None, ad_id=None, click_url=None, properties=None, event_ids=None, overrides=None, content_keys=None, count=None, proportionality=None, ecpm_partition=None, ecpm_partitions=None, event_multiplier=None, skip_selection=None, ad_query=None, floor_price=None, floor_cpc=None, local_vars_configuration=None):  # noqa: E501
        """Placement - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._div_name = None
        self._network_id = None
        self._site_id = None
        self._ad_types = None
        self._zone_ids = None
        self._campaign_id = None
        self._flight_id = None
        self._ad_id = None
        self._click_url = None
        self._properties = None
        self._event_ids = None
        self._overrides = None
        self._content_keys = None
        self._count = None
        self._proportionality = None
        self._ecpm_partition = None
        self._ecpm_partitions = None
        self._event_multiplier = None
        self._skip_selection = None
        self._ad_query = None
        self._floor_price = None
        self._floor_cpc = None
        self.discriminator = None

        if div_name is not None:
            self.div_name = div_name
        if network_id is not None:
            self.network_id = network_id
        if site_id is not None:
            self.site_id = site_id
        if ad_types is not None:
            self.ad_types = ad_types
        self.zone_ids = zone_ids
        self.campaign_id = campaign_id
        self.flight_id = flight_id
        self.ad_id = ad_id
        self.click_url = click_url
        self.properties = properties
        self.event_ids = event_ids
        self.overrides = overrides
        self.content_keys = content_keys
        self.count = count
        self.proportionality = proportionality
        self.ecpm_partition = ecpm_partition
        self.ecpm_partitions = ecpm_partitions
        self.event_multiplier = event_multiplier
        self.skip_selection = skip_selection
        self.ad_query = ad_query
        self.floor_price = floor_price
        self.floor_cpc = floor_cpc

    @property
    def div_name(self):
        """Gets the div_name of this Placement.  # noqa: E501

        A unique name for the placement defined by you  # noqa: E501

        :return: The div_name of this Placement.  # noqa: E501
        :rtype: str
        """
        return self._div_name

    @div_name.setter
    def div_name(self, div_name):
        """Sets the div_name of this Placement.

        A unique name for the placement defined by you  # noqa: E501

        :param div_name: The div_name of this Placement.  # noqa: E501
        :type: str
        """

        self._div_name = div_name

    @property
    def network_id(self):
        """Gets the network_id of this Placement.  # noqa: E501

        The numeric network id  # noqa: E501

        :return: The network_id of this Placement.  # noqa: E501
        :rtype: int
        """
        return self._network_id

    @network_id.setter
    def network_id(self, network_id):
        """Sets the network_id of this Placement.

        The numeric network id  # noqa: E501

        :param network_id: The network_id of this Placement.  # noqa: E501
        :type: int
        """

        self._network_id = network_id

    @property
    def site_id(self):
        """Gets the site_id of this Placement.  # noqa: E501

        The numeric site id  # noqa: E501

        :return: The site_id of this Placement.  # noqa: E501
        :rtype: int
        """
        return self._site_id

    @site_id.setter
    def site_id(self, site_id):
        """Sets the site_id of this Placement.

        The numeric site id  # noqa: E501

        :param site_id: The site_id of this Placement.  # noqa: E501
        :type: int
        """

        self._site_id = site_id

    @property
    def ad_types(self):
        """Gets the ad_types of this Placement.  # noqa: E501

        One or more integer ad types. More info [here](https://dev.adzerk.com/docs/ad-sizes)  # noqa: E501

        :return: The ad_types of this Placement.  # noqa: E501
        :rtype: list[int]
        """
        return self._ad_types

    @ad_types.setter
    def ad_types(self, ad_types):
        """Sets the ad_types of this Placement.

        One or more integer ad types. More info [here](https://dev.adzerk.com/docs/ad-sizes)  # noqa: E501

        :param ad_types: The ad_types of this Placement.  # noqa: E501
        :type: list[int]
        """

        self._ad_types = ad_types

    @property
    def zone_ids(self):
        """Gets the zone_ids of this Placement.  # noqa: E501

        Zone IDs to use  # noqa: E501

        :return: The zone_ids of this Placement.  # noqa: E501
        :rtype: list[int]
        """
        return self._zone_ids

    @zone_ids.setter
    def zone_ids(self, zone_ids):
        """Sets the zone_ids of this Placement.

        Zone IDs to use  # noqa: E501

        :param zone_ids: The zone_ids of this Placement.  # noqa: E501
        :type: list[int]
        """

        self._zone_ids = zone_ids

    @property
    def campaign_id(self):
        """Gets the campaign_id of this Placement.  # noqa: E501

        A numeric campaign id; if specified, only consider ads in that campaign  # noqa: E501

        :return: The campaign_id of this Placement.  # noqa: E501
        :rtype: int
        """
        return self._campaign_id

    @campaign_id.setter
    def campaign_id(self, campaign_id):
        """Sets the campaign_id of this Placement.

        A numeric campaign id; if specified, only consider ads in that campaign  # noqa: E501

        :param campaign_id: The campaign_id of this Placement.  # noqa: E501
        :type: int
        """

        self._campaign_id = campaign_id

    @property
    def flight_id(self):
        """Gets the flight_id of this Placement.  # noqa: E501

        A numeric ad (flight-creative map) id; if specified, only serve that ad if possible  # noqa: E501

        :return: The flight_id of this Placement.  # noqa: E501
        :rtype: int
        """
        return self._flight_id

    @flight_id.setter
    def flight_id(self, flight_id):
        """Sets the flight_id of this Placement.

        A numeric ad (flight-creative map) id; if specified, only serve that ad if possible  # noqa: E501

        :param flight_id: The flight_id of this Placement.  # noqa: E501
        :type: int
        """

        self._flight_id = flight_id

    @property
    def ad_id(self):
        """Gets the ad_id of this Placement.  # noqa: E501

        A numeric ad (flight-creative map) id; if specified, only serve that ad if possible  # noqa: E501

        :return: The ad_id of this Placement.  # noqa: E501
        :rtype: int
        """
        return self._ad_id

    @ad_id.setter
    def ad_id(self, ad_id):
        """Sets the ad_id of this Placement.

        A numeric ad (flight-creative map) id; if specified, only serve that ad if possible  # noqa: E501

        :param ad_id: The ad_id of this Placement.  # noqa: E501
        :type: int
        """

        self._ad_id = ad_id

    @property
    def click_url(self):
        """Gets the click_url of this Placement.  # noqa: E501

        The ad's click-through URL  # noqa: E501

        :return: The click_url of this Placement.  # noqa: E501
        :rtype: str
        """
        return self._click_url

    @click_url.setter
    def click_url(self, click_url):
        """Sets the click_url of this Placement.

        The ad's click-through URL  # noqa: E501

        :param click_url: The click_url of this Placement.  # noqa: E501
        :type: str
        """

        self._click_url = click_url

    @property
    def properties(self):
        """Gets the properties of this Placement.  # noqa: E501

        A map of key/value pairs used for [Custom Targeting](https://dev.adzerk.com/docs/custom-targeting)  # noqa: E501

        :return: The properties of this Placement.  # noqa: E501
        :rtype: object
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this Placement.

        A map of key/value pairs used for [Custom Targeting](https://dev.adzerk.com/docs/custom-targeting)  # noqa: E501

        :param properties: The properties of this Placement.  # noqa: E501
        :type: object
        """

        self._properties = properties

    @property
    def event_ids(self):
        """Gets the event_ids of this Placement.  # noqa: E501

        An array of numeric event types. Requests tracking URLs for custom events. See here for [Event Tracking IDs](https://dev.adzerk.com/v1.0/docs/custom-event-tracking)  # noqa: E501

        :return: The event_ids of this Placement.  # noqa: E501
        :rtype: list[int]
        """
        return self._event_ids

    @event_ids.setter
    def event_ids(self, event_ids):
        """Sets the event_ids of this Placement.

        An array of numeric event types. Requests tracking URLs for custom events. See here for [Event Tracking IDs](https://dev.adzerk.com/v1.0/docs/custom-event-tracking)  # noqa: E501

        :param event_ids: The event_ids of this Placement.  # noqa: E501
        :type: list[int]
        """

        self._event_ids = event_ids

    @property
    def overrides(self):
        """Gets the overrides of this Placement.  # noqa: E501

        An object that overrides values for an advertiser, campaign, flight or ad. Used especially for header bidding  # noqa: E501

        :return: The overrides of this Placement.  # noqa: E501
        :rtype: object
        """
        return self._overrides

    @overrides.setter
    def overrides(self, overrides):
        """Sets the overrides of this Placement.

        An object that overrides values for an advertiser, campaign, flight or ad. Used especially for header bidding  # noqa: E501

        :param overrides: The overrides of this Placement.  # noqa: E501
        :type: object
        """

        self._overrides = overrides

    @property
    def content_keys(self):
        """Gets the content_keys of this Placement.  # noqa: E501

        A map of key/value pairs used with [ContentDB](https://dev.adzerk.com/docs/contentdb-1). The format is `\"contentKeys\": {\"schema\": \"contentKey\"}`  # noqa: E501

        :return: The content_keys of this Placement.  # noqa: E501
        :rtype: dict(str, int)
        """
        return self._content_keys

    @content_keys.setter
    def content_keys(self, content_keys):
        """Sets the content_keys of this Placement.

        A map of key/value pairs used with [ContentDB](https://dev.adzerk.com/docs/contentdb-1). The format is `\"contentKeys\": {\"schema\": \"contentKey\"}`  # noqa: E501

        :param content_keys: The content_keys of this Placement.  # noqa: E501
        :type: dict(str, int)
        """

        self._content_keys = content_keys

    @property
    def count(self):
        """Gets the count of this Placement.  # noqa: E501

        (BETA) The number of ads to return per placement. Integer between 1 and 20  # noqa: E501

        :return: The count of this Placement.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this Placement.

        (BETA) The number of ads to return per placement. Integer between 1 and 20  # noqa: E501

        :param count: The count of this Placement.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def proportionality(self):
        """Gets the proportionality of this Placement.  # noqa: E501

        (BETA) If true, fills ads in a multi-winner placement in proportion to the flight's goals  # noqa: E501

        :return: The proportionality of this Placement.  # noqa: E501
        :rtype: bool
        """
        return self._proportionality

    @proportionality.setter
    def proportionality(self, proportionality):
        """Sets the proportionality of this Placement.

        (BETA) If true, fills ads in a multi-winner placement in proportion to the flight's goals  # noqa: E501

        :param proportionality: The proportionality of this Placement.  # noqa: E501
        :type: bool
        """

        self._proportionality = proportionality

    @property
    def ecpm_partition(self):
        """Gets the ecpm_partition of this Placement.  # noqa: E501

        (BETA) The name of the eCPM Partition that should be used to source eCPM data for auctions  # noqa: E501

        :return: The ecpm_partition of this Placement.  # noqa: E501
        :rtype: str
        """
        return self._ecpm_partition

    @ecpm_partition.setter
    def ecpm_partition(self, ecpm_partition):
        """Sets the ecpm_partition of this Placement.

        (BETA) The name of the eCPM Partition that should be used to source eCPM data for auctions  # noqa: E501

        :param ecpm_partition: The ecpm_partition of this Placement.  # noqa: E501
        :type: str
        """

        self._ecpm_partition = ecpm_partition

    @property
    def ecpm_partitions(self):
        """Gets the ecpm_partitions of this Placement.  # noqa: E501

        (BETA) The names of the eCPM Partitions that should be used to source eCPM data for auctions  # noqa: E501

        :return: The ecpm_partitions of this Placement.  # noqa: E501
        :rtype: list[str]
        """
        return self._ecpm_partitions

    @ecpm_partitions.setter
    def ecpm_partitions(self, ecpm_partitions):
        """Sets the ecpm_partitions of this Placement.

        (BETA) The names of the eCPM Partitions that should be used to source eCPM data for auctions  # noqa: E501

        :param ecpm_partitions: The ecpm_partitions of this Placement.  # noqa: E501
        :type: list[str]
        """

        self._ecpm_partitions = ecpm_partitions

    @property
    def event_multiplier(self):
        """Gets the event_multiplier of this Placement.  # noqa: E501


        :return: The event_multiplier of this Placement.  # noqa: E501
        :rtype: int
        """
        return self._event_multiplier

    @event_multiplier.setter
    def event_multiplier(self, event_multiplier):
        """Sets the event_multiplier of this Placement.


        :param event_multiplier: The event_multiplier of this Placement.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                event_multiplier is not None and event_multiplier > 100000000):  # noqa: E501
            raise ValueError("Invalid value for `event_multiplier`, must be a value less than or equal to `100000000`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                event_multiplier is not None and event_multiplier < -100000000):  # noqa: E501
            raise ValueError("Invalid value for `event_multiplier`, must be a value greater than or equal to `-100000000`")  # noqa: E501

        self._event_multiplier = event_multiplier

    @property
    def skip_selection(self):
        """Gets the skip_selection of this Placement.  # noqa: E501


        :return: The skip_selection of this Placement.  # noqa: E501
        :rtype: bool
        """
        return self._skip_selection

    @skip_selection.setter
    def skip_selection(self, skip_selection):
        """Sets the skip_selection of this Placement.


        :param skip_selection: The skip_selection of this Placement.  # noqa: E501
        :type: bool
        """

        self._skip_selection = skip_selection

    @property
    def ad_query(self):
        """Gets the ad_query of this Placement.  # noqa: E501


        :return: The ad_query of this Placement.  # noqa: E501
        :rtype: object
        """
        return self._ad_query

    @ad_query.setter
    def ad_query(self, ad_query):
        """Sets the ad_query of this Placement.


        :param ad_query: The ad_query of this Placement.  # noqa: E501
        :type: object
        """

        self._ad_query = ad_query

    @property
    def floor_price(self):
        """Gets the floor_price of this Placement.  # noqa: E501


        :return: The floor_price of this Placement.  # noqa: E501
        :rtype: float
        """
        return self._floor_price

    @floor_price.setter
    def floor_price(self, floor_price):
        """Sets the floor_price of this Placement.


        :param floor_price: The floor_price of this Placement.  # noqa: E501
        :type: float
        """

        self._floor_price = floor_price

    @property
    def floor_cpc(self):
        """Gets the floor_cpc of this Placement.  # noqa: E501


        :return: The floor_cpc of this Placement.  # noqa: E501
        :rtype: float
        """
        return self._floor_cpc

    @floor_cpc.setter
    def floor_cpc(self, floor_cpc):
        """Sets the floor_cpc of this Placement.


        :param floor_cpc: The floor_cpc of this Placement.  # noqa: E501
        :type: float
        """

        self._floor_cpc = floor_cpc

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Placement):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Placement):
            return True

        return self.to_dict() != other.to_dict()
