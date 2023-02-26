print(" ----------------------------------main.py---------------------------------- ")
import urequests


base_url = "http://192.168.1.246:8000" # PC
base_url = "http://192.168.1.240:8000" # Smartphone Novo
base_url = "http://192.168.1.31:8000" # Smartphone Velho
print(urequests.post(f"{base_url}/alarm"))
