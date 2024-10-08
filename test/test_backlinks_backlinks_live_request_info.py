# coding: utf-8

"""
    DataForSEO API documentation

    DataForSEO API is the starting point on your journey towards building powerful SEO software. With DataForSEO you can get all the data you need to build an efficient application while also saving your time and budget. DataForSEO API is using the REST technology for interchanging data between your application and our service. The data exchange is made through the widely used HTTP protocol, which allows applying our API to almost all programming languages.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dataforseo_client.models.backlinks_backlinks_live_request_info import BacklinksBacklinksLiveRequestInfo

class TestBacklinksBacklinksLiveRequestInfo(unittest.TestCase):
    """BacklinksBacklinksLiveRequestInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> BacklinksBacklinksLiveRequestInfo:
        """Test BacklinksBacklinksLiveRequestInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BacklinksBacklinksLiveRequestInfo`
        """
        model = BacklinksBacklinksLiveRequestInfo()
        if include_optional:
            return BacklinksBacklinksLiveRequestInfo(
                target = '',
                mode = '',
                custom_mode = {
                    'key' : None
                    },
                field = '',
                value = 56,
                filters = [
                    None
                    ],
                order_by = [
                    ''
                    ],
                offset = 56,
                search_after_token = '',
                limit = 56,
                backlinks_status_type = '',
                include_subdomains = True,
                include_indirect_links = True,
                exclude_internal_backlinks = True,
                tag = ''
            )
        else:
            return BacklinksBacklinksLiveRequestInfo(
        )
        """

    def testBacklinksBacklinksLiveRequestInfo(self):
        """Test BacklinksBacklinksLiveRequestInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
