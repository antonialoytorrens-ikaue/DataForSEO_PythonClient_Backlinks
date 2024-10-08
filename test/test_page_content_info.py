# coding: utf-8

"""
    DataForSEO API documentation

    DataForSEO API is the starting point on your journey towards building powerful SEO software. With DataForSEO you can get all the data you need to build an efficient application while also saving your time and budget. DataForSEO API is using the REST technology for interchanging data between your application and our service. The data exchange is made through the widely used HTTP protocol, which allows applying our API to almost all programming languages.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dataforseo_client.models.page_content_info import PageContentInfo

class TestPageContentInfo(unittest.TestCase):
    """PageContentInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PageContentInfo:
        """Test PageContentInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PageContentInfo`
        """
        model = PageContentInfo()
        if include_optional:
            return PageContentInfo(
                header = dataforseo_client.models.page_section_content_info.PageSectionContentInfo(
                    primary_content = [
                        dataforseo_client.models.content_item_info.ContentItemInfo(
                            text = '', 
                            url = '', 
                            urls = [
                                dataforseo_client.models.content_url_info.ContentUrlInfo(
                                    url = '', 
                                    anchor_text = '', )
                                ], )
                        ], 
                    secondary_content = [
                        dataforseo_client.models.content_item_info.ContentItemInfo(
                            text = '', 
                            url = '', )
                        ], 
                    table_content = [
                        dataforseo_client.models.table_content.TableContent(
                            header = [
                                dataforseo_client.models.table_content_item_info.TableContentItemInfo(
                                    row_cells = [
                                        dataforseo_client.models.row_cell_info.RowCellInfo(
                                            text = '', 
                                            is_header = True, )
                                        ], )
                                ], 
                            body = [
                                dataforseo_client.models.table_content_item_info.TableContentItemInfo()
                                ], 
                            footer = [
                                
                                ], )
                        ], ),
                footer = dataforseo_client.models.page_section_content_info.PageSectionContentInfo(
                    primary_content = [
                        dataforseo_client.models.content_item_info.ContentItemInfo(
                            text = '', 
                            url = '', 
                            urls = [
                                dataforseo_client.models.content_url_info.ContentUrlInfo(
                                    url = '', 
                                    anchor_text = '', )
                                ], )
                        ], 
                    secondary_content = [
                        dataforseo_client.models.content_item_info.ContentItemInfo(
                            text = '', 
                            url = '', )
                        ], 
                    table_content = [
                        dataforseo_client.models.table_content.TableContent(
                            header = [
                                dataforseo_client.models.table_content_item_info.TableContentItemInfo(
                                    row_cells = [
                                        dataforseo_client.models.row_cell_info.RowCellInfo(
                                            text = '', 
                                            is_header = True, )
                                        ], )
                                ], 
                            body = [
                                dataforseo_client.models.table_content_item_info.TableContentItemInfo()
                                ], 
                            footer = [
                                
                                ], )
                        ], ),
                main_topic = [
                    dataforseo_client.models.topic_info.TopicInfo(
                        h_title = '', 
                        main_title = '', 
                        author = '', 
                        language = '', 
                        level = 56, 
                        primary_content = [
                            dataforseo_client.models.content_item_info.ContentItemInfo(
                                text = '', 
                                url = '', 
                                urls = [
                                    dataforseo_client.models.content_url_info.ContentUrlInfo(
                                        url = '', 
                                        anchor_text = '', )
                                    ], )
                            ], 
                        secondary_content = [
                            dataforseo_client.models.content_item_info.ContentItemInfo(
                                text = '', 
                                url = '', )
                            ], 
                        table_content = [
                            dataforseo_client.models.table_content.TableContent(
                                header = [
                                    dataforseo_client.models.table_content_item_info.TableContentItemInfo(
                                        row_cells = [
                                            dataforseo_client.models.row_cell_info.RowCellInfo(
                                                text = '', 
                                                is_header = True, )
                                            ], )
                                    ], 
                                body = [
                                    dataforseo_client.models.table_content_item_info.TableContentItemInfo()
                                    ], 
                                footer = [
                                    
                                    ], )
                            ], )
                    ],
                secondary_topic = [
                    dataforseo_client.models.topic_info.TopicInfo(
                        h_title = '', 
                        main_title = '', 
                        author = '', 
                        language = '', 
                        level = 56, 
                        primary_content = [
                            dataforseo_client.models.content_item_info.ContentItemInfo(
                                text = '', 
                                url = '', 
                                urls = [
                                    dataforseo_client.models.content_url_info.ContentUrlInfo(
                                        url = '', 
                                        anchor_text = '', )
                                    ], )
                            ], 
                        secondary_content = [
                            dataforseo_client.models.content_item_info.ContentItemInfo(
                                text = '', 
                                url = '', )
                            ], 
                        table_content = [
                            dataforseo_client.models.table_content.TableContent(
                                header = [
                                    dataforseo_client.models.table_content_item_info.TableContentItemInfo(
                                        row_cells = [
                                            dataforseo_client.models.row_cell_info.RowCellInfo(
                                                text = '', 
                                                is_header = True, )
                                            ], )
                                    ], 
                                body = [
                                    dataforseo_client.models.table_content_item_info.TableContentItemInfo()
                                    ], 
                                footer = [
                                    
                                    ], )
                            ], )
                    ]
            )
        else:
            return PageContentInfo(
        )
        """

    def testPageContentInfo(self):
        """Test PageContentInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
