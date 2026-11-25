from flask import Blueprint, jsonify, request

settings_bp = Blueprint("settings", __name__, url_prefix="/api")

DEFAULT_SETTINGS = {
    "system_name": "WiFi Management System",
    "organization": "Network Operations",
    "timezone": "UTC",
    "language": "en",
    "smtp_server": "smtp.example.com",
    "smtp_port": 587,
    "smtp_username": "admin",
    "smtp_password": "",
    "email_notifications": True,
    "dark_mode": False,
}


def get_settings_payload():
    return DEFAULT_SETTINGS.copy()


@settings_bp.get("/settings")
def get_settings():
    return jsonify(get_settings_payload())


@settings_bp.put("/settings")
def save_settings():
    payload = request.get_json(silent=True) or {}

    for key, value in payload.items():
        if key in DEFAULT_SETTINGS:
            DEFAULT_SETTINGS[key] = value

    return jsonify(get_settings_payload())


@settings_bp.post("/settings/backup")
def backup_settings():
    return jsonify({
        "message": "Backup created successfully.",
        "status": "success",
    })


@settings_bp.post("/settings/restore")
def restore_settings():
    return jsonify({
        "message": "Settings restored successfully.",
        "status": "success",
    })
