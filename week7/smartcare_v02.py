from enum import Enum
from datetime import datetime


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


class AppointmentStatus(Enum):
    SCHEDULED = "Scheduled"
    CANCELLED = "Cancelled"


class Appointment:
    def __init__(
        self,
        appointment_id: int,
        patient: Patient,
        practitioner: Practitioner,
        date_time: datetime
    ):
        if appointment_id is None:
            raise ValueError("Appointment ID cannot be empty")
        if patient is None:
            raise ValueError("Patient cannot be empty")
        if practitioner is None:
            raise ValueError("Practitioner cannot be empty")
        if date_time is None:
            raise ValueError("Appointment date and time cannot be empty")

        self.appointment_id = appointment_id
        self.patient = patient
        self.practitioner = practitioner
        self.date_time = date_time
        self.status = AppointmentStatus.SCHEDULED

    def cancel_appointment(self):
        if self.status == AppointmentStatus.CANCELLED:
            raise ValueError("Appointment is already cancelled")

        self.status = AppointmentStatus.CANCELLED