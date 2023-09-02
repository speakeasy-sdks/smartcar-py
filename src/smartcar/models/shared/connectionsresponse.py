"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import cursorpaging as shared_cursorpaging
from ..shared import getconnection as shared_getconnection
from dataclasses_json import Undefined, dataclass_json
from smartcar import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class ConnectionsResponse:
    r"""returns vehicle connections"""
    connections: Optional[list[shared_getconnection.GetConnection]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('connections'), 'exclude': lambda f: f is None }})
    paging: Optional[shared_cursorpaging.CursorPaging] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('paging'), 'exclude': lambda f: f is None }})
    
