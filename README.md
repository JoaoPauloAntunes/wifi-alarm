# TODO

- [x] Run a ring sound in smartphone using Python
- [x] Create a service to do it, just call the POST /alarm endpoint
- [ ] Install it on smartphone
    - [x] test: install it on "Smartphone Novo"   
    - [ ] test: install it on "Smartphone Velho"   
- [x] Call the endpoint from another device in the same network
- [ ] ...

# Make it yourself

- Install Termux in your smartphone.
- Configure your Termux:
```bash
pkg upgrade
pkg install python
pkg install vlc
pkg install git

git clone https://github.com/JoaoPauloAntunes/wifi-alarm.git
cd wifi-alarm
pip install --upgrade pip
pip install -r requirements.txt
python src/run.py
```
