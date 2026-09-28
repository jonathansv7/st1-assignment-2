class Practitioner:
    def __init__(self, practitioner_id: int, name: str, specialty: str):
        if practitioner_id is None:
            raise ValueError("Practitioner ID cannot be empty")
        if not name:
            raise ValueError("Practitioner name cannot be empty")
        if not specialty:
            raise ValueError("Specialty cannot be empty")

        self.practitioner_id = practitioner_id
        self.name = name
        self.specialty = specialty