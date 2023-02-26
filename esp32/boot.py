print("--boot.py")
import os
import network
import sys
sys.path.append("src")

import config


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
