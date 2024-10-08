# coding: utf-8

"""
    DataForSEO API documentation

    DataForSEO API is the starting point on your journey towards building powerful SEO software. With DataForSEO you can get all the data you need to build an efficient application while also saving your time and budget. DataForSEO API is using the REST technology for interchanging data between your application and our service. The data exchange is made through the widely used HTTP protocol, which allows applying our API to almost all programming languages.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dataforseo_client.models.app_ranked_serp_element_info import AppRankedSerpElementInfo

class TestAppRankedSerpElementInfo(unittest.TestCase):
    """AppRankedSerpElementInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AppRankedSerpElementInfo:
        """Test AppRankedSerpElementInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AppRankedSerpElementInfo`
        """
        model = AppRankedSerpElementInfo()
        if include_optional:
            return AppRankedSerpElementInfo(
                se_type = '',
                serp_item = dataforseo_client.models.data_app_google_play_search_organic_serp_element_item.DataAppGooglePlaySearchOrganicSerpElementItem(),
                check_url = '',
                se_results_count = '',
                last_updated_time = '',
                previous_updated_time = ''
            )
        else:
            return AppRankedSerpElementInfo(
        )
        """

    def testAppRankedSerpElementInfo(self):
        """Test AppRankedSerpElementInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
