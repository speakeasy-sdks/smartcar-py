"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import capability as shared_capability
from dataclasses_json import Undefined, dataclass_json
from smartcar import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CompatibilityResponse:
    r"""return Compatibility"""
    
    capabilities: Optional[list[shared_capability.Capability]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('capabilities'), 'exclude': lambda f: f is None }})  
    compatible: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('compatible'), 'exclude': lambda f: f is None }})  
    reason: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('reason'), 'exclude': lambda f: f is None }})  
    