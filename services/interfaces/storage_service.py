from abc import ABC, abstractmethod


class StorageService(ABC):

    @abstractmethod
    def save_receipt(self, upload_file) -> str:
        pass