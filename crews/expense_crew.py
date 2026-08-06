"""
Expense Crew

Coordinates all AI agents responsible
for analyzing an employee expense.
"""

from crewai import Crew, Process

from agents.receipt_agent import ReceiptAgent
from agents.policy_agent import PolicyAgent
from agents.risk_agent import RiskAgent
from agents.manager_agent import ManagerAgent
from agents.employee_agent import EmployeeAgent

from tasks.receipt_task import ReceiptTask
from tasks.policy_task import PolicyTask
from tasks.risk_task import RiskTask
from tasks.manager_task import ManagerTask
from tasks.employee_task import EmployeeTask


class ExpenseCrew:

    def crew(self):

        # -----------------------------
        # Agents
        # -----------------------------

        print("Creating Receipt Agent...")
        receipt_agent = ReceiptAgent().agent()

        print("Creating Policy Agent...")
        policy_agent = PolicyAgent().agent()

        print("Creating Risk Agent...")
        risk_agent = RiskAgent().agent()

        print("Creating Manager Agent...")
        manager_agent = ManagerAgent().agent()

        print("Creating Employee Agent...")
        employee_agent = EmployeeAgent().agent()

        print("All Agents Created Successfully.")
        # -----------------------------
        # Tasks
        # -----------------------------

        receipt_task = ReceiptTask().task(
            receipt_agent
        )

        policy_task = PolicyTask().task(
            policy_agent
        )

        risk_task = RiskTask().task(
            risk_agent
        )

        manager_task = ManagerTask().task(
            manager_agent
        )

        employee_task = EmployeeTask().task(
            employee_agent
        )

        # -----------------------------
        # Crew
        # -----------------------------

        return Crew(

            agents=[

                receipt_agent,

                policy_agent,

                risk_agent,

                manager_agent,

                employee_agent

            ],

            tasks=[

                receipt_task,

                policy_task,

                risk_task,

                manager_task,

                employee_task

            ],

            process=Process.sequential,

            verbose=True

        )