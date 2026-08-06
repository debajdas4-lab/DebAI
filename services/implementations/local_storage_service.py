import uuid
import shutil
from pathlib import Path

from config import Config

from services.interfaces.storage_service import StorageService


class LocalStorageService(StorageService):

    def save_receipt(self, upload_file):

        Path(Config.UPLOAD_FOLDER).mkdir(
            parents=True,
            exist_ok=True
        )

        filename = (
            f"{uuid.uuid4()}_{upload_file.filename}"
        )

        destination = (
            Path(Config.UPLOAD_FOLDER) /
            filename
        )

        with destination.open("wb") as buffer:

            shutil.copyfileobj(
                upload_file.file,
                buffer
            )

        return str(destination)
