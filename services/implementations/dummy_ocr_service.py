from services.interfaces.ocr_service import OCRService


class DummyOCRService(OCRService):

    def extract_text(
        self,
        receipt_path: str
    ):

        return {

            "text": "",

            "confidence": 0.0

        }