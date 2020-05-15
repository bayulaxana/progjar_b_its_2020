import json
import logging
import os
from FileDBHandler import FileDBHandler

DB = FileDBHandler()
class FileHandler:
    def __init__(self):
        self.dbLocation = "database/db.dat"
        self.fileServerLocation = "fileserver/"
    
    def uploadFile(self, filename: str):
        # file destination
        dest = open(self.fileServerLocation + filename, "wb")
        resp = ""
        try:
            # write to destination
            with open(filename) as f:
                buff = f.read()
                while buff:
                    dest.write( buff.encode() )
                    buff = f.read()
            
            dest.close()
            if not DB.exist(filename):
                DB.createData(filename)
            else:
                DB.update(filename)
            # response
            resp += f"File \"{filename}\" successfully uploaded\n"
            resp += "Detailed information:\n"
            resp += json.dumps(DB.get(filename), indent=2) + "\n"
        except:
            # case when file not found
            resp += f"File \"{filename}\" not found\n"
            dest.close()
            os.remove(filename)
        return resp

    def listFile(self):
        files = DB.getAll()
        resp = f"Found {len(files)} files on the server\n"
        for x in files:
            resp += json.dumps(x, indent=2) + "\n"
        return resp

    def getFile(self, filename: str):
        if DB.exist(filename) == False:
            return f"Cannot find \"{filename}\" on the server\n"
        else:
            files = DB.get(filename)
            resp = json.dumps(files, indent=2) + "\n"
            return resp

    def downloadFile(self, filename: str):
        # file destination
        resp = ""
        try:
            fileDest = open(filename, "wb")
            with open(self.fileServerLocation + filename, "rb") as f:
                buff = f.read()
                while buff:
                    fileDest.write(buff)
                    buff = f.read()
            fileDest.close()
            resp += f"File \"{filename}\" successfully downloaded\n"
            resp += "Detailed information:\n"
            resp += json.dumps(DB.get(filename), indent=2) + "\n"
        except:
            # case when file not found
            resp += f"Cannot find \"{filename}\" on the server\n"
            os.remove(filename)
        return resp

fileHandler = FileHandler()
class CommandExecutor:
    def checkCommand(self, cmd: str):
        cmdList = ["upload", "download", "list", "exit", "quit"]
        if cmd in cmdList: return True
        else: return False
    
    def upload(self, arg: str, filename: str):
        return fileHandler.uploadFile(filename)

    def list(self, arg: str, filename=None):
        if arg == "--all":
            return fileHandler.listFile()
        else:
            return fileHandler.getFile(filename)

    def download(self, arg: str, filename: str):
        return fileHandler.downloadFile(filename)
    
    def execute(self, cmdInput: str):
        cmdSplit = cmdInput.split(" ")
        cmd = cmdSplit[0]

        if self.checkCommand(cmd) == False:
            return "Error, unrecognized command\n"

        if cmd == "upload":
            resp = self.upload(cmdSplit[1], cmdSplit[2])
            return resp
        elif cmd == "list":
            if cmdSplit[1] == "--all":
                return self.list(cmdSplit[1])
            else:
                return self.list(cmdSplit[1], cmdSplit[2])
        elif cmd == "download":
            resp = self.download(cmdSplit[1], cmdSplit[2])
            return resp

if __name__ == "__main__":
    x = FileHandler()
    z = x.getFile("fileTest.txt")
    print(z)