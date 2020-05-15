import sys
import os
import json
import uuid
import logging
from queue import  Queue

## User List
user_list = {
    "messi" : {
        "username" : "messi",
        "nama" : "Lionel Messi",
        "password" : "surabaya",
        "incoming" : {},
        "outgoing" : {}
    },
    "lineker" : {
        "username" : "lineker",
        "nama" : "Gary Lineker",
        "password" : "surabaya",
        "incoming" : {},
        "outgoing" : {}
    },
    "bayulaxana" : {
        "username" : "bayulaxana",
        "nama" : "Bayu Laksana",
        "password" : "password123",
        "incoming" : {},
        "outgoing" : {}
    }
}
##

class Chat:
    def __init__(self):
        self.sessions = {}
        self.users = {}
        
        for key in user_list:
            self.users[key] = user_list[key]
    
    def process(self, data: str):
        cmdinput = data.split(" ")
        try:
            command = cmdinput[0].strip()
            if command == 'auth':
                options = cmdinput[1].strip()
                if options == 'login':
                    username = cmdinput[2].strip()
                    password = cmdinput[3].strip()
                    # server print
                    return self.authenticate_user(username, password)
                elif options == 'logout':
                    sessionid = cmdinput[2].strip()
                    return self.authenticate_logout(sessionid)
            
            elif command == 'send':
                sessionid = cmdinput[1].strip()
                usernameto = cmdinput[2].strip()
                message = ""
                for x in cmdinput[3:]:
                    message = "{} {}".format(message, x)
                usernamefrom = self.sessions[sessionid]['username']
                # server print
                return self.send_message(sessionid, usernamefrom, usernameto, message)
            
            elif command == 'inbox':
                sessionid = cmdinput[1].strip()
                username = self.sessions[sessionid]['username']
                # server print
                return self.get_inbox(username)

            elif command == 'active_user':
                return self.get_active_user()
            
            else:
                return {'status': 'Error', 'message': '>> Protokol tidak benar'}
        except KeyError:
            return {'status': 'Error', 'message': 'Informasi tidak ditemukan'}
        except IndexError:
            return {'status': 'Error', 'message': '-> Protokol tidak benar'}

    def authenticate_logout(self, tokenid):
        if tokenid not in self.sessions:
            return {"status": "Error", "message": "User tidak ada"}
        
        # delete token id
        self.sessions.pop(tokenid)
        return {"status": "Ok", "message": "Berhasil logout"}
    
    def authenticate_user(self, username: str, password: str):
        # auth handling (username dan password)
        if username not in self.users:
            return {"status": "Error", "message": "User tidak ada"}
        else:
            if password != self.users[username]["password"]:
                return {"status": "Error", "message": "Login gagal"}
        # generate token
        token_id = str( uuid.uuid4() )
        self.sessions[token_id] = {
            'username': username,
            'userdetail': self.users[username]
        }
        return {"status": "Ok", "tokenid": token_id}

    def get_user(self, username):
        if username not in self.users: return False
        return self.users[username]

    def send_message( self, sessionid, username_from, username_dest, message ):
        if sessionid not in self.sessions:
            return {"status": "Error", "message": "Session tidak ditemukan"}
        
        s_fr = self.get_user(username_from)
        s_to = self.get_user(username_dest)
        # user not found
        if s_fr == False or s_to == False:
            return {"status": "Error", "message": "User tidak ditemukan"}
        
        message_detail = {
            'msg_from': s_fr['nama'],
            'msg_to': s_to['nama'],
            'msg': message
        }
        outqueue_sender  = s_fr['outgoing']
        inqueue_receiver = s_to['incoming']

        # insert the message to the queue
        try:
            outqueue_sender[username_from].put(message_detail)
        except KeyError:
            outqueue_sender[username_from] = Queue()
            outqueue_sender[username_from].put(message_detail)

        try:
            inqueue_receiver[username_from].put(message_detail)
        except KeyError:
            inqueue_receiver[username_from] = Queue()
            inqueue_receiver[username_from].put(message_detail)
        
        return {'status': 'Ok', 'message': 'Pesan terkirim'}

    def get_active_user(self):
        return {"status": "Ok", "message": self.sessions}

    def get_inbox(self, username):
        s_fr = self.get_user(username)
        if s_fr:
            incoming = s_fr['incoming']
            msgs = {}
            for users in incoming:
                msgs[users] = []
                while not incoming[users].empty():
                    msgs[users].append(
                        s_fr['incoming'][users].get_nowait()
                    )
            
            return {"status": "Ok", "message": msgs}
        

if __name__ == "__main__":
    pass