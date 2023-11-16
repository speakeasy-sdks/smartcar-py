"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .response import Response
from dataclasses_json import Undefined, dataclass_json
from smartcar import utils
from typing import List, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class BatchResponse:
    responses: Optional[List[Response]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('responses'), 'exclude': lambda f: f is None }})
    

