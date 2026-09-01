from checks import parts_check, wiring_check, torque_check
from models import TorqueSpec, Slot, InstalledPart

spark_plug_torque = TorqueSpec(min_nm=20, target_nm=25, max_nm=30)

ignition_coil_torque = TorqueSpec(min_nm=20, target_nm=25, max_nm=30)

slots = {
    "cyl1_spark_plug": Slot(slot_id="cyl1_spark_plug", required_part_type="spark_plug", requires_connection_to="cyl1_ignition_coil", torque_spec=spark_plug_torque),
    "cyl1_ignition_coil": Slot(slot_id="cyl1_ignition_coil", required_part_type="ignition_coil", requires_connection_to="cyl1_spark_plug", torque_spec=ignition_coil_torque)
                            
}


installed_parts = {
    "cyl1_spark_plug": InstalledPart(slot_id="cyl1_spark_plug", part_type="spark_plug", connected_to="cyl1_ignition_coil", torque=19),
    "cyl1_ignition_coil": InstalledPart(slot_id="cyl1_ignition_coil", part_type="ignition_coil", connected_to="cyl1_spark_plug", torque=31),
    
}

parts_check(slots, installed_parts)
wiring_check(slots, installed_parts)
torque_check(slots, installed_parts)