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
from pydantic import BaseModel
from pydantic import Field
from comodash_api_client_lowlevel.models.query_result_result_set import QueryResultResultSet
from comodash_api_client_lowlevel.models.query_result_result_set_meta_data import QueryResultResultSetMetaData
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class QueryResult(BaseModel):
    """
    QueryResult
    """ # noqa: E501
    result_set: Optional[QueryResultResultSet] = Field(default=None, alias="resultSet")
    result_set_meta_data: Optional[QueryResultResultSetMetaData] = Field(default=None, alias="ResultSetMetaData")
    __properties: ClassVar[List[str]] = ["resultSet", "ResultSetMetaData"]

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
        """Create an instance of QueryResult from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of result_set
        if self.result_set:
            _dict['resultSet'] = self.result_set.to_dict()
        # override the default output from pydantic by calling `to_dict()` of result_set_meta_data
        if self.result_set_meta_data:
            _dict['ResultSetMetaData'] = self.result_set_meta_data.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of QueryResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "resultSet": QueryResultResultSet.from_dict(obj.get("resultSet")) if obj.get("resultSet") is not None else None,
            "ResultSetMetaData": QueryResultResultSetMetaData.from_dict(obj.get("ResultSetMetaData")) if obj.get("ResultSetMetaData") is not None else None
        })
        return _obj

