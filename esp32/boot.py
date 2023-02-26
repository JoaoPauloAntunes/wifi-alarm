print(" ----------------------------------boot.py----------------------------------")
import network

import config

if config.INSTALL_PACKAGES:
    import upip


def do_connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    print(wlan.scan())
    if not wlan.isconnected():
        print('Connecting to network...')
        wlan.connect(config.SSID, config.PASSWORD)
        while not wlan.isconnected():
            pass
    print(f'network config: {wlan.ifconfig()}')

if config.TURN_ON_WIFI:
    do_connect()

if config.INSTALL_PACKAGES:
    upip.install("pystone_lowmem")
    