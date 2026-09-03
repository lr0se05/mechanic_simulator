from models import FaultType

SYMPTOM_MAP = {

    FaultType.MISSING_PART: "No spark - Cylinder misfire",
    FaultType.INCORRECT_PART: "No spark - Cylinder misfire",
    FaultType.INCORRECT_CONNECTION: "Mistimed spark - Rough engine running, possible engine backfire",
    FaultType.LOW_TORQUE: "Poor seal - Hissing/Ticking sound with potential reduced power",
    FaultType.HIGH_TORQUE: "Poor seal - Hissing/Ticking sound with potential reduced power"

}

def get_symptom(fault):
    base_message = SYMPTOM_MAP.get(fault.fault)
    if base_message is None:
        base_message = "Unknown fault type"
        
    return f"{fault.slot_id}: {base_message}"