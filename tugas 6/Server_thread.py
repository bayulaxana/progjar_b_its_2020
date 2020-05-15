from socket import *
import socket
import threading
import time
import sys
import logging
from HTTP_server import HttpServer

httpserver = HttpServer()


class ClientHandler(threading.Thread):
	def __init__(self, connection, address):
		self.connection = connection
		self.address = address
		threading.Thread.__init__(self)

	def run(self):
		received = ""
		while True:
			try:
				data = self.connection.recv(32)
				if data:
					tmp = data.decode()
					received=received + tmp
					if received[-2:] == '\r\n':
						#end of command, proses string
						
						# logging.warning("data dari client: {}" . format(received))
						print("Data from client: {}".format(received))
						result = httpserver.proses(received)
						result = result + "\r\n\r\n"
						
						# logging.warning("balas ke  client: {}" . format(result))
						print("Reply to client: {}".format(result))
						self.connection.sendall(result.encode())
						received = ""
						self.connection.close()
				else:
					break
			except OSError as e:
				pass
		self.connection.close()

class Server(threading.Thread):
	def __init__(self):
		self.client_list = []
		self.my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		threading.Thread.__init__(self)

	def run(self):
		self.my_socket.bind(('127.0.0.1', 10001))
		self.my_socket.listen(1)
		while True:
			self.connection, self.client_address = self.my_socket.accept()
			# logging.warning("connection from {}".format(self.client_address))
			print("New Connection from {}".format(self.client_address))

			clt = ClientHandler(self.connection, self.client_address)
			clt.start()
			self.client_list.append(clt)

def main():
	svr = Server()
	svr.start()

if __name__=="__main__":
	main()

