from socket import *
import socket
import threading
import time
import sys
import json
import logging
from chat import Chat

chatserver = Chat()

IP_ADDR = "0.0.0.0"
SVR_PORT = 8889

class ClientProcess(threading.Thread):
    def __init__(self, connection, address):
        self.connection = connection
        self.address = address
        threading.Thread.__init__(self)

    def run(self):
        cmd_received = str()
        # receive incoming data from client
        while True:
            data = self.connection.recv(32)
            if data:
                tmp = data.decode("utf-8")
                cmd_received += tmp

                if cmd_received[-2:] == '\r\n':
                    print("==> Data dari client: {}".format(cmd_received).strip())
                    hasil = json.dumps( chatserver.process(cmd_received) )
                    hasil += "\r\n\r\n"
                    print("==> Mengirim respon ke client: {}".format(hasil).strip())
                    self.connection.sendall(hasil.encode())

                    cmd_received = ""
            else:
                break
        print("Koneksi dari {} ditutup".format((self.address)))
        self.connection.close()


class Server(threading.Thread):
    def __init__(self):
        self.client_list = []
        self.my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        threading.Thread.__init__(self)

    def run(self):
        self.my_socket.bind( (IP_ADDR, SVR_PORT) )
        self.my_socket.listen(1)


        while True:
            self.connection, self.client_address = self.my_socket.accept()
            print("Koneksi baru dari {}".format(self.client_address))

            clt = ClientProcess(self.connection, self.client_address)
            clt.start()
            self.client_list.append(clt)

if __name__ == "__main__":
    svr = Server()
    svr.start()
    
