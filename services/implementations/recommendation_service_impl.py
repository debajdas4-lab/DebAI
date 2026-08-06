from services.interfaces.recommendation_service import RecommendationService

from models.expense_response import ExpenseResponse


class RecommendationServiceImpl(
    RecommendationService
):

    def build_response(

        self,

        receipt,

        policy,

        risk,

        approval,

        employee

    ):

        return ExpenseResponse(

            status="SUCCESS",

            receipt=receipt,

            policy=policy,

            risk=risk,

            approval=approval,

            employee=employee

        )