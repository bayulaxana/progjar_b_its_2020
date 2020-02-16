import socket
import sys

# address and port where client would connect to
address_port = ("localhost", 31000)

# create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the socket to the port where the server is listening
sock.connect(address_port)

# open the file which to be sent
files = open("test_client.pdf", "rb")

try:
    # send the files
    print(f"Sending file to server port {address_port[1]}")
    buff = files.read(1024)
    while buff:
        sock.send(buff)
        buff = files.read(1024)

    # receive the respond from the server
    # shutdown socket after sending files
    sock.shutdown(socket.SHUT_WR)
    buff = sock.recv(1024)

    # print the respond message
    print("[Server]: " + buff.decode('utf-8'))

finally:
    print("File sent successfully")
    # close the file
    files.close()
    
    # close the connection
    sock.close()
    print("Connection closed")