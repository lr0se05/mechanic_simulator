from dataclasses import dataclass
from typing import Optional

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
