import socket
import sys

# address and port where client would connect to
address_port = ("localhost", 31001)

# filename request
file_request = "test.txt"

# create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the socket to the port where the server is listening
sock.connect(address_port)

try:
    # sending file request to the server
    print(f"Requesting {file_request} to server....")
    sock.send(file_request.encode())

    # shutdown socket to receive incoming file
    sock.shutdown(socket.SHUT_WR)

    # write incoming file
    f = open("result.txt", "wb")
    while True:
        data = sock.recv(1024)
        if data:
            f.write(data)
        else:
            f.close()
            break
finally:
    print("File received from the server")

    # close connection
    sock.close()
