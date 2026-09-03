from models import FaultType        #Necessary imports

SYMPTOM_MAP = {

    FaultType.MISSING_PART: "No spark - Cylinder misfire",          #Sets the initial translation dictionary to the plain english for the user to receive. 
    FaultType.INCORRECT_PART: "No spark - Cylinder misfire",
    FaultType.INCORRECT_CONNECTION: "Mistimed spark - Rough engine running, possible engine backfire",
    FaultType.LOW_TORQUE: "Poor seal - Hissing/Ticking sound with potential reduced power",
    FaultType.HIGH_TORQUE: "Poor seal - Hissing/Ticking sound with potential reduced power"

}

def get_symptom(fault):
    base_message = SYMPTOM_MAP.get(fault.fault)         #This function is called in main.py to display the translate the error message into plain english for the user.
    if base_message is None:
        base_message = "Unknown fault type"         #If the error message ever returns as None then it is not specified in the SYMPTOM_MAP so to remove confusion will state Unknown fault type.
        
    return f"{fault.slot_id}: {base_message}"           #Returns the error message in a clean fashion for the user to receive. 