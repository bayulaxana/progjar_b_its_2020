import socket
import sys

# input Address and Destination Port
ADDRESS = input("Enter server address: ")
DEST_PORT = int(input("Enter port number: "))

# filename request
file_request = input("Input filename to request: ")

try:
    # address and port where client would connect to
    address_port = (ADDRESS, DEST_PORT)
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

        data = sock.recv(1024)
        if not data:
            print("File not found on the server")
        else:
            f = open("test_result.pdf", "wb")
            f.write(data)
            while True:
                data = sock.recv(1024)
                if data:
                    f.write(data)
                else:
                    f.close()
                    break
            print("File received")

    finally:
        # close connection
        sock.close()
        print("Connection closed")
except:
    print("Error, server is unavailable. Closing...")
    exit(-1)
