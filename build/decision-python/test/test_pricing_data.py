# coding: utf-8

"""
    Adzerk Decision API

    Adzerk Decision API  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import adzerk_decision_sdk
from adzerk_decision_sdk.models.pricing_data import PricingData  # noqa: E501
from adzerk_decision_sdk.rest import ApiException

class TestPricingData(unittest.TestCase):
    """PricingData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PricingData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = adzerk_decision_sdk.models.pricing_data.PricingData()  # noqa: E501
        if include_optional :
            return PricingData(
                price = 1.337, 
                clear_price = 1.337, 
                revenue = 1.337, 
                rate_type = 56, 
                e_cpm = 1.337
            )
        else :
            return PricingData(
        )

    def testPricingData(self):
        """Test PricingData"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
