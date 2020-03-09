import socket

# IP Address target and port
TARGET_IP   = "192.168.100.21"
TARGET_PORT = 5006

# Initialize for UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Data to send
data_to_send = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Send the data
sock.sendto( bytes(data_to_send.encode()), (TARGET_IP,TARGET_PORT) )