import socket
import sys

# input Address and Destination Port
ADDRESS = input("Enter server address: ")
DEST_PORT = int(input("Enter port number: "))

try:
    # open the file which to be sent
    filename = input("Input filename to send: ")
    files = open(filename, "rb")
except:
    print("Error, file does not exist. Closing...")
    exit(-1)

try:
    # address and port where client would connect to
    address_port = (ADDRESS, DEST_PORT)
    # create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # connect the socket to the port where the server is listening
    sock.connect(address_port)

    def send_file():
        buffer = files.read(1024)
        while buffer:
            sock.send(buffer)
            buffer = files.read(1024)

    try:
        # send the files
        print(f"Sending file to server port {address_port[1]}")
        send_file()

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
except:
    print("Error, server is unavailable. Closing...")
    exit(-1)
