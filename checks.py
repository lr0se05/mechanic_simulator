from models import Slot, InstalledPart, TorqueSpec, FaultType, Fault

def parts_check(slots, installed_parts):
    faults = []
    for slot_id, slot in slots.items():
        installed = installed_parts.get(slot_id)

        if installed is None:
            faults.append(Fault(
                slot_id=slot_id,
                fault=FaultType.MISSING_PART,
                detail=f"{slot_id} is missing, expecting to have {slot.required_part_type} installed"
            ))

        elif installed.part_type != slot.required_part_type:
            faults.append(Fault(
                slot_id=slot_id,
                fault=FaultType.INCORRECT_PART,
                detail=f"Incorrect Part: {slot_id} has {installed.part_type}, expected {slot.required_part_type}"
            ))

    return faults

def wiring_check(slots, installed_parts):
    faults = []
    for slot_id, slot in slots.items():
        wired = installed_parts.get(slot_id)

        if slot.requires_connection_to is None:
            continue

        elif wired is None:
            continue

        elif wired.connected_to != slot.requires_connection_to:
            faults.append(Fault(
                slot_id=slot_id,
                fault=FaultType.INCORRECT_CONNECTION,
                detail=f"Incorrrect Connection: {slot_id} is connected to {wired.connected_to} but is expected to connect to {slot.requires_connection_to}"
            ))

    return faults

def torque_check(slots, installed_parts):
    faults = []
    for slot_id, slot in slots.items():
        torqued = installed_parts.get(slot_id)

        if slot.torque_spec is None:
            continue

        elif torqued is None:
            continue

        elif torqued.torque is None:
            continue

        elif torqued.torque < slot.torque_spec.min_nm:
            faults.append(Fault(
                slot_id=slot_id,
                fault=FaultType.LOW_TORQUE,
                detail=f"Incorrect Torque: {slot_id} is too loose, it is tightened with {torqued.torque} but at a minimum needs {slot.torque_spec.min_nm} to prevent it from unattaching"
            ))

        elif torqued.torque > slot.torque_spec.max_nm:
            faults.append(Fault(
                slot_id=slot_id,
                fault=FaultType.HIGH_TORQUE,
                detail=f"Incorrect Torque: {slot_id} is too tight, it is tightened with {torqued.torque} but at a maximum needs {slot.torque_spec.max_nm} to prevent it from damaging the thread"
            ))

        else:
            continue

    return faults