# TODO

- [x] Run a ring sound in smartphone using Python
- [x] Create a service to do it, just call the POST /alarm endpoint
- [x] Install it on smartphone
    - [x] test: install it on "Smartphone Novo"   
    - [x] test: install it on "Smartphone Velho"   
- [x] Call the endpoint from another device in the same network
- [x] Make the API Client: ESP32 + button without retention
    - [x] Make it with ESP32 internal button
    - [x] Make it with external button
- [ ] Install the system at home

# Make it yourself

## Install Termux in your smartphone

- [Termux](https://github.com/termux/termux-app)
- [Termux on android 5 or 6](https://github.com/termux/termux-app/wiki/Termux-on-android-5-or-6)

## Configure your Termux

```bash
pkg upgrade
pkg install python
pkg install vlc
pkg install git

git clone https://github.com/JoaoPauloAntunes/wifi-alarm.git
```

## Configure the API
```bash
cd wifi-alarm/api
pip install --upgrade pip
pip install -r requirements.txt
```

Get your device's IP address (internal network):
```bash
ifconfig
```
Something like: 192.168.1.x

Configure the environments:
```bash
cp sample.env .env
nano .env
```

Then, run the API:
```bash
python src/run.py
```

## Configure the ESP32 microcontroller

Install the esptool program:
```bash
pip install esptool
```

Use the esptool to erase ESP32 flash card:
```bash
esptool --port <port_name> erase_flash
```

Use the esptool to flashing micropython firmware on ESP32
```bash
esptool --chip esp32 --port <serial_port> write_flash -z 0x1000 <esp32-X.bin>
```

Download the VSCode program; install Pymakr, a VScode pluggin; use them to program on the ESP32.
You will need to copy the files from folder "esp32" to the ESP32 flash card.
