from pathlib import Path
import shutil

LATEST_IMAGE = Path(
    "/data/camera/latest/latest.jpg"
)

SOURCE_IMAGE = Path(
    "/app/app/example/example.jpg"
)


class CameraService:

    def update_latest(self) -> None:

        LATEST_IMAGE.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        shutil.copy(
            SOURCE_IMAGE,
            LATEST_IMAGE
        )