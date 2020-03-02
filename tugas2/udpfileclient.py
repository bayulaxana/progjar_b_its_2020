import socket
import os

# IP Address target and port
TARGET_IP = "127.0.0.1"
TARGET_PORT = 5006

# Initialize for UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# File attributes (name and size)
fileName = "test.txt"
size = os.stat(fileName).st_size

# Open and read the file
fp = open(fileName,'rb')
k = fp.read()

# Send the file to the destination
sent=0
for x in k:
   k_bytes = bytes([x])
   sock.sendto(k_bytes, (TARGET_IP, TARGET_PORT))
   sent = sent + 1
   print(k_bytes,f"terkirim {sent} of {size} ")

# Close the file and shutdown the socket
fp.close();
sock.shutdown(socket.SHUT_WR)