from abc import ABC, abstractmethod


class DatabaseService(ABC):

    @abstractmethod
    def save_expense(self, expense):

        pass

    @abstractmethod
    def update_status(
        self,
        expense_id,
        status
    ):

        pass