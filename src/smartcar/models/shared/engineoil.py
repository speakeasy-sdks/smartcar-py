"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from smartcar import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class EngineOil:
    r"""return engine oil reading"""
    
    life_remaining: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('lifeRemaining'), 'exclude': lambda f: f is None }})
    r"""The engine oil’s remaining life span (as a percentage). Oil life is based on the current quality of the oil. (in percent)."""  
    