from datetime import datetime

from domain.patient import Patient
from domain.practitioner import Practitioner
from domain.appointment import Appointment
from services.appointment_service import AppointmentService


# Create a patient
patient = Patient(
    1,
    "John Smith",
    "0400000000"
)

# Create a practitioner
practitioner = Practitioner(
    1,
    "Dr Sarah Jones",
    "General Practice"
)

# Create an appointment
appointment = Appointment(
    1,
    patient,
    practitioner,
    datetime(2026, 10, 1, 10, 30)
)

# Show starting status
print("Appointment created")
print("Patient:", patient.name)
print("Practitioner:", practitioner.name)
print("Status:", appointment.status.value)

# Cancel using the service
service = AppointmentService()
service.cancel_appointment(appointment)

# Show new status
print("Appointment cancelled")
print("Status:", appointment.status.value)