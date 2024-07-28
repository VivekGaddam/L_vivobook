# import socket

# # Create a socket object
# client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# # Define the host and port to connect to
# host = '127.0.0.1'
# port = 8080

# # Connect to the server
# client_socket.connect((host, port))

# # Send an HTTP GET request
# request = "GET / HTTP/1.1\r\nHost: 127.0.0.1\r\n\r\n"
# client_socket.sendall(request.encode('utf-8'))

# # Receive the response from the server
# response = client_socket.recv(4096)
# print(response.decode('utf-8'))

# # Close the connection
# client_socket.close()


import socket

# Create a socket object
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server (www.py4inf.com) on port 80 (HTTP)
mysock.connect(('www.py4inf.com', 80))

# Send an HTTP GET request
mysock.send('GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n'.encode("utf8"))

# Receive the response and print it
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode("utf-8"))

# Close the socket
mysock.close()
