from flask import Blueprint, jsonify

health_bp = Blueprint("health", __name__)


@health_bp.route("/")
def home():
    return jsonify({
        "application": "WiFi Management System",
        "version": "1.0.0",
        "status": "running"
    })


@health_bp.route("/api/health")
def health():
    return jsonify({
        "success": True,
        "database": "connected",
        "server": "running"
    })