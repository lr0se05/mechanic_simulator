from models import Slot, InstalledPart, TorqueSpec

def parts_check(slots, installed_parts):
    for slot_id, slot in slots.items():
        installed = installed_parts.get(slot_id)

        if installed is None:
            print(f"Missing: {slot_id} is empty (expected {slot.required_part_type})")
        elif installed.part_type != slot.required_part_type:
            print(f"Incorrect Part: {slot_id} has {installed.part_type}, expected {slot.required_part_type}")

def wiring_check(slots, installed_parts):
    for slot_id, slot in slots.items():
        wired = installed_parts.get(slot_id)

        if slot.requires_connection_to is None:
            continue

        elif wired is None:
            continue

        elif wired.connected_to != slot.requires_connection_to:
            print (f"Incorrrect Connection: {slot_id} is connected to {wired.connected_to} but is expected to connect to {slot.requires_connection_to}")

def torque_check(slots, installed_parts):
    for slot_id, slot in slots.items():
        torqued = installed_parts.get(slot_id)

        if slot.torque_spec is None:
            continue

        elif torqued is None:
            continue

        elif torqued.torque is None:
            continue

        elif torqued.torque < slot.torque_spec.min_nm:
            print (f"Incorrect Torque: {slot_id} is too loose, it is tightened with {torqued.torque} but at a minimum needs {slot.torque_spec.min_nm} to prevent it from unattaching")

        elif torqued.torque > slot.torque_spec.max_nm:
            print (f"Incorrect Torque: {slot_id} is too tight, it is tightened with {torqued.torque} but at a maximum needs {slot.torque_spec.max_nm} to prevent it from damaging the thread")

        else:

            continue