from abc import ABC, abstractmethod


class AuditService(ABC):

    @abstractmethod
    def log(
        self,
        action,
        details
    ):

        pass

# Later this becomes
# ELK
# Splunk
# Azure Monitor