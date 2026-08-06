from services.interfaces.notification_service import NotificationService


class ConsoleNotificationService(NotificationService):

    def notify_employee(
        self,
        employee,
        message
    ):

        print(
            f"Employee: {employee}"
        )


    def notify_manager(
        self,
        manager,
        message
    ):

        print(
            f"Manager: {manager}"
        )

# Later replace with Teams.