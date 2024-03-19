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
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class MigrationStatus(BaseModel):
    """
    MigrationStatus
    """ # noqa: E501
    flash_schema_status: Optional[StrictStr] = Field(default=None, description="Status of the FLASH_SCHEMA process. ")
    flash_schema_message: Optional[StrictStr] = Field(default=None, description="Status message of the FLASH_SCHEMA process. ")
    full_migration_status: StrictStr = Field(description="Status of the FULL_MIGRATION process. ")
    full_migration_message: Optional[StrictStr] = Field(default=None, description="Status message of the FULL_MIGRATION process. ")
    __properties: ClassVar[List[str]] = ["flash_schema_status", "flash_schema_message", "full_migration_status", "full_migration_message"]

    @field_validator('flash_schema_status')
    def flash_schema_status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('Not Run', 'Started', 'Completed', 'Failed'):
            raise ValueError("must be one of enum values ('Not Run', 'Started', 'Completed', 'Failed')")
        return value

    @field_validator('full_migration_status')
    def full_migration_status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('Not Run', 'Started', 'Completed', 'Failed'):
            raise ValueError("must be one of enum values ('Not Run', 'Started', 'Completed', 'Failed')")
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
        """Create an instance of MigrationStatus from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of MigrationStatus from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "flash_schema_status": obj.get("flash_schema_status"),
            "flash_schema_message": obj.get("flash_schema_message"),
            "full_migration_status": obj.get("full_migration_status"),
            "full_migration_message": obj.get("full_migration_message")
        })
        return _obj

