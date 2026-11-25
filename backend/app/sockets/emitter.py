from app.extensions import socketio


class SocketEmitter:

    ############################################################
    # ROUTERS
    ############################################################

    @staticmethod
    def router_update(router):

        socketio.emit(
            "router_update",
            router,
            namespace="/network"
        )

    @staticmethod
    def router_online(router):

        socketio.emit(
            "router_online",
            router,
            namespace="/network"
        )

    @staticmethod
    def router_offline(router):

        socketio.emit(
            "router_offline",
            router,
            namespace="/network"
        )

    ############################################################
    # DEVICES
    ############################################################

    @staticmethod
    def device_discovered(device):

        socketio.emit(
            "device_discovered",
            device,
            namespace="/devices"
        )

    @staticmethod
    def device_updated(device):

        socketio.emit(
            "device_updated",
            device,
            namespace="/devices"
        )

    @staticmethod
    def device_removed(device):

        socketio.emit(
            "device_removed",
            device,
            namespace="/devices"
        )

    ############################################################
    # TRAFFIC
    ############################################################

    @staticmethod
    def traffic(data):

        socketio.emit(
            "traffic",
            data,
            namespace="/traffic"
        )

    ############################################################
    # DASHBOARD
    ############################################################

    @staticmethod
    def dashboard(data):

        socketio.emit(
            "dashboard",
            data,
            namespace="/dashboard"
        )

    @staticmethod
    def analytics(data):

        socketio.emit(
            "analytics",
            data,
            namespace="/dashboard"
        )

    ############################################################
    # TOPOLOGY
    ############################################################

    @staticmethod
    def topology(data):

        socketio.emit(
            "topology",
            data,
            namespace="/network"
        )

    ############################################################
    # NOTIFICATIONS
    ############################################################

    @staticmethod
    def notification(notification):

        socketio.emit(
            "notification",
            notification,
            namespace="/notifications"
        )

    ############################################################
    # LOGS
    ############################################################

    @staticmethod
    def log(log):

        socketio.emit(
            "log",
            log,
            namespace="/logs"
        )