from pathlib import Path
import shutil
from datetime import datetime
import json


# ==========================================================
# Verzeichnisstruktur
# ==========================================================

CAMERA_DIR = Path("/data/camera")

LATEST_DIR = CAMERA_DIR / "latest"
ARCHIVE_DIR = CAMERA_DIR / "archive"
TRAINING_DIR = CAMERA_DIR / "training"
EVENTS_DIR = CAMERA_DIR / "events"

STATUS_FILE = CAMERA_DIR / "status.json"

LATEST_IMAGE = LATEST_DIR / "latest.jpg"

# Aktuell nur Testbild
SOURCE_IMAGE = Path(
    "/app/app/example/example.jpg"
)


class CameraService:

    def __init__(self):

        LATEST_DIR.mkdir(
            parents=True,
            exist_ok=True
        )

        ARCHIVE_DIR.mkdir(
            parents=True,
            exist_ok=True
        )

        TRAINING_DIR.mkdir(
            parents=True,
            exist_ok=True
        )

        EVENTS_DIR.mkdir(
            parents=True,
            exist_ok=True
        )

    def update_latest(self) -> None:

        shutil.copy(
            SOURCE_IMAGE,
            LATEST_IMAGE
        )

    def update_status(self) -> None:

        status = {
            "service": "camera",
            "last_update": datetime.utcnow().isoformat(),
            "status": "running"
        }

        with open(
            STATUS_FILE,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                status,
                file,
                indent=4
            )
