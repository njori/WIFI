from app.scanners.arp_scanner import ARPScanner

devices = ARPScanner.scan(
    "192.168.0.0/24"
)

for device in devices:
    print(device)