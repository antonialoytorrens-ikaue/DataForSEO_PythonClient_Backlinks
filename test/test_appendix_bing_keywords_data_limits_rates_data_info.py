# coding: utf-8

"""
    DataForSEO API documentation

    DataForSEO API is the starting point on your journey towards building powerful SEO software. With DataForSEO you can get all the data you need to build an efficient application while also saving your time and budget. DataForSEO API is using the REST technology for interchanging data between your application and our service. The data exchange is made through the widely used HTTP protocol, which allows applying our API to almost all programming languages.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dataforseo_client.models.appendix_bing_keywords_data_limits_rates_data_info import AppendixBingKeywordsDataLimitsRatesDataInfo

class TestAppendixBingKeywordsDataLimitsRatesDataInfo(unittest.TestCase):
    """AppendixBingKeywordsDataLimitsRatesDataInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AppendixBingKeywordsDataLimitsRatesDataInfo:
        """Test AppendixBingKeywordsDataLimitsRatesDataInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AppendixBingKeywordsDataLimitsRatesDataInfo`
        """
        model = AppendixBingKeywordsDataLimitsRatesDataInfo()
        if include_optional:
            return AppendixBingKeywordsDataLimitsRatesDataInfo(
                keyword_performance = dataforseo_client.models.appendix_info.AppendixInfo(
                    task_post = 1.337, 
                    task_get = 1.337, 
                    tasks_ready = 1.337, 
                    live = 1.337, ),
                search_volume_history = dataforseo_client.models.appendix_info.AppendixInfo(
                    task_post = 1.337, 
                    task_get = 1.337, 
                    tasks_ready = 1.337, 
                    live = 1.337, ),
                search_volume = dataforseo_client.models.appendix_info.AppendixInfo(
                    task_post = 1.337, 
                    task_get = 1.337, 
                    tasks_ready = 1.337, 
                    live = 1.337, ),
                keywords_for_site = dataforseo_client.models.appendix_info.AppendixInfo(
                    task_post = 1.337, 
                    task_get = 1.337, 
                    tasks_ready = 1.337, 
                    live = 1.337, ),
                keywords_for_keywords = dataforseo_client.models.appendix_info.AppendixInfo(
                    task_post = 1.337, 
                    task_get = 1.337, 
                    tasks_ready = 1.337, 
                    live = 1.337, )
            )
        else:
            return AppendixBingKeywordsDataLimitsRatesDataInfo(
        )
        """

    def testAppendixBingKeywordsDataLimitsRatesDataInfo(self):
        """Test AppendixBingKeywordsDataLimitsRatesDataInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
