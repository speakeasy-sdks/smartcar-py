"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from smartcar import utils
from typing import Optional

class CompassDirection(str, Enum):
    r"""The direction the vehicle is traveling."""
    N = 'N'
    NE = 'NE'
    E = 'E'
    SE = 'SE'
    S = 'S'
    SW = 'SW'
    W = 'W'
    NW = 'NW'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class Compass:
    direction: Optional[CompassDirection] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('direction'), 'exclude': lambda f: f is None }})
    r"""The direction the vehicle is traveling."""
    heading: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('heading'), 'exclude': lambda f: f is None }})
    r"""The direction the vehicle is traveling (in degrees)."""
    

