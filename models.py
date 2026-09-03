from dataclasses import dataclass
from typing import Optional
from enum import Enum

@dataclass
class TorqueSpec:
    min_nm: int
    target_nm: int
    max_nm: int

@dataclass
class Slot:
    slot_id: str
    required_part_type: str
    requires_connection_to: Optional[str] = None
    torque_spec: Optional[TorqueSpec] = None

@dataclass
class InstalledPart:
    slot_id: str
    part_type: str
    connected_to: Optional[str] = None
    torque: Optional[int] = None

class FaultType(str, Enum):
    MISSING_PART = "missing_part"
    INCORRECT_PART = "incorrect_part"
    INCORRECT_CONNECTION = "incorrect_connection"
    LOW_TORQUE = "low_torque"
    HIGH_TORQUE = "high_torque"

@dataclass
class Fault:
    slot_id: str
    part_type: str
    fault: FaultType
    detail: str



