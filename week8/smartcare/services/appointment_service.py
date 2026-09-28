from domain.appointment import Appointment


class AppointmentService:
    def cancel_appointment(self, appointment: Appointment):
        appointment.cancel_appointment()
        return appointment