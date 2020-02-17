import socket
import sys

ADDRESS = "127.0.0.1"
SERVER_PORT = 31001

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

    # store filename requested by client
    s = ""
    while True:
        data = connection.recv(1024)
        if data:
            s += data.decode("utf-8")
        else:
            break

    print("==> File requested: " + s)
    try:
        f = open(s, "rb")
        buff = f.read(1024)
        while buff:
            connection.send(buff)
            buff = f.read(1024)
        f.close()
    except:
        print(f"==> File {s} not found")
        connection.send(b"")

    # Clean up the connection
    connection.close()