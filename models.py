from dataclasses import dataclass           #Necessary imports
from typing import Optional
from enum import Enum

@dataclass              #Sets the expected information in the dataclass for the torque specifications.
class TorqueSpec:
    min_nm: int
    target_nm: int
    max_nm: int

@dataclass
class Slot:             #Sets the expected information in the dataclass for the individual part slot.
    slot_id: str
    required_part_type: str
    requires_connection_to: Optional[str] = None
    torque_spec: Optional[TorqueSpec] = None

@dataclass
class InstalledPart:            #Sets the expected information in the dataclass for the actual installed parts by the user. 
    slot_id: str
    part_type: str
    connected_to: Optional[str] = None
    torque: Optional[int] = None

class FaultType(str, Enum):
    MISSING_PART = "missing_part"           #Sets the expected information in the class for the different types of faults to help translate the output from checks.py into fault_engine.py for the presented error message to the user.
    INCORRECT_PART = "incorrect_part"
    INCORRECT_CONNECTION = "incorrect_connection"
    LOW_TORQUE = "low_torque"
    HIGH_TORQUE = "high_torque"

@dataclass
class Fault:            #Sets the expected information in the dataclass for the faults if they are found during the checks. 
    slot_id: str
    part_type: str
    fault: FaultType
    detail: str



