from json import encoder
import socket
import json

data = input("Запись данных в формате: Серийный номер; Вход1; Выход1; Вход2; Выход2; Напряжение; Температура\n").split(';')

print(data)
print(type(data))

jsonData = json.dumps(data)
print(type(jsonData))

sock = socket.socket()
sock.connect((socket.gethostbyname('http://vasilievpavel.pythonanywhere.com'), 5050))
sock.sendall(bytes(jsonData,encoding="utf-8"))
data = sock.recv(1024)
print((data.decode('utf-8')))
sock.close()   
