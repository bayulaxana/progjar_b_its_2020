import socket
import json
import os
import time

IP_ADDR = "0.0.0.0"
PORT = 8685
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def startConnection():
    sock.connect((IP_ADDR, PORT))

if __name__ == "__main__":
    # connect to the server
    try:
        print(f"Connecting to server {IP_ADDR}:{PORT}")
        time.sleep(1)
        startConnection()
    except:
        print("Server is unreachable")
        print("Exiting...")
        exit(-1)

    # begin to input command
    print("Connected! OK!\n")
    while True:
        cmdInput = input("> ")
        cmdSplit = cmdInput.split(" ")
        cmd = cmdSplit[0]
        
        if cmd == "exit" or cmd == "quit":
            sock.send(cmdInput.encode())
            break
        else:
            if cmd == "download":
                print("Downloading file...")
            sock.send(cmdInput.encode())
        
        # accepting response
        response = sock.recv(4096)
        print(response.decode("utf-8"))
    
    sock.close()
