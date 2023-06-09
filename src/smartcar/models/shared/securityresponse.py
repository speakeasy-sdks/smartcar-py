"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from smartcar import utils
from typing import Optional

class SecurityResponseStatusEnum(str, Enum):
    SUCCESS = 'SUCCESS'
    FAILED = 'FAILED'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SecurityResponse:
    r"""return Compatibility"""
    
    message: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('message'), 'exclude': lambda f: f is None }})  
    status: Optional[SecurityResponseStatusEnum] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }})  
    