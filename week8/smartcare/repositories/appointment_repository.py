from abc import ABC, abstractmethod

from domain.appointment import Appointment


class AppointmentRepository(ABC):

    @abstractmethod
    def save(self, appointment: Appointment):
        pass

    @abstractmethod
    def find_by_id(self, appointment_id: int):
        pass