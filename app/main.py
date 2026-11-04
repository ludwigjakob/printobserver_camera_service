import time

from app.services.camera_service import CameraService


camera = CameraService()

print(
    "PrintObserver Camera Service started",
    flush=True
)

while True:

    try:

        camera.update_latest()

        camera.update_status()

        print(
            "latest.jpg updated",
            flush=True
        )

    except Exception as e:

        print(
            f"Error: {e}",
            flush=True
        )

    time.sleep(5)