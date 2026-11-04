from pathlib import Path
import os
from datetime import datetime
import json
import subprocess
import tempfile


# ==========================================================
# Verzeichnisstruktur
# ==========================================================
DATA_ROOT = Path(
    os.getenv(
        "PRINTOBSERVER_DATA",
        str(Path.home() / "data")
    )
)

CAMERA_DIR = DATA_ROOT / "camera"

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

        temporary_image = None
        try:
            with tempfile.NamedTemporaryFile(
                dir=LATEST_DIR,
                prefix=".latest-",
                suffix=".jpg",
                delete=False
            ) as file:
                temporary_image = Path(file.name)

            subprocess.run(
                [
                    "rpicam-still",
                    "-n",
                    "--width",
                    "1280",
                    "--height",
                    "720",
                    "-o",
                    str(temporary_image)
                ],
                check=True,
                timeout=30
            )

            os.replace(temporary_image, LATEST_IMAGE)
        finally:
            if temporary_image is not None:
                temporary_image.unlink(missing_ok=True)

    def update_status(self) -> None:

        status = {
            "service": "camera",
            "last_update": datetime.utcnow().isoformat(),
            "status": "running"
        }

        temporary_file = None
        try:
            with tempfile.NamedTemporaryFile(
                mode="w",
                encoding="utf-8",
                dir=CAMERA_DIR,
                prefix=".status-",
                suffix=".tmp",
                delete=False
            ) as file:
                temporary_file = Path(file.name)
                json.dump(
                    status,
                    file,
                    indent=4
                )

            os.replace(temporary_file, STATUS_FILE)
        finally:
            if temporary_file is not None:
                temporary_file.unlink(missing_ok=True)
