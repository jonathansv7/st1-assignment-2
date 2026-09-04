appointments = []


def book_appointment(patient_name, practitioner_name, appointment_time):
    appointment = {
        "patient": patient_name,
        "practitioner": practitioner_name,
        "time": appointment_time
    }

    appointments.append(appointment)


def display_appointments():
    for appointment in appointments:
        print("Patient:", appointment["patient"])
        print("Practitioner:", appointment["practitioner"])
        print("Appointment time:", appointment["time"])


# Welcome message
print("Welcome to SmartCare Community Clinic!")
print("Appointment Booking System")
print()

# Add appointments
book_appointment("Alice Smith", "Dr. John Doe", "2024-07-20 10:00 AM")
book_appointment("Bob Johnson", "Dr. Jane Roe", "2024-07-20 11:30 AM")

# Display appointments
print("Appointments:")
print("----------------------")
display_appointments()