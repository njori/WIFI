class ConfigTemplates:

    GUEST_WIFI = """

interface wireless

set wlan2 ssid=GuestWiFi

/ip pool

add name=guest ranges=192.168.20.2-192.168.20.254

"""

    OFFICE_WIFI = """

interface wireless

set wlan1 ssid=OfficeWiFi

"""