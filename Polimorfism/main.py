from Persistence import ImpCrudDoctor, ImpCrudHospital
import sys
from ui import messages

crud_doctor = ImpCrudDoctor.ImportCrudDoctor()
crud_hospital = ImpCrudHospital.ImportCrudHospital()

messages.general_presentation()

name_hospital = messages.insert_hospital_name()
hospital_record = crud_hospital.to_get_by(hospital_name=name_hospital)
messages.show_information_hospital(hospital_record)
print("\n")
sys.stdout.flush()
id_doctor = messages.insert_doctor_id()
doctor_record = crud_doctor.to_get_by(id_doctor)
messages.show_information_doctor(doctor_record)
