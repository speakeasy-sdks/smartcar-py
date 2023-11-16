"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from smartcar import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class BatteryLevel:
    percent_remaining: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('percentRemaining'), 'exclude': lambda f: f is None }})
    r"""An EV battery’s state of charge (in percent)."""
    range: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('range'), 'exclude': lambda f: f is None }})
    r"""The estimated remaining distance the vehicle can travel (in kilometers by default or in miles using the sc-unit-system)."""
    

