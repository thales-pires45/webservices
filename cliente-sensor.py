import time
from random import randint
import requests

while True:
    temperatura = randint(0, 50)
    dados = {
        "umidade": randint(0, 100),
        "chuva": randint(0, 100),
        "celsius": temperatura,
        "fahrenheit": 32 + (temperatura*1.8),
        "kelvin": 272 + temperatura,
    }
    req = requests.post('http://127.0.0.1:5000/clima/id/', json=dados)

    time.sleep(10)
