import sys
import os.path
import uuid
from glob import glob
from datetime import datetime

class HttpServer:
	def __init__(self):
		self.sessions={}
		self.types={}
		self.types['.pdf']='application/pdf'
		self.types['.jpg']='image/jpeg'
		self.types['.txt']='text/plain'
		self.types['.html']='text/html'

	def response(self, code=404, message='Not found', messagebody='', headers={}):
		dates = datetime.now().strftime('%c')
		responds=[]

		responds.append("HTTP/1.0 {} {}\r\n" . format(code, message))
		responds.append("Date: {}\r\n" . format(dates))
		responds.append("Connection: close\r\n")
		responds.append("Server: myserver/1.0\r\n")
		responds.append("Content-Length: {}\r\n" . format( len(messagebody) ))
		
		for header_content in headers:
			responds.append("{}:{}\r\n" . format(header_content, headers[header_content]))
		
		responds.append("\r\n")
		responds.append("{}" . format(messagebody))

		response_str=''
		for i in responds:	
			response_str="{}{}" . format(response_str, i)
		return response_str

	def proses(self,data):
		requests = data.split("\r\n")
		request_string = requests[0]

		print(request_string)
		request_split = request_string.split(" ")
		try:
			method = request_split[0].upper().strip()
			if method == 'GET':
				object_address = request_split[1].strip()
				return self.http_get(object_address)
			else:
				return self.response(400,'Bad Request','',{})
		except IndexError:
			return self.response(400,'Bad Request','',{})
	
	def http_get(self,object_address):		
		return self.response(200,'OK','<h1>SERVER HTTP</h1>',{})

if __name__=="__main__":
	pass















