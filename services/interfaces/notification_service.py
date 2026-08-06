from abc import ABC, abstractmethod


class NotificationService(ABC):

    @abstractmethod
    def notify_employee(
        self,
        employee,
        message
    ):

        pass

    @abstractmethod
    def notify_manager(
        self,
        manager,
        message
    ):

        pass