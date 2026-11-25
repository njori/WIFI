from flask import request

from app.extensions import socketio


@socketio.on("connect", namespace="/dashboard")
def dashboard_connect():

    print(f"Dashboard connected {request.sid}")


@socketio.on("disconnect", namespace="/dashboard")
def dashboard_disconnect():

    print(f"Dashboard disconnected {request.sid}")


@socketio.on("connect", namespace="/network")
def network_connect():

    print(f"Network connected {request.sid}")


@socketio.on("disconnect", namespace="/network")
def network_disconnect():

    print(f"Network disconnected {request.sid}")


@socketio.on("connect", namespace="/devices")
def device_connect():

    print(f"Devices connected {request.sid}")


@socketio.on("disconnect", namespace="/devices")
def device_disconnect():

    print(f"Devices disconnected {request.sid}")


@socketio.on("connect", namespace="/traffic")
def traffic_connect():

    print(f"Traffic connected {request.sid}")


@socketio.on("disconnect", namespace="/traffic")
def traffic_disconnect():

    print(f"Traffic disconnected {request.sid}")


@socketio.on("connect", namespace="/notifications")
def notification_connect():

    print(f"Notifications connected {request.sid}")


@socketio.on("disconnect", namespace="/notifications")
def notification_disconnect():

    print(f"Notifications disconnected {request.sid}")


@socketio.on("connect", namespace="/logs")
def log_connect():

    print(f"Logs connected {request.sid}")


@socketio.on("disconnect", namespace="/logs")
def log_disconnect():

    print(f"Logs disconnected {request.sid}")