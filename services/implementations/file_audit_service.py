from datetime import datetime

from services.interfaces.audit_service import AuditService


class FileAuditService(AuditService):

    def log(
        self,
        action,
        details
    ):

        print(

            datetime.now(),

            action,

            details

        )