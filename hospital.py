# 4. Hospital System (Hierarchical Inheritance)

class Hospital:
    def hospital_name(self):
        print("Hospital: City Care Hospital")


class Doctor(Hospital):
    def doctor_info(self):
        print("Doctor: Cardiologist")


class Nurse(Hospital):
    def nurse_info(self):
        print("Nurse: ICU Specialist")


d = Doctor()
n = Nurse()

d.hospital_name()
d.doctor_info()

n.hospital_name()
n.nurse_info()

