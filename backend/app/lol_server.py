import socket

server_socket = socket.socket()
server_socket.bind(('192.168.137.1', 8000))
server_socket.listen()
client_socket, client_address = server_socket.accept()


message = client_socket.recv(1024)


print(f"Received message: {message.decode()}")

response = "Hello, client!".encode()
client_socket.send(response)

client_socket.close()
server_socket.close()
