from datetime import datetime
from app.models.device import Device
from app.repositories.device_repository import DeviceRepository
from app.repositories.network_repository import NetworkRepository
from app.scanners.arp_scanner import ARPScanner
from app.services.vendor_service import VendorService
from app.services.device_classifier import DeviceClassifier
from app.services.notification_service import NotificationService
from app.services.log_service import LogService
from app.services.intrusion_service import IntrusionService
from app.services.topology_service import TopologyService
from app.services.notification_service import NotificationService
from app.sockets.emitter import SocketEmitter


class DiscoveryService:

    @staticmethod
    def scan():

        discovered_devices = []

        online_macs = set()

        networks = NetworkRepository.get_all()

        for network in networks:

            try:

                #
                # Scan Network
                #

                results = ARPScanner.scan(network.cidr)

                for result in results:

                    ip = result["ip_address"]

                    mac = result["mac_address"].upper()

                    hostname = result.get("hostname", ip)

                    manufacturer = VendorService.lookup(mac)

                    device_type = DeviceClassifier.classify(
                        hostname,
                        manufacturer
                    )

                    online_macs.add(mac)

                    device = DeviceRepository.get_by_mac(mac)

                    ##################################################
                    # NEW DEVICE
                    ##################################################

                    if device is None:

                        device = Device(

                            hostname=hostname,

                            device_name=hostname,

                            ip_address=ip,

                            mac_address=mac,

                            manufacturer=manufacturer,

                            operating_system="Unknown",

                            device_type=device_type,

                            signal_strength=0,

                            connection_speed=0,

                            upload_speed=0,

                            download_speed=0,

                            is_connected=True,

                            first_seen=datetime.utcnow(),

                            last_seen=datetime.utcnow(),

                            network_id=network.id,

                            router_id=network.router_id

                        )

                        DeviceRepository.create(device)

                        ##################################################
                        # Log
                        ##################################################

                        LogService.create(

                            level="INFO",

                            action="DEVICE_DISCOVERED",

                            message=f"{hostname} ({ip}) connected."

                        )

                        ##################################################
                        # Notification
                        ##################################################

                        NotificationService.create(

                            title="New Device",

                            message=f"{hostname} joined {network.name}.",

                            notification_type="success"

                        )

                        ##################################################
                        # IDS
                        ##################################################

                        IntrusionService.unknown_device(device)

                    ##################################################
                    # EXISTING DEVICE
                    ##################################################

                    else:

                        device.hostname = hostname

                        device.device_name = hostname

                        device.ip_address = ip

                        device.manufacturer = manufacturer

                        device.device_type = device_type

                        device.last_seen = datetime.utcnow()

                        device.is_connected = True

                        DeviceRepository.update()

                    ##################################################
                    # Socket.IO
                    ##################################################

                    SocketEmitter.device_connected(
                        device.to_dict()
                    )

                    discovered_devices.append(
                        device.to_dict()
                    )

            except Exception as e:

                LogService.create(

                    level="ERROR",

                    action="NETWORK_SCAN",

                    message=str(e)

                )

        ##################################################
        # Detect Offline Devices
        ##################################################

        all_devices = DeviceRepository.get_all()

        for device in all_devices:

            if device.mac_address.upper() not in online_macs:

                if device.is_connected:

                    device.is_connected = False

                    device.last_seen = datetime.utcnow()

                    DeviceRepository.update()

                    LogService.create(

                        level="WARNING",

                        action="DEVICE_OFFLINE",

                        message=f"{device.hostname} disconnected."

                    )

                    NotificationService.create(

                        title="Device Offline",

                        message=f"{device.hostname} disconnected.",

                        notification_type="warning"

                    )
                    NotificationService.send(
                        title="Unknown Device",
                        message=f"{device.mac_address} joined the network.",
                        type="warning"
)

                    SocketEmitter.device_disconnected(

                        device.to_dict()

                    )

        ##################################################
        # Refresh Network Topology
        ##################################################

        SocketEmitter.topology(

            TopologyService.generate()

        )

        ##################################################
        # Broadcast Device List
        ##################################################

        SocketEmitter.device_discovered(

            discovered_devices

        )

        ##################################################
        # Finished
        ##################################################

        return discovered_devices