from crewai import Task


class ReceiptTask:

    def task(self, agent):

        return Task(

            description="""
            Analyze the uploaded receipt at {receipt_file} for employee
            {employee_name} ({employee_id}). The submitted expense is
            {expense_type} for {amount}.

            Extract:

            - Vendor
            - Amount
            - Currency
            - Taxes
            - Invoice Number
            - Expense Date

            Validate receipt quality.
            """,

            expected_output="""
            Structured JSON containing receipt information and a confidence
            score. Do not invent values that are not visible in the receipt.
            """,

            agent=agent
        )
