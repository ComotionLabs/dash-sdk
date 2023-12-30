# coding: utf-8

"""
    Comotion Dash API

    Comotion Dash API

    The version of the OpenAPI document: 2.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictStr, field_validator
from pydantic import Field
from comodash_api_client_lowlevel.models.load_meta_data_error_messages_inner import LoadMetaDataErrorMessagesInner
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class LoadMetaData(BaseModel):
    """
    LoadMetaData
    """ # noqa: E501
    load_status: StrictStr = Field(description="Current status of the load.", alias="LoadStatus")
    error_type: Optional[StrictStr] = Field(default=None, description="Type of error if the load status is FAIL.", alias="ErrorType")
    error_messages: Optional[List[LoadMetaDataErrorMessagesInner]] = Field(default=None, description="Detailed error messages if the load status is FAIL.", alias="ErrorMessages")
    __properties: ClassVar[List[str]] = ["LoadStatus", "ErrorType", "ErrorMessages"]

    @field_validator('load_status')
    def load_status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('OPEN', 'PROCESSING', 'FAIL', 'SUCCESS'):
            raise ValueError("must be one of enum values ('OPEN', 'PROCESSING', 'FAIL', 'SUCCESS')")
        return value

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of LoadMetaData from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in error_messages (list)
        _items = []
        if self.error_messages:
            for _item in self.error_messages:
                if _item:
                    _items.append(_item.to_dict())
            _dict['ErrorMessages'] = _items
        # set to None if error_type (nullable) is None
        # and model_fields_set contains the field
        if self.error_type is None and "error_type" in self.model_fields_set:
            _dict['ErrorType'] = None

        # set to None if error_messages (nullable) is None
        # and model_fields_set contains the field
        if self.error_messages is None and "error_messages" in self.model_fields_set:
            _dict['ErrorMessages'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of LoadMetaData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "LoadStatus": obj.get("LoadStatus"),
            "ErrorType": obj.get("ErrorType"),
            "ErrorMessages": [LoadMetaDataErrorMessagesInner.from_dict(_item) for _item in obj.get("ErrorMessages")] if obj.get("ErrorMessages") is not None else None
        })
        return _obj


