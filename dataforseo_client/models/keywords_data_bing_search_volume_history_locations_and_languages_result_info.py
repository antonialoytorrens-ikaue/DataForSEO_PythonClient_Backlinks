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

from pydantic import BaseModel, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from dataforseo_client.models.available_locations import AvailableLocations
from typing import Optional, Set
from typing_extensions import Self

class KeywordsDataBingSearchVolumeHistoryLocationsAndLanguagesResultInfo(BaseModel):
    """
    KeywordsDataBingSearchVolumeHistoryLocationsAndLanguagesResultInfo
    """ # noqa: E501
    language_name: Optional[StrictStr] = Field(default=None, description="language name")
    language_code: Optional[StrictStr] = Field(default=None, description="language code according to ISO 639-1")
    available_locations: Optional[List[AvailableLocations]] = Field(default=None, description="array of available locations for a certain language")
    __properties: ClassVar[List[str]] = ["language_name", "language_code", "available_locations"]

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
        """Create an instance of KeywordsDataBingSearchVolumeHistoryLocationsAndLanguagesResultInfo from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in available_locations (list)
        _items = []
        if self.available_locations:
            for _item in self.available_locations:
                if _item:
                    _items.append(_item.to_dict())
            _dict['available_locations'] = _items
        # set to None if language_name (nullable) is None
        # and model_fields_set contains the field
        if self.language_name is None and "language_name" in self.model_fields_set:
            _dict['language_name'] = None

        # set to None if language_code (nullable) is None
        # and model_fields_set contains the field
        if self.language_code is None and "language_code" in self.model_fields_set:
            _dict['language_code'] = None

        # set to None if available_locations (nullable) is None
        # and model_fields_set contains the field
        if self.available_locations is None and "available_locations" in self.model_fields_set:
            _dict['available_locations'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of KeywordsDataBingSearchVolumeHistoryLocationsAndLanguagesResultInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "language_name": obj.get("language_name"),
            "language_code": obj.get("language_code"),
            "available_locations": [AvailableLocations.from_dict(_item) for _item in obj["available_locations"]] if obj.get("available_locations") is not None else None
        })
        return _obj


