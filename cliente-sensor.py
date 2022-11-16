import time
from random import randint
from datetime import datetime
import requests

id = 0

while True:
    data = str(datetime.now().date())
    hora = str(datetime.now().strftime("%H:%M:%S"))
    id += 1
    temperatura = randint(0, 50)
    dados = {
        "id": id,
        "umidade": randint(0, 100),
        "chuva": randint(0, 100),
        "celsius": temperatura,
        "fahrenheit": 32 + (temperatura*1.8),
        "kelvin": 272 + temperatura,
        "data": data,
        "hora": hora,
    }
    req = requests.post('http://127.0.0.1:5000/clima/', json=dados)

    time.sleep(10)
