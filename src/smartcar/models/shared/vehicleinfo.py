"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from smartcar import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class VehicleInfo:
    r"""A single vehicles"""
    
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})  
    make: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('make') }})  
    model: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('model') }})  
    year: int = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('year') }})  
    