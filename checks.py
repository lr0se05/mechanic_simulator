from models import Slot, InstalledPart, TorqueSpec, FaultType, Fault            #Necessary imports

def parts_check(slots, installed_parts):            #This function just compares the expected parts to the actual installed parts from main.py
    faults = []                 #This is created to monitor any found faults so that it can be processed through the fault_engine to be returned back to the user 
    for slot_id, slot in slots.items(): 
        installed = installed_parts.get(slot_id)

        if installed is None:                   #This check that if the slot which should have something installed is not present and then appends the necessary information to faults
            faults.append(Fault(
                slot_id=slot_id,
                fault=FaultType.MISSING_PART,
                detail=f"{slot_id} is missing, expecting to have {slot.required_part_type} installed"
            ))

        elif installed.part_type != slot.required_part_type:            #This checks to see if the actually installed slot and the expected installed slot match, if not appends it to faults and returns.
            faults.append(Fault(
                slot_id=slot_id,
                fault=FaultType.INCORRECT_PART,
                detail=f"Incorrect Part: {slot_id} has {installed.part_type}, expected {slot.required_part_type}"
            ))

    return faults               #Returns all found faults back to main.py to be processed through fault_engine.py to be informed to the user. 

def wiring_check(slots, installed_parts):           #This function checks to make sure any parts are connected to the correct necessary part
    faults = []
    for slot_id, slot in slots.items():
        wired = installed_parts.get(slot_id)

        if slot.requires_connection_to is None:             #Checks to see if the requires_connection_to is None meaning it does not need to be connected to anything so can continue to the next item. 
            continue

        elif wired is None:             #Checks to see if the actual installed parts is None, if it is None then the item is not present so skips that item as it would of already been picked up by the parts checker. 
            continue

        elif wired.connected_to != slot.requires_connection_to:         #Checks to see if the actual connection matches what the expected connection is, if they are not appends it to faults to be returned back to main.py
            faults.append(Fault(
                slot_id=slot_id,
                fault=FaultType.INCORRECT_CONNECTION,
                detail=f"Incorrrect Connection: {slot_id} is connected to {wired.connected_to} but is expected to connect to {slot.requires_connection_to}"
            ))

    return faults               #Returns all found faults back to main.py to be processed through fault_engine.py to be informed to the user. 

def torque_check(slots, installed_parts):
    faults = []
    for slot_id, slot in slots.items():
        torqued = installed_parts.get(slot_id)

        if slot.torque_spec is None:        #These are the same relevant checks of wiring checks to make sure that not repeat errors flag back to the user to remove confusion. 
            continue

        elif torqued is None:
            continue

        elif torqued.torque is None:
            continue

        elif torqued.torque < slot.torque_spec.min_nm:          #Checks to see if the inputted torque is lower then the minimum range allowed for the part, if it is appends the fault to the list 
            faults.append(Fault(
                slot_id=slot_id,
                fault=FaultType.LOW_TORQUE,
                detail=f"Incorrect Torque: {slot_id} is too loose, it is tightened with {torqued.torque} but at a minimum needs {slot.torque_spec.min_nm} to prevent it from unattaching"
            ))

        elif torqued.torque > slot.torque_spec.max_nm:      #Checks to see if the inputted torque is higher then the maximum range allowed for the part, if it is appends the fault to the list 
            faults.append(Fault(
                slot_id=slot_id,
                fault=FaultType.HIGH_TORQUE,
                detail=f"Incorrect Torque: {slot_id} is too tight, it is tightened with {torqued.torque} but at a maximum needs {slot.torque_spec.max_nm} to prevent it from damaging the thread"
            ))

        else:
            continue

    return faults               #Returns all found faults back to main.py to be processed through fault_engine.py to be informed to the user. 
