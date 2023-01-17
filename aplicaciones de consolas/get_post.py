from ast import If
from xml.dom import ValidationErr
import requests
#Recibir
if True:
    resp = requests.get('https://www.google.com/', timeout=0.10)
    print("😁 Respuesta recibida: ", resp)
else:
    print("No hemos recibido respuesta 😥")

# Enviar
if True:
    send_data = {'email': 'cperez@octagono.com.do', 'pass': 'perezdejesus23'}
    val = requests.post('https://github.com/login', data=send_data)
    print("😁 Datos enviados")
else:
    print("Hay bobo 😥")