# TODO

- [x] Run a ring sound in smartphone using Python
- [x] Create a service to do it, just call the POST /alarm endpoint
- [ ] Install it on smartphone
    - [x] test: install it on "Smartphone Novo"   
    - [ ] test: install it on "Smartphone Velho"   
- [x] Call the endpoint from another device in the same network
- [ ] ...

# Make it yourself

## Install Termux in your smartphone.

- [Termux](https://github.com/termux/termux-app)
- [Termux on android 5 or 6](https://github.com/termux/termux-app/wiki/Termux-on-android-5-or-6)

## Configure your Termux:

```bash
pkg upgrade
pkg install python
pkg install vlc
pkg install git

git clone https://github.com/JoaoPauloAntunes/wifi-alarm.git
cd wifi-alarm
pip install --upgrade pip
pip install -r requirements.txt
```

Get the IP address of this device:   
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
