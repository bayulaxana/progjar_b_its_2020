import socket
import sys

ADDRESS = "127.0.0.1"
SERVER_PORT = 31000

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = (ADDRESS, SERVER_PORT)
print("Starting up on {0} port {1}".format(server_address[0], server_address[1]))
print("===================================")
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print("Waiting for a connection")
    connection, client_address = sock.accept()

    print(f"==> Accepted connection from {client_address}")

    # open file for writing
    f = open("server/test_server.pdf", "wb")

    while True:
        data = connection.recv(1024)
        if data:
            f.write(data)
        else:
            f.close()
            break

    print("==> File received successfully")

    # server sends respond to client
    # confirming the file has received
    msg = b"Server has received the file"
    connection.sendall(msg)

    # Clean up the connection
    connection.close()
