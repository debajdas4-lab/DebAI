class RecommendationService:

    def build_response(

        self,

        receipt,

        policy,

        risk,

        approval,

        employee

    ):

        return {

            "receipt": receipt,

            "policy": policy,

            "risk": risk,

            "approval": approval,

            "employee": employee

        }