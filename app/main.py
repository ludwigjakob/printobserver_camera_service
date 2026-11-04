import time

from app.services.camera_service import CameraService


camera = CameraService()

print("PrintObserver Camera Service started")


while True:

    try:

        camera.update_latest()

        print(
            "latest.jpg updated"
        )

    except Exception as e:

        print(
            f"Error: {e}"
        )

    time.sleep(5)