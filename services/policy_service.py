from config import Config


class PolicyService:

    def is_auto_approved(
        self,
        amount: float
    ):

        return (
            amount <=
            Config.AUTO_APPROVAL_LIMIT
        )


    def requires_manager(
        self,
        amount: float
    ):

        return (
            amount >
            Config.MANAGER_APPROVAL_LIMIT
        )
