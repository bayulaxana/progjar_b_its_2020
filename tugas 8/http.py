import sys
import os.path
import uuid
from glob import glob
from datetime import datetime
import cgi, cgitb

class HttpServer:
	def __init__(self):
		self.sessions = {}
		self.types = {}
		self.types['.pdf'] 	= 'application/pdf'
		self.types['.jpg']	= 'image/jpeg'
		self.types['.txt']	= 'text/plain'
		self.types['.html']	= 'text/html'
	
	def response(self,kode=404,message='Not Found',messagebody='',headers={}):
		tanggal = datetime.now().strftime('%c')
		resp = []
		resp.append("HTTP/1.0 {} {}\r\n" . format(kode,message))
		resp.append("Date: {}\r\n" . format(tanggal))
		resp.append("Connection: close\r\n")
		resp.append("Server: myserver/1.0\r\n")
		resp.append("Content-Length: {}\r\n" . format(len(messagebody)))
		
		for kk in headers:
			resp.append("{}:{}\r\n" . format(kk,headers[kk]))
		
		resp.append("\r\n")
		resp.append("{}" . format(messagebody))
		response_str = ''
		
		for i in resp:
			response_str="{}{}" . format(response_str,i)
		
		return response_str

	def proses(self,data):
		requests = data.split("\r\n")
		baris = requests[0]
		
		all_headers = [n for n in requests[1:] if n != '']
		requestArr = baris.split(" ")
		try:
			method = requestArr[0].upper().strip()

			if method == 'GET':
				object_address = requestArr[1].strip()
				print(object_address)
				return self.http_get(object_address, all_headers)
			
			if method == 'POST':
				form = requests[-1].split("=")
				formData = form[1]
				object_address = requestArr[1].strip()
				return self.http_post(object_address, all_headers, formData)
			else:
				return self.response(400,'Bad Request','',{})
		
		except IndexError:
			return self.response(400,'Bad Request','',{})
	
	def http_get(self,object_address,headers):
		files = glob('./*')
		thedir = '.'
		print(thedir+object_address)
		
		if thedir+object_address not in files:
			return self.response(404,'Not Found','',{})
		
		fp = open(thedir + object_address, 'r')
		isi = fp.read()
		fext = os.path.splitext(thedir + object_address)[1]
		content_type = self.types[fext]

		headers = {}
		headers['Content-type'] = "text/html"

		return self.response(200,'OK',isi,headers)

	def http_post(self, object_address, headers, formData):
		allHeaders = headers
		heading = "<h1>Request Header</h1>"
		tempStr = ""

		for header in allHeaders:
			tempStr += f"<li>{header}</li>"
		
		headerContent = f"{heading}<ul>{tempStr}</ul>"
		headerContent = f"{headerContent}<h1>Konten Form</h1><h3>{formData}</h3>"
		
		return self.response(200, 'OK', headerContent, {})

if __name__ == "__main__":
	pass