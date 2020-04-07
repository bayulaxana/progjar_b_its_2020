import socket
import os
import json

TARGET_IP = "127.0.0.1"
TARGET_PORT = 8889

class ChatClient:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_address = (TARGET_IP, TARGET_PORT)
        self.sock.connect(self.server_address)
        self.tokenid  = ""
        self.username = ""

    def process(self, cmdline: str):
        cmdinput = cmdline.split(" ")
        try:
            command = cmdinput[0].strip()
            
            if command == 'auth':
                options = cmdinput[1].strip()
                if options == 'login':
                    username = cmdinput[2].strip()
                    password = cmdinput[3].strip()
                    return self.login(username, password)
                elif options == 'logout':
                    return self.logout()
            
            elif command == 'send':
                usernameto = cmdinput[1].strip()
                message = ""
                for x in cmdinput[2:]:
                    message = "{} {}".format(message, x)
                return self.send_message(usernameto, message)

            elif command == 'active_user':
                return self.list_active_user()

            elif command == 'inbox':
                return self.inbox()

            else:
                return "Perintah salah"
        except IndexError:
            return "Perintah salah"
    
    def send_string(self, string):
        try:
            self.sock.sendall( string.encode() )
            receive_msg = ""
            while True:
                data = self.sock.recv(64)
                print( "Diterima dari server {}".format(data.decode()).strip() )
                if data:
                    receive_msg = f"{receive_msg}{data.decode()}"
                    if receive_msg[-4:] == "\r\n\r\n":
                        print("end of string\n")
                        return json.loads(receive_msg)
        except:
            self.sock.close()
            return {'status': "Error", 'message': "Gagal"}

    def login(self, username, password):
        string = "auth login {} {} \r\n".format(username, password)
        result = self.send_string(string)

        if result['status'] == 'Ok':
            self.tokenid = result['tokenid']
            self.username = username
            return f"Masuk sebagai {username}. Token ID {self.tokenid}"
        else:
            return f"Error, {result['message']}"

    def logout(self):
        if self.tokenid == "":
            return "Anda belum login"

        string = "auth logout {} \r\n".format(self.tokenid)
        result = self.send_string(string)

        if result['status'] == 'Ok':
            self.tokenid = ""
            self.username = ""
            return "Logout berhasil"
        else:
            return f"Error, {result['message']}"

    def send_message(self, usernameto, message):
        if self.tokenid == "":
            return "Error, login terlebih dahulu"
        
        string = "send {} {} {} \r\n".format(self.tokenid, usernameto, message) 
        result = self.send_string(string)
        if result['status'] == 'Ok':
            return "Pesan telah terkirim ke {}".format(usernameto)
        else:
            return "Error, {}".format(result['message'])

    def list_active_user(self):
        if self.tokenid == "":
            return "Error, login terlebih dahulu"
        
        string = "active_user \r\n"
        result = self.send_string(string)
        list_active = "Daftar user yang aktif\n======================\n"

        if result['status'] == 'Ok':
            for keyid in result['message']:
                list_active += f"{result['message'][keyid]['userdetail']['nama']} "
                list_active += f"[{result['message'][keyid]['username']}] / {keyid}\n"
            return list_active
        else:
            return "Error, {}".format(result['message'])
    
    def inbox(self):
        if self.tokenid == "":
            return "Error, login terlebih dahulu"
        
        string = "inbox {} \r\n".format(self.tokenid)
        result = self.send_string(string)
        if result['status'] == 'Ok':
            return "{}".format(json.dumps(result['message'], indent=2))
        else:
            return "Error, {}".format(result['message'])

if __name__ == "__main__":
    running = ChatClient()
    while True:
        if running.username == "" or running.tokenid == "":
            cmdline = input("[Command] >> ")
        else:
            cmdline = input("[Command {}/{}] >> ".format(running.username, running.tokenid))
        
        if cmdline == 'exit':
            running.process("auth logout")
            break
        print(running.process(cmdline))
        print("")
