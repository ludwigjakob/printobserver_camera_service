# printobserver_camera_service
This repository contains the code for the camera service of the project printobserver

## Automatischer Start mit systemd

Deaktiviere zuerst den automatischen Neustart des alten Docker-Containers,
damit nicht Docker und systemd gleichzeitig auf die Kamera zugreifen:

```bash
docker update --restart=no printobserver_camera_service
```

Beende einen manuell laufenden `python -m app.main`-Prozess mit `Ctrl+C`.
Installiere und starte anschließend den systemd-Dienst:

```bash
cd /home/printobserver/printobserver_camera_service
sudo install -m 644 systemd/printobserver-camera.service /etc/systemd/system/printobserver-camera.service
sudo systemctl daemon-reload
sudo systemctl enable --now printobserver-camera.service
```

Der Dienst startet damit sofort und bei jedem zukünftigen Systemstart. Status
und Logs kannst du so prüfen:

```bash
sudo systemctl status printobserver-camera.service
sudo journalctl -u printobserver-camera.service -f
```

Falls der Docker-Container gerade läuft, stoppe ihn vor dem Start des
systemd-Dienstes mit `docker stop printobserver_camera_service`. Beide Dienste
benötigen exklusiven Zugriff auf die Kamera.
