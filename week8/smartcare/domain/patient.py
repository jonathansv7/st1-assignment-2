class Patient:
    def __init__(self, patient_id: int, name: str, contact_details: str):
        if patient_id is None:
            raise ValueError("Patient ID cannot be empty")
        if not name:
            raise ValueError("Patient name cannot be empty")
        if not contact_details:
            raise ValueError("Contact details cannot be empty")

        self.patient_id = patient_id
        self.name = name
        self.contact_details = contact_details