import socket

# Create a socket object
client_socket = socket.socket()

# Connect to the server at a specific IP address and port
client_socket.connect(('192.168.137.1', 8000))

# Send a message to the server
message = "Hello, server!".encode()
client_socket.send(message)

# Receive a response from the server
response = client_socket.recv(1024)

# Print the response
print(f"Received response: {response.decode()}")

# Close the socket
client_socket.close()
