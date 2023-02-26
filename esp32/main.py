print(" ----------------------------------main.py---------------------------------- ")
import urequests
import machine
import time


button = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_UP)
while True:
    first = button.value()
    time.sleep(0.01) # debounce time
    second = button.value()
    if first and not second:
        print('Button pressed!')

        print('Requesting the alarm ring...')
        base_url = "http://192.168.1.246:8000" # PC
        base_url = "http://192.168.1.240:8000" # Smartphone Novo
        base_url = "http://192.168.1.31:8000" # Smartphone Velho
        print(urequests.post(f"{base_url}/alarm"))
    elif not first and second:
        print('Button released!')
  