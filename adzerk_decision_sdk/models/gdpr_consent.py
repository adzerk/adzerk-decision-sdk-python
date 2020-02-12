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


class GdprConsent(object):
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
        'user_key': 'str',
        'consent': 'Consent'
    }

    attribute_map = {
        'user_key': 'userKey',
        'consent': 'consent'
    }

    def __init__(self, user_key=None, consent=None, local_vars_configuration=None):  # noqa: E501
        """GdprConsent - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._user_key = None
        self._consent = None
        self.discriminator = None

        if user_key is not None:
            self.user_key = user_key
        if consent is not None:
            self.consent = consent

    @property
    def user_key(self):
        """Gets the user_key of this GdprConsent.  # noqa: E501


        :return: The user_key of this GdprConsent.  # noqa: E501
        :rtype: str
        """
        return self._user_key

    @user_key.setter
    def user_key(self, user_key):
        """Sets the user_key of this GdprConsent.


        :param user_key: The user_key of this GdprConsent.  # noqa: E501
        :type: str
        """

        self._user_key = user_key

    @property
    def consent(self):
        """Gets the consent of this GdprConsent.  # noqa: E501


        :return: The consent of this GdprConsent.  # noqa: E501
        :rtype: Consent
        """
        return self._consent

    @consent.setter
    def consent(self, consent):
        """Sets the consent of this GdprConsent.


        :param consent: The consent of this GdprConsent.  # noqa: E501
        :type: Consent
        """

        self._consent = consent

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
        if not isinstance(other, GdprConsent):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GdprConsent):
            return True

        return self.to_dict() != other.to_dict()
