# import socket

# # Create a socket object
# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# # Define the host and port
# host = '127.0.0.1'
# port = 8080

# # Bind the socket to the address
# server_socket.bind((host, port))

# # Listen for incoming connections
# server_socket.listen(5)
# print(f"Server listening on {host}:{port}")

# while True:
#     # Accept a connection from a client
#     client_socket, addr = server_socket.accept()
#     print(f"Connection from {addr}")

#     # Receive the request from the client
#     request = client_socket.recv(1024).decode('utf-8')
#     print(f"Request: {request}")

#     # Simple HTTP response
#     response = """HTTP/1.1 200 OK
# Content-Type: text/html
# <html>
#     <body>
#         <h1>Hello, World!</h1>
#     </body>
# </html>"""
    
#     # Send the response to the client
#     client_socket.sendall(response.encode('utf-8'))
    
#     # Close the connection
#     client_socket.close()



import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the host and port
host = '127.0.0.1'
port = 8080

# Bind the socket to the address
server_socket.bind((host, port))

# Listen for incoming connections
server_socket.listen(5)
print(f"Server listening on {host}:{port}")

while True:
    # Accept a connection from a client
    client_socket, addr = server_socket.accept()
    print(f"Connection from {addr}")

    while True:
        # Receive data from the client
        data = client_socket.recv(1024)
        if not data:
            break
        # Echo the received data back to the client
        client_socket.sendall(data)

    # Close the connection
    client_socket.close()
