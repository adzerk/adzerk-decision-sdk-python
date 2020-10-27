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


class DecisionRequest(object):
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
        'placements': 'list[Placement]',
        'user': 'User',
        'keywords': 'list[str]',
        'url': 'str',
        'referrer': 'str',
        'ip': 'str',
        'blocked_creatives': 'list[int]',
        'is_mobile': 'bool',
        'include_pricing_data': 'bool',
        'notrack': 'bool',
        'enable_bot_filtering': 'bool',
        'enable_user_dbip': 'bool',
        'consent': 'object',
        'device_id': 'str',
        'parallel': 'bool',
        'intended_latitude': 'str',
        'intended_longitude': 'str',
        'include_matched_points': 'bool'
    }

    attribute_map = {
        'placements': 'placements',
        'user': 'user',
        'keywords': 'keywords',
        'url': 'url',
        'referrer': 'referrer',
        'ip': 'ip',
        'blocked_creatives': 'blockedCreatives',
        'is_mobile': 'isMobile',
        'include_pricing_data': 'includePricingData',
        'notrack': 'notrack',
        'enable_bot_filtering': 'enableBotFiltering',
        'enable_user_dbip': 'enableUserDBIP',
        'consent': 'consent',
        'device_id': 'deviceID',
        'parallel': 'parallel',
        'intended_latitude': 'intendedLatitude',
        'intended_longitude': 'intendedLongitude',
        'include_matched_points': 'includeMatchedPoints'
    }

    def __init__(self, placements=None, user=None, keywords=None, url=None, referrer=None, ip=None, blocked_creatives=None, is_mobile=None, include_pricing_data=None, notrack=None, enable_bot_filtering=None, enable_user_dbip=None, consent=None, device_id=None, parallel=None, intended_latitude=None, intended_longitude=None, include_matched_points=None, local_vars_configuration=None):  # noqa: E501
        """DecisionRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._placements = None
        self._user = None
        self._keywords = None
        self._url = None
        self._referrer = None
        self._ip = None
        self._blocked_creatives = None
        self._is_mobile = None
        self._include_pricing_data = None
        self._notrack = None
        self._enable_bot_filtering = None
        self._enable_user_dbip = None
        self._consent = None
        self._device_id = None
        self._parallel = None
        self._intended_latitude = None
        self._intended_longitude = None
        self._include_matched_points = None
        self.discriminator = None

        self.placements = placements
        if user is not None:
            self.user = user
        self.keywords = keywords
        self.url = url
        self.referrer = referrer
        self.ip = ip
        self.blocked_creatives = blocked_creatives
        self.is_mobile = is_mobile
        self.include_pricing_data = include_pricing_data
        self.notrack = notrack
        self.enable_bot_filtering = enable_bot_filtering
        self.enable_user_dbip = enable_user_dbip
        self.consent = consent
        self.device_id = device_id
        self.parallel = parallel
        self.intended_latitude = intended_latitude
        self.intended_longitude = intended_longitude
        self.include_matched_points = include_matched_points

    @property
    def placements(self):
        """Gets the placements of this DecisionRequest.  # noqa: E501

        One or more Placement objects  # noqa: E501

        :return: The placements of this DecisionRequest.  # noqa: E501
        :rtype: list[Placement]
        """
        return self._placements

    @placements.setter
    def placements(self, placements):
        """Sets the placements of this DecisionRequest.

        One or more Placement objects  # noqa: E501

        :param placements: The placements of this DecisionRequest.  # noqa: E501
        :type: list[Placement]
        """
        if self.local_vars_configuration.client_side_validation and placements is None:  # noqa: E501
            raise ValueError("Invalid value for `placements`, must not be `None`")  # noqa: E501

        self._placements = placements

    @property
    def user(self):
        """Gets the user of this DecisionRequest.  # noqa: E501


        :return: The user of this DecisionRequest.  # noqa: E501
        :rtype: User
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this DecisionRequest.


        :param user: The user of this DecisionRequest.  # noqa: E501
        :type: User
        """

        self._user = user

    @property
    def keywords(self):
        """Gets the keywords of this DecisionRequest.  # noqa: E501

        Keywords for keyword Targeting. Such as `\"keywords\": [\"foo\", \"bar\", \"baz\"]`.  # noqa: E501

        :return: The keywords of this DecisionRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._keywords

    @keywords.setter
    def keywords(self, keywords):
        """Sets the keywords of this DecisionRequest.

        Keywords for keyword Targeting. Such as `\"keywords\": [\"foo\", \"bar\", \"baz\"]`.  # noqa: E501

        :param keywords: The keywords of this DecisionRequest.  # noqa: E501
        :type: list[str]
        """

        self._keywords = keywords

    @property
    def url(self):
        """Gets the url of this DecisionRequest.  # noqa: E501

        The current page URL  # noqa: E501

        :return: The url of this DecisionRequest.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this DecisionRequest.

        The current page URL  # noqa: E501

        :param url: The url of this DecisionRequest.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def referrer(self):
        """Gets the referrer of this DecisionRequest.  # noqa: E501

        The referrer URL  # noqa: E501

        :return: The referrer of this DecisionRequest.  # noqa: E501
        :rtype: str
        """
        return self._referrer

    @referrer.setter
    def referrer(self, referrer):
        """Sets the referrer of this DecisionRequest.

        The referrer URL  # noqa: E501

        :param referrer: The referrer of this DecisionRequest.  # noqa: E501
        :type: str
        """

        self._referrer = referrer

    @property
    def ip(self):
        """Gets the ip of this DecisionRequest.  # noqa: E501

        The IP address. Required for [Geo-Targeting](https://dev.adzerk.com/docs/geo-location)  # noqa: E501

        :return: The ip of this DecisionRequest.  # noqa: E501
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        """Sets the ip of this DecisionRequest.

        The IP address. Required for [Geo-Targeting](https://dev.adzerk.com/docs/geo-location)  # noqa: E501

        :param ip: The ip of this DecisionRequest.  # noqa: E501
        :type: str
        """

        self._ip = ip

    @property
    def blocked_creatives(self):
        """Gets the blocked_creatives of this DecisionRequest.  # noqa: E501

        Numeric creative ids to disregard for ad selection  # noqa: E501

        :return: The blocked_creatives of this DecisionRequest.  # noqa: E501
        :rtype: list[int]
        """
        return self._blocked_creatives

    @blocked_creatives.setter
    def blocked_creatives(self, blocked_creatives):
        """Sets the blocked_creatives of this DecisionRequest.

        Numeric creative ids to disregard for ad selection  # noqa: E501

        :param blocked_creatives: The blocked_creatives of this DecisionRequest.  # noqa: E501
        :type: list[int]
        """

        self._blocked_creatives = blocked_creatives

    @property
    def is_mobile(self):
        """Gets the is_mobile of this DecisionRequest.  # noqa: E501

        If true, only ads containing a single image will be returned  # noqa: E501

        :return: The is_mobile of this DecisionRequest.  # noqa: E501
        :rtype: bool
        """
        return self._is_mobile

    @is_mobile.setter
    def is_mobile(self, is_mobile):
        """Sets the is_mobile of this DecisionRequest.

        If true, only ads containing a single image will be returned  # noqa: E501

        :param is_mobile: The is_mobile of this DecisionRequest.  # noqa: E501
        :type: bool
        """

        self._is_mobile = is_mobile

    @property
    def include_pricing_data(self):
        """Gets the include_pricing_data of this DecisionRequest.  # noqa: E501

        If true, return pricing data for the decision in the response  # noqa: E501

        :return: The include_pricing_data of this DecisionRequest.  # noqa: E501
        :rtype: bool
        """
        return self._include_pricing_data

    @include_pricing_data.setter
    def include_pricing_data(self, include_pricing_data):
        """Sets the include_pricing_data of this DecisionRequest.

        If true, return pricing data for the decision in the response  # noqa: E501

        :param include_pricing_data: The include_pricing_data of this DecisionRequest.  # noqa: E501
        :type: bool
        """

        self._include_pricing_data = include_pricing_data

    @property
    def notrack(self):
        """Gets the notrack of this DecisionRequest.  # noqa: E501

        If true, only return ads that are set to honor Do Not Track  # noqa: E501

        :return: The notrack of this DecisionRequest.  # noqa: E501
        :rtype: bool
        """
        return self._notrack

    @notrack.setter
    def notrack(self, notrack):
        """Sets the notrack of this DecisionRequest.

        If true, only return ads that are set to honor Do Not Track  # noqa: E501

        :param notrack: The notrack of this DecisionRequest.  # noqa: E501
        :type: bool
        """

        self._notrack = notrack

    @property
    def enable_bot_filtering(self):
        """Gets the enable_bot_filtering of this DecisionRequest.  # noqa: E501

        If making a client-side request, set to true. Defaults to false to ensure a server isn't seen as a bot. See [here](https://dev.adzerk.com/docs/tracking-overview#section-bot-filtering) for more info  # noqa: E501

        :return: The enable_bot_filtering of this DecisionRequest.  # noqa: E501
        :rtype: bool
        """
        return self._enable_bot_filtering

    @enable_bot_filtering.setter
    def enable_bot_filtering(self, enable_bot_filtering):
        """Sets the enable_bot_filtering of this DecisionRequest.

        If making a client-side request, set to true. Defaults to false to ensure a server isn't seen as a bot. See [here](https://dev.adzerk.com/docs/tracking-overview#section-bot-filtering) for more info  # noqa: E501

        :param enable_bot_filtering: The enable_bot_filtering of this DecisionRequest.  # noqa: E501
        :type: bool
        """

        self._enable_bot_filtering = enable_bot_filtering

    @property
    def enable_user_dbip(self):
        """Gets the enable_user_dbip of this DecisionRequest.  # noqa: E501

        If true, override the IP address of the request with the IP address supplied on the UserKey. If no IP address is found on the UserKey, this will fall back to the IP address on the request. Requires UserDB  # noqa: E501

        :return: The enable_user_dbip of this DecisionRequest.  # noqa: E501
        :rtype: bool
        """
        return self._enable_user_dbip

    @enable_user_dbip.setter
    def enable_user_dbip(self, enable_user_dbip):
        """Sets the enable_user_dbip of this DecisionRequest.

        If true, override the IP address of the request with the IP address supplied on the UserKey. If no IP address is found on the UserKey, this will fall back to the IP address on the request. Requires UserDB  # noqa: E501

        :param enable_user_dbip: The enable_user_dbip of this DecisionRequest.  # noqa: E501
        :type: bool
        """

        self._enable_user_dbip = enable_user_dbip

    @property
    def consent(self):
        """Gets the consent of this DecisionRequest.  # noqa: E501

        Object that sets the data consent preferences. Other consent settings are available in the GDPR settings documentation.  # noqa: E501

        :return: The consent of this DecisionRequest.  # noqa: E501
        :rtype: object
        """
        return self._consent

    @consent.setter
    def consent(self, consent):
        """Sets the consent of this DecisionRequest.

        Object that sets the data consent preferences. Other consent settings are available in the GDPR settings documentation.  # noqa: E501

        :param consent: The consent of this DecisionRequest.  # noqa: E501
        :type: object
        """

        self._consent = consent

    @property
    def device_id(self):
        """Gets the device_id of this DecisionRequest.  # noqa: E501

        RTB requests only - sets an Identifier for Advertisers (IFA or IDFA)  # noqa: E501

        :return: The device_id of this DecisionRequest.  # noqa: E501
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this DecisionRequest.

        RTB requests only - sets an Identifier for Advertisers (IFA or IDFA)  # noqa: E501

        :param device_id: The device_id of this DecisionRequest.  # noqa: E501
        :type: str
        """

        self._device_id = device_id

    @property
    def parallel(self):
        """Gets the parallel of this DecisionRequest.  # noqa: E501


        :return: The parallel of this DecisionRequest.  # noqa: E501
        :rtype: bool
        """
        return self._parallel

    @parallel.setter
    def parallel(self, parallel):
        """Sets the parallel of this DecisionRequest.


        :param parallel: The parallel of this DecisionRequest.  # noqa: E501
        :type: bool
        """

        self._parallel = parallel

    @property
    def intended_latitude(self):
        """Gets the intended_latitude of this DecisionRequest.  # noqa: E501


        :return: The intended_latitude of this DecisionRequest.  # noqa: E501
        :rtype: str
        """
        return self._intended_latitude

    @intended_latitude.setter
    def intended_latitude(self, intended_latitude):
        """Sets the intended_latitude of this DecisionRequest.


        :param intended_latitude: The intended_latitude of this DecisionRequest.  # noqa: E501
        :type: str
        """

        self._intended_latitude = intended_latitude

    @property
    def intended_longitude(self):
        """Gets the intended_longitude of this DecisionRequest.  # noqa: E501


        :return: The intended_longitude of this DecisionRequest.  # noqa: E501
        :rtype: str
        """
        return self._intended_longitude

    @intended_longitude.setter
    def intended_longitude(self, intended_longitude):
        """Sets the intended_longitude of this DecisionRequest.


        :param intended_longitude: The intended_longitude of this DecisionRequest.  # noqa: E501
        :type: str
        """

        self._intended_longitude = intended_longitude

    @property
    def include_matched_points(self):
        """Gets the include_matched_points of this DecisionRequest.  # noqa: E501


        :return: The include_matched_points of this DecisionRequest.  # noqa: E501
        :rtype: bool
        """
        return self._include_matched_points

    @include_matched_points.setter
    def include_matched_points(self, include_matched_points):
        """Sets the include_matched_points of this DecisionRequest.


        :param include_matched_points: The include_matched_points of this DecisionRequest.  # noqa: E501
        :type: bool
        """

        self._include_matched_points = include_matched_points

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
        if not isinstance(other, DecisionRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DecisionRequest):
            return True

        return self.to_dict() != other.to_dict()
