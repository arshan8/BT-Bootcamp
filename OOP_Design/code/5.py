# ==================== PATIENT ==================== #
from abc import ABC

class Patient:
    def __init__(self, patient_id, name):
        self.__id = patient_id        # IMMUTABLE
        self.name = name

    @property
    def id(self):
        return self.__id              # read-only

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Patient name must be a string")
        self.__name = value


# ==================== WARD ==================== #

class Ward:
    def __init__(self, ward_id, name):
        self.__id = ward_id           # IMMUTABLE
        self.name = name
        self.__patients = []          # PRIVATE list

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Ward name must be a string")
        self.__name = value

    def admit_patient(self, patient):
        if not isinstance(patient, Patient):
            raise TypeError("Only Patient can be admitted to a Ward")
        self.__patients.append(patient)

    @property
    def patients(self):
        return tuple(self.__patients)   # READ-ONLY


# ==================== HOSPITAL ==================== #

class Hospital:
    def __init__(self, hospital_id, name):
        self.__id = hospital_id        # IMMUTABLE
        self.name = name
        self.__wards = []              # PRIVATE list

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Hospital name must be a string")
        self.__name = value

    def add_ward(self, ward):
        if not isinstance(ward, Ward):
            raise TypeError("Only Ward can be added to Hospital")
        self.__wards.append(ward)

    @property
    def wards(self):
        return tuple(self.__wards)     # READ-ONLY


# ==================== SURGEON ==================== #

class Surgeon(ABC):
    def __init__(self, surgeon_id, name):
        self.__id = surgeon_id         # IMMUTABLE
        self.name = name
        self.__hospitals = []          # PRIVATE list
        self.__operated_patients = []  # PRIVATE list

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Surgeon name must be a string")
        self.__name = value

    def add_hospital(self, hospital):
        if not isinstance(hospital, Hospital):
            raise TypeError("Surgeon can work only for Hospital")
        self.__hospitals.append(hospital)

    def operate(self, patient):
        if not isinstance(patient, Patient):
            raise TypeError("Surgeon can operate only on Patient")
        self.__operated_patients.append(patient)

    @property
    def hospitals(self):
        return tuple(self.__hospitals)   # READ-ONLY

    @property
    def operated_patients(self):
        return tuple(self.__operated_patients)   # READ-ONLY


# ==================== SURGEON TYPES ==================== #

class SeniorSurgeon(Surgeon):
    pass


class NonSeniorSurgeon(Surgeon):
    pass


# ==================== MANAGEMENT SYSTEM ==================== #

class SurgeonManagementSystem:
    def __init__(self):
        self.__surgeons = []           # PRIVATE list

    def add_surgeon(self, surgeon):
        if not isinstance(surgeon, Surgeon):
            raise TypeError("Only Surgeon objects allowed")
        self.__surgeons.append(surgeon)

    @property
    def surgeons(self):
        return tuple(self.__surgeons)  # READ-ONLY

    # 1. Total number of patients being operated
    def total_patients_operated(self):
        return sum(len(s.operated_patients) for s in self.__surgeons)

    # 2. List all patients operated by a surgeon
    def patients_by_surgeon(self, surgeon_id):
        for surgeon in self.__surgeons:
            if surgeon.id == surgeon_id:
                return surgeon.operated_patients
        return ()

    # 3. List all patients admitted to a ward
    def patients_in_ward(self, hospital, ward_id):
        if not isinstance(hospital, Hospital):
            raise TypeError("Invalid Hospital")

        for ward in hospital.wards:
            if ward.id == ward_id:
                return ward.patients
        return ()


# ==================== MAIN / TESTING ==================== #

if __name__ == "__main__":

    # Patients
    p1 = Patient(1, "Alice")
    p2 = Patient(2, "Bob")
    p3 = Patient(3, "Charlie")

    # Ward
    general_ward = Ward(101, "General Ward")
    general_ward.admit_patient(p1)
    general_ward.admit_patient(p2)

    # Hospital
    city_hospital = Hospital(1001, "City Hospital")
    city_hospital.add_ward(general_ward)

    # Surgeons
    s1 = SeniorSurgeon(501, "Dr. Smith")
    s2 = NonSeniorSurgeon(502, "Dr. John")

    s1.add_hospital(city_hospital)
    s2.add_hospital(city_hospital)

    # Operations
    s1.operate(p1)
    s1.operate(p2)
    s2.operate(p3)

    # Management system
    system = SurgeonManagementSystem()
    system.add_surgeon(s1)
    system.add_surgeon(s2)

    # Outputs
    print("Total patients being operated:",
          system.total_patients_operated())

    print("\nPatients operated by Dr. Smith:")
    for p in system.patients_by_surgeon(501):
        print("-", p.name)

    print("\nPatients admitted to General Ward:")
    for p in system.patients_in_ward(city_hospital, 101):
        print("-", p.name)
