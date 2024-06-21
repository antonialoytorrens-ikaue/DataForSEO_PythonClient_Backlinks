# coding: utf-8

"""
    DataForSEO API documentation

    DataForSEO API is the starting point on your journey towards building powerful SEO software. With DataForSEO you can get all the data you need to build an efficient application while also saving your time and budget. DataForSEO API is using the REST technology for interchanging data between your application and our service. The data exchange is made through the widely used HTTP protocol, which allows applying our API to almost all programming languages.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class DataforseoLabsGoogleCompetitorsDomainLiveRequestInfo(BaseModel):
    """
    DataforseoLabsGoogleCompetitorsDomainLiveRequestInfo
    """ # noqa: E501
    target: Optional[StrictStr] = Field(default=None, description="domain required field the domain name of the target website the domain should be specified without https:// and www.")
    location_name: Optional[StrictStr] = Field(default=None, description="full name of the location required field if you don’t specify location_code Note: it is required to specify either location_name or location_code you can receive the list of available locations with their location_name by making a separate request to the https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages example: United Kingdom")
    location_code: Optional[StrictInt] = Field(default=None, description="location code required field if you don’t specify location_name Note: it is required to specify either location_name or location_code you can receive the list of available locations with their location_code by making a separate request to the https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages example: 2840")
    language_name: Optional[StrictStr] = Field(default=None, description="full name of the language required field if you don’t specify language_code Note: it is required to specify either language_name or language_code you can receive the list of available languages with their language_name by making a separate request to the https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages example: English")
    language_code: Optional[StrictStr] = Field(default=None, description="language code required field if you don’t specify language_name Note: it is required to specify either language_name or language_code you can receive the list of available languages with their language_code by making a separate request to the https://api.dataforseo.com/v3/dataforseo_labs/locations_and_languages example: en")
    item_types: Optional[List[StrictStr]] = Field(default=None, description="display results by item type optional field indicates the type of search results included in the response Note: if the item_types array contains item types that are different from organic, the results will be ordered by the first item type in the array; you will not be able to sort and filter results by the types of search results not included in the response; possible values: [\"organic\", \"paid\", \"featured_snippet\", \"local_pack\"] default value: [\"organic\", \"paid\"]")
    include_clickstream_data: Optional[StrictBool] = Field(default=None, description="include or exclude data from clickstream-based metrics in the result optional field if the parameter is set to true, you will receive clickstream_etv, clickstream_gender_distribution, and clickstream_age_distribution fields with clickstream data in the response default value: false with this parameter enabled, you will be charged double the price for the request Note: clickstream data is available for roughly 15% of keywords in the response learn more about how clickstream-based metrics are calculated in this help center article")
    filters: Optional[List[Optional[Dict[str, Any]]]] = Field(default=None, description="array of results filtering parameters optional field you can add several filters at once (8 filters maximum) you should set a logical operator and, or between the conditions the following operators are supported: regex, not_regex, <, <=, >, >=, =, <>, in, not_in example: [\"metrics.organic.count\",\">\",50] [[\"metrics.organic.pos_1\",\"<>\",0],\"and\",[\"metrics.organic.impressions_etv\",\">=\",\"10\"]] [[[\"metrics.organic.count\",\">=\",50],\"and\",[\"metrics.organic.pos_1\",\"in\",[1,5]]], \"or\", [\"metrics.organic.etv\",\">=\",\"100\"]] for more information about filters, please refer to Dataforseo Labs – Filters or this help center guide")
    order_by: Optional[List[StrictStr]] = Field(default=None, description="results sorting rules optional field you can use the same values as in the filters array to sort the results possible sorting types: asc – results will be sorted in the ascending order desc – results will be sorted in the descending order you should use a comma to specify a sorting type example: [\"metrics.paid.etv,asc\"] Note: you can set no more than three sorting rules in a single request you should use a comma to separate several sorting rules example: [\"metrics.organic.etv,desc\",\"metrics.paid.count,asc\"] default rule: [\"metrics.organic.count,desc\"] Note: if the item_types array contains item types that are different from organic, the results will be ordered by the first item type in the array")
    limit: Optional[StrictInt] = Field(default=None, description="the maximum number of returned domains optional field default value: 100 maximum value: 1000")
    offset: Optional[StrictInt] = Field(default=None, description="offset in the results array of returned domains optional field default value: 0 if you specify the 10 value, the first ten keywords in the results array will be omitted and the data will be provided for the successive keywords")
    max_rank_group: Optional[StrictInt] = Field(default=None, description="maximum rank up to which competitors will be considered optional field default value: 100 if you specify 10 here, we will extract competitors from the top 10 Google search results only")
    exclude_top_domains: Optional[StrictBool] = Field(default=None, description="indicates whether to exclude world’s largest websites optional field default value: false set to true if you want to get highly-relevant competitors excluding the websites listed below: wikipedia.org pinterest.com amazon.com google.com facebook.com wordpress.com medium.com quora.com reddit.com youtube.com ebay.com uol.com.br instagram.com olx.com twitter.com linkedin.com slideshare.net")
    intersecting_domains: Optional[List[StrictStr]] = Field(default=None, description="additional domains for improving results accuracy optional field to improve the accuracy of the result, you can specify domains that are known to intersect with the target in SERPs; if you use this array, metrics in the result will be based on SERPs where both target website and intersecting_domains appear; Note: you can specify up to 20 domains in this array")
    tag: Optional[StrictStr] = Field(default=None, description="user-defined task identifier optional field the character limit is 255 you can use this parameter to identify the task and match it with the result you will find the specified tag value in the data object of the response")
    __properties: ClassVar[List[str]] = ["target", "location_name", "location_code", "language_name", "language_code", "item_types", "include_clickstream_data", "filters", "order_by", "limit", "offset", "max_rank_group", "exclude_top_domains", "intersecting_domains", "tag"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of DataforseoLabsGoogleCompetitorsDomainLiveRequestInfo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if location_name (nullable) is None
        # and model_fields_set contains the field
        if self.location_name is None and "location_name" in self.model_fields_set:
            _dict['location_name'] = None

        # set to None if location_code (nullable) is None
        # and model_fields_set contains the field
        if self.location_code is None and "location_code" in self.model_fields_set:
            _dict['location_code'] = None

        # set to None if language_name (nullable) is None
        # and model_fields_set contains the field
        if self.language_name is None and "language_name" in self.model_fields_set:
            _dict['language_name'] = None

        # set to None if language_code (nullable) is None
        # and model_fields_set contains the field
        if self.language_code is None and "language_code" in self.model_fields_set:
            _dict['language_code'] = None

        # set to None if item_types (nullable) is None
        # and model_fields_set contains the field
        if self.item_types is None and "item_types" in self.model_fields_set:
            _dict['item_types'] = None

        # set to None if include_clickstream_data (nullable) is None
        # and model_fields_set contains the field
        if self.include_clickstream_data is None and "include_clickstream_data" in self.model_fields_set:
            _dict['include_clickstream_data'] = None

        # set to None if filters (nullable) is None
        # and model_fields_set contains the field
        if self.filters is None and "filters" in self.model_fields_set:
            _dict['filters'] = None

        # set to None if order_by (nullable) is None
        # and model_fields_set contains the field
        if self.order_by is None and "order_by" in self.model_fields_set:
            _dict['order_by'] = None

        # set to None if limit (nullable) is None
        # and model_fields_set contains the field
        if self.limit is None and "limit" in self.model_fields_set:
            _dict['limit'] = None

        # set to None if offset (nullable) is None
        # and model_fields_set contains the field
        if self.offset is None and "offset" in self.model_fields_set:
            _dict['offset'] = None

        # set to None if max_rank_group (nullable) is None
        # and model_fields_set contains the field
        if self.max_rank_group is None and "max_rank_group" in self.model_fields_set:
            _dict['max_rank_group'] = None

        # set to None if exclude_top_domains (nullable) is None
        # and model_fields_set contains the field
        if self.exclude_top_domains is None and "exclude_top_domains" in self.model_fields_set:
            _dict['exclude_top_domains'] = None

        # set to None if intersecting_domains (nullable) is None
        # and model_fields_set contains the field
        if self.intersecting_domains is None and "intersecting_domains" in self.model_fields_set:
            _dict['intersecting_domains'] = None

        # set to None if tag (nullable) is None
        # and model_fields_set contains the field
        if self.tag is None and "tag" in self.model_fields_set:
            _dict['tag'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DataforseoLabsGoogleCompetitorsDomainLiveRequestInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "target": obj.get("target"),
            "location_name": obj.get("location_name"),
            "location_code": obj.get("location_code"),
            "language_name": obj.get("language_name"),
            "language_code": obj.get("language_code"),
            "item_types": obj.get("item_types"),
            "include_clickstream_data": obj.get("include_clickstream_data"),
            "filters": obj.get("filters"),
            "order_by": obj.get("order_by"),
            "limit": obj.get("limit"),
            "offset": obj.get("offset"),
            "max_rank_group": obj.get("max_rank_group"),
            "exclude_top_domains": obj.get("exclude_top_domains"),
            "intersecting_domains": obj.get("intersecting_domains"),
            "tag": obj.get("tag")
        })
        return _obj


