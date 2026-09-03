from checks import parts_check, wiring_check, torque_check          #Necessary imports
from models import TorqueSpec, Slot, InstalledPart
from fault_engine import get_symptom

spark_plug_torque = TorqueSpec(min_nm=20, target_nm=25, max_nm=30)          # Sets intial torque measurements for testing.
ignition_coil_torque = TorqueSpec(min_nm=20, target_nm=25, max_nm=30)       #To be changed in the future to accurate measurements.
carburetor_torque = TorqueSpec(min_nm=20, target_nm=25, max_nm=30)

slots = {}
for cyl in range(1, 5):         #Repeats the addition to the individual ignition coils and spark plugs to the slots dictionary as 4 of each is needed.

    slots[f"cyl{cyl}_spark_plug"] = Slot(
        slot_id=f"cyl{cyl}_spark_plug",
        required_part_type="spark_plug",
        requires_connection_to=f"cyl{cyl}_ignition_coil",
        torque_spec=spark_plug_torque
    )

    slots[f"cyl{cyl}_ignition_coil"] = Slot(
        slot_id=f"cyl{cyl}_ignition_coil",
        required_part_type="ignition_coil",
        requires_connection_to=f"cyl{cyl}_spark_plug",
        torque_spec=ignition_coil_torque
    )

slots["fuel_pump"] = Slot(slot_id="fuel_pump", required_part_type="fuel_pump", requires_connection_to="carburetor", torque_spec=fuel_pump_torque)       #Adds the fuel pump and carbuerator to the dictionary with its needed information.
slots["carburetor"] = Slot(slot_id="carburetor", required_part_type="carburetor", requires_connection_to="fuel_pump", torque_spec=carburetor_torque)

installed_parts = {
    "cyl1_spark_plug": InstalledPart(slot_id="cyl1_spark_plug", part_type="spark_plug", connected_to="cyl1_ignition_coil", torque=19),
    "cyl1_ignition_coil": InstalledPart(slot_id="cyl1_ignition_coil", part_type="ignition_coil", connected_to="cyl1_spark_plug", torque=31),        #This is the dictionary that represents the actually installed parts by the user, is currently static data for testing purposes. 
    
}

parts_faults = parts_check(slots, installed_parts)          #This runs each function from checks.py to compare the installed parts to the expected parts to flag any faults with the installation in the engine.
wiring_faults = wiring_check(slots, installed_parts)
torque_faults = torque_check(slots, installed_parts)

all_faults = parts_faults + wiring_faults + torque_faults       #Takes all the outputs from the functions in checks.py and then combines them in all_faults to print each output.

for fault in all_faults:
    print(get_symptom(fault))           #Prints any faults that is found in plain english by running the function in fault_engine to translate it for the user. 