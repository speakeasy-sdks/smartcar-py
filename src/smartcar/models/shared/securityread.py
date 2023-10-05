"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from smartcar import utils
from typing import Optional

class SecurityReadChargingPortStatus(str, Enum):
    OPEN = 'OPEN'
    CLOSED = 'CLOSED'
    UNKNOWN = 'UNKNOWN'

class SecurityReadChargingPortType(str, Enum):
    CHARGING_PORT = 'chargingPort'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SecurityReadChargingPort:
    status: Optional[SecurityReadChargingPortStatus] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }})
    type: Optional[SecurityReadChargingPortType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type'), 'exclude': lambda f: f is None }})
    


class SecurityReadDoorsStatus(str, Enum):
    OPEN = 'OPEN'
    CLOSED = 'CLOSED'
    UNKNOWN = 'UNKNOWN'

class SecurityReadDoorsType(str, Enum):
    FRONT_LEFT = 'frontLeft'
    FRONT_RIGHT = 'frontRight'
    BACK_LEFT = 'backLeft'
    BACK_RIGHT = 'backRight'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SecurityReadDoors:
    status: Optional[SecurityReadDoorsStatus] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }})
    type: Optional[SecurityReadDoorsType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type'), 'exclude': lambda f: f is None }})
    


class SecurityReadStorageStatus(str, Enum):
    OPEN = 'OPEN'
    CLOSED = 'CLOSED'
    UNKNOWN = 'UNKNOWN'

class SecurityReadStorageType(str, Enum):
    REAR = 'rear'
    FRONT = 'front'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SecurityReadStorage:
    status: Optional[SecurityReadStorageStatus] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }})
    type: Optional[SecurityReadStorageType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type'), 'exclude': lambda f: f is None }})
    


class SecurityReadSunroofStatus(str, Enum):
    OPEN = 'OPEN'
    CLOSED = 'CLOSED'
    UNKNOWN = 'UNKNOWN'

class SecurityReadSunroofType(str, Enum):
    SUNROOF = 'sunroof'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SecurityReadSunroof:
    status: Optional[SecurityReadSunroofStatus] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }})
    type: Optional[SecurityReadSunroofType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type'), 'exclude': lambda f: f is None }})
    


class SecurityReadWindowsStatus(str, Enum):
    OPEN = 'OPEN'
    CLOSED = 'CLOSED'
    UNKNOWN = 'UNKNOWN'

class SecurityReadWindowsType(str, Enum):
    FRONT_LEFT = 'frontLeft'
    FRONT_RIGHT = 'frontRight'
    BACK_LEFT = 'backLeft'
    BACK_RIGHT = 'backRight'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SecurityReadWindows:
    status: Optional[SecurityReadWindowsStatus] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }})
    type: Optional[SecurityReadWindowsType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class SecurityRead:
    charging_port: Optional[list[SecurityReadChargingPort]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('chargingPort'), 'exclude': lambda f: f is None }})
    doors: Optional[list[SecurityReadDoors]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('doors'), 'exclude': lambda f: f is None }})
    is_locked: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('isLocked'), 'exclude': lambda f: f is None }})
    storage: Optional[list[SecurityReadStorage]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('storage'), 'exclude': lambda f: f is None }})
    sunroof: Optional[list[SecurityReadSunroof]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sunroof'), 'exclude': lambda f: f is None }})
    windows: Optional[list[SecurityReadWindows]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('windows'), 'exclude': lambda f: f is None }})
    

