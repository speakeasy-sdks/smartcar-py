"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from smartcar import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class TirePressure:
    back_left: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('backLeft'), 'exclude': lambda f: f is None }})
    r"""The current air pressure of the back left tire (in kilopascals by default or in pounds per square inch using the sc-unit-system)."""
    back_right: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('backRight'), 'exclude': lambda f: f is None }})
    r"""The current air pressure of the back right tire (in kilopascals by default or in pounds per square inch using the sc-unit-system)."""
    front_left: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('frontLeft'), 'exclude': lambda f: f is None }})
    r"""The current air pressure of the front left tire (in kilopascals by default or in pounds per square inch using the sc-unit-system)."""
    front_right: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('frontRight'), 'exclude': lambda f: f is None }})
    r"""The current air pressure of the front right tire (in kilopascals by default or in pounds per square inch using the sc-unit-system)."""
    

