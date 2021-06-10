"""
    Adzerk Decision API

    Adzerk Decision API  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from adzerk_decision_sdk.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)


class Placement(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
        ('event_multiplier',): {
            'inclusive_maximum': 100000000,
            'inclusive_minimum': -100000000,
        },
    }

    additional_properties_type = None

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        return {
            'div_name': (str,),  # noqa: E501
            'network_id': (int,),  # noqa: E501
            'site_id': (int,),  # noqa: E501
            'ad_types': ([int],),  # noqa: E501
            'zone_ids': ([int], none_type,),  # noqa: E501
            'campaign_id': (int, none_type,),  # noqa: E501
            'flight_id': (int, none_type,),  # noqa: E501
            'ad_id': (int, none_type,),  # noqa: E501
            'click_url': (str, none_type,),  # noqa: E501
            'properties': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type,),  # noqa: E501
            'event_ids': ([int], none_type,),  # noqa: E501
            'overrides': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type,),  # noqa: E501
            'content_keys': ({str: (int,)}, none_type,),  # noqa: E501
            'count': (int, none_type,),  # noqa: E501
            'proportionality': (bool, none_type,),  # noqa: E501
            'ecpm_partition': (str, none_type,),  # noqa: E501
            'ecpm_partitions': ([str], none_type,),  # noqa: E501
            'event_multiplier': (int, none_type,),  # noqa: E501
            'skip_selection': (bool, none_type,),  # noqa: E501
            'ad_query': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type,),  # noqa: E501
            'floor_price': (float, none_type,),  # noqa: E501
            'floor_cpc': (float, none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'div_name': 'divName',  # noqa: E501
        'network_id': 'networkId',  # noqa: E501
        'site_id': 'siteId',  # noqa: E501
        'ad_types': 'adTypes',  # noqa: E501
        'zone_ids': 'zoneIds',  # noqa: E501
        'campaign_id': 'campaignId',  # noqa: E501
        'flight_id': 'flightId',  # noqa: E501
        'ad_id': 'adId',  # noqa: E501
        'click_url': 'clickUrl',  # noqa: E501
        'properties': 'properties',  # noqa: E501
        'event_ids': 'eventIds',  # noqa: E501
        'overrides': 'overrides',  # noqa: E501
        'content_keys': 'contentKeys',  # noqa: E501
        'count': 'count',  # noqa: E501
        'proportionality': 'proportionality',  # noqa: E501
        'ecpm_partition': 'ecpmPartition',  # noqa: E501
        'ecpm_partitions': 'ecpmPartitions',  # noqa: E501
        'event_multiplier': 'eventMultiplier',  # noqa: E501
        'skip_selection': 'skipSelection',  # noqa: E501
        'ad_query': 'adQuery',  # noqa: E501
        'floor_price': 'floorPrice',  # noqa: E501
        'floor_cpc': 'floorCpc',  # noqa: E501
    }

    _composed_schemas = {}

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """Placement - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            div_name (str): A unique name for the placement defined by you. [optional]  # noqa: E501
            network_id (int): The numeric network id. [optional]  # noqa: E501
            site_id (int): The numeric site id. [optional]  # noqa: E501
            ad_types ([int]): One or more integer ad types. More info [here](https://dev.adzerk.com/docs/ad-sizes). [optional]  # noqa: E501
            zone_ids ([int], none_type): Zone IDs to use. [optional]  # noqa: E501
            campaign_id (int, none_type): A numeric campaign id; if specified, only consider ads in that campaign. [optional]  # noqa: E501
            flight_id (int, none_type): A numeric ad (flight-creative map) id; if specified, only serve that ad if possible. [optional]  # noqa: E501
            ad_id (int, none_type): A numeric ad (flight-creative map) id; if specified, only serve that ad if possible. [optional]  # noqa: E501
            click_url (str, none_type): The ad's click-through URL. [optional]  # noqa: E501
            properties ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type): A map of key/value pairs used for [Custom Targeting](https://dev.adzerk.com/docs/custom-targeting). [optional]  # noqa: E501
            event_ids ([int], none_type): An array of numeric event types. Requests tracking URLs for custom events. See here for [Event Tracking IDs](https://dev.adzerk.com/v1.0/docs/custom-event-tracking). [optional]  # noqa: E501
            overrides ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type): An object that overrides values for an advertiser, campaign, flight or ad. Used especially for header bidding. [optional]  # noqa: E501
            content_keys ({str: (int,)}, none_type): A map of key/value pairs used with [ContentDB](https://dev.adzerk.com/docs/contentdb-1). The format is `\"contentKeys\": {\"schema\": \"contentKey\"}`. [optional]  # noqa: E501
            count (int, none_type): (BETA) The number of ads to return per placement. Integer between 1 and 20. [optional]  # noqa: E501
            proportionality (bool, none_type): (BETA) If true, fills ads in a multi-winner placement in proportion to the flight's goals. [optional]  # noqa: E501
            ecpm_partition (str, none_type): (BETA) The name of the eCPM Partition that should be used to source eCPM data for auctions. [optional]  # noqa: E501
            ecpm_partitions ([str], none_type): (BETA) The names of the eCPM Partitions that should be used to source eCPM data for auctions. [optional]  # noqa: E501
            event_multiplier (int, none_type): [optional]  # noqa: E501
            skip_selection (bool, none_type): [optional]  # noqa: E501
            ad_query ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type): [optional]  # noqa: E501
            floor_price (float, none_type): [optional]  # noqa: E501
            floor_cpc (float, none_type): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
