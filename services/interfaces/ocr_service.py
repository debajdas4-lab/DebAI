from abc import ABC, abstractmethod


class OCRService(ABC):

    @abstractmethod
    def extract_text(self, receipt_path: str):

        pass