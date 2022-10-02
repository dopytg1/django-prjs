from http import server
import socket

someDict = [{"key1": "value1"}, {"k1": "v1", "k2": "v2", "k3": "v3"}, {}, {}, {"key1": "value1"}, {"key1": "value1"}, {"key2": "value2"}]

newDict = []

for each in someDict:
    if each not in newDict:
        newDict.append(each)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(("localhost", 8000))

while True:
    try:
        result = server_socket.recv(1024)
    except KeyboardInterrupt:
        server_socket.close()
        break
    else:
        print("message: " + result.decode("utf-8"))
