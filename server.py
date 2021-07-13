import socket
import sqlite3
import json
import psycopg2


connection = psycopg2.connect(dbname='testsitedb', user='admin', 
                        password='Spleenter1q1', host='localhost')
cursor = connection.cursor()

sock = socket.socket()
sock.bind(('localhost', 5000))
sock.listen(10)
conn, addr = sock.accept()

print('connected:', addr)

while True:
    request = conn.recv(1024)
    if not request:
        break   

    jsonData = request.decode('utf-8')
    data = json.loads(jsonData)
    cursor.execute('SELECT serial_number FROM mysite_devices WHERE serial_number = %s',(data[0],))
    if cursor.fetchone()!= None:
        cursor.execute('UPDATE mysite_devices  SET status_input1 = %s, status_output1 = %s,  status_input2 = %s, status_output2 = %s WHERE serial_number = %s',(data[1],data[2],data[3],data[4],data[0],))
    else :
        cursor.execute('INSERT INTO mysite_devices (serial_number, status_input1, status_input2, status_output1, status_output2, voltage, temperature) VALUES (%s, %s, %s, %s, %s, %s, %s)',(data[0],data[1],data[2],data[3],data[4],data[5],data[6],))
    conn.send(b"The data was successfully changed")
conn.close()
#
connection.commit()
connection.close()
