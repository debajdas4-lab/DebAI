from services.interfaces.database_service import DatabaseService


class SQLiteDatabaseService(DatabaseService):

    def save_expense(self, expense):

        print("Expense saved")

        return True


    def update_status(
        self,
        expense_id,
        status
    ):
        print(f"Expense {expense_id} status updated to {status}")
        return True
