from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required

from app.services.device_service import DeviceService

device_bp = Blueprint(
    "devices",
    __name__,
    url_prefix="/api/devices"
)
@device_bp.get("")
@jwt_required()
def get_devices():

    devices = DeviceService.get_all()

    return jsonify([
        device.to_dict()
        for device in devices
    ])

@device_bp.get("/<int:device_id>")
@jwt_required()
def get_device(device_id):

    device = DeviceService.get(device_id)

    return jsonify(device.to_dict())

@device_bp.post("")
@jwt_required()
def create_device():

    data = request.get_json()

    device = DeviceService.create(data)

    return jsonify(device.to_dict()), 201


@device_bp.put("/<int:device_id>")
@jwt_required()
def update_device(device_id):

    data = request.get_json()

    device = DeviceService.update(
        device_id,
        data
    )

    return jsonify(device.to_dict())

@device_bp.delete("/<int:device_id>")
@jwt_required()
def delete_device(device_id):

    DeviceService.delete(device_id)

    return jsonify({
        "message": "Device deleted successfully."
    })