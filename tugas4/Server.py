import os
import threading
import json
import socket
from FileHandler import CommandExecutor

commExe = CommandExecutor()

class ClientHandler(threading.Thread):
    def __init__(self, connection, addr):
        self.connection = connection
        self.clientAddr = addr
        threading.Thread.__init__(self)

    def run(self):
        while True:
            data = self.connection.recv(1024)
            comm = data.decode("utf-8")
            if comm == "exit" or comm == "quit":
                break
            else:
                print(f">> Received \"{comm}\" from {self.clientAddr}")
                response = commExe.execute(comm)
                self.connection.send(response.encode())
        
        print(f"Connection from {self.clientAddr} closed")
        self.connection.close()


class Server(threading.Thread):
    def __init__(self):
        self.ipAddr   = "0.0.0.0"
        self.portConn = 8685
        self.clients  = []
        self.sockets  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        threading.Thread.__init__(self)
    
    def run(self):
        self.sockets.bind( (self.ipAddr, self.portConn) )
        self.sockets.listen(1)

        while True:
            self.connection, self.clientAddr = self.sockets.accept()
            print(f"New connection from {self.clientAddr}")
            
            client = ClientHandler(self.connection, self.clientAddr)
            client.start()
            self.clients.append(client)

if __name__ == "__main__":
    x = Server()
    x.start()