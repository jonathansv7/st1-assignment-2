from enum import Enum
from datetime import datetime

from domain.patient import Patient
from domain.practitioner import Practitioner


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