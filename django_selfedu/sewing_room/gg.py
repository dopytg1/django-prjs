import socket 

socket_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket_server.bind(("localhost", 8000))
result = socket_server.recv(1024)
print("message: " + result.decode("utf-8"))
socket_server.close()
