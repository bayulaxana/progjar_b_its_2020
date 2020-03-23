from FileDBHandler import *
import json
import logging
import os

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
            resp += f"File {filename} successfully uploaded\n"
        except:
            # case when file not found
            resp += f"File {filename} not found\n"
            dest.close()
        return resp

    def listFile(self):
        files = DB.getAll()
        resp = f"Found {len(files)} files on the server\n"
        for x in files:
            resp += json.dumps(x, indent=2) + "\n"
        return resp

    def deleteFile(self, filename: str):
        pass

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
            resp += f"File {filename} successfully downloaded\n"
        except:
            # case when file not found
            resp += f"Cannot find {filename} on the server\n"
            os.remove(filename)
        return resp

fileHandler = FileHandler()

class CommandExecutor:
    def upload(self, arg: str, filename: str):
        return fileHandler.uploadFile(filename)

    def list(self):
        return fileHandler.listFile()

    def download(self, arg: str, filename: str):
        return fileHandler.downloadFile(filename)
    
    def execute(self, cmdInput: str):
        cmdSplit = cmdInput.split(" ")
        cmd = cmdSplit[0]

        if cmd == "upload":
            resp = self.upload(cmdSplit[1], cmdSplit[2])
            return resp
        elif cmd == "list":
            resp = self.list()
            return resp
        elif cmd == "download":
            resp = self.download(cmdSplit[1], cmdSplit[2])
            return resp


if __name__ == "__main__":
    x = {"name":1, "talent":23}
    z = json.dumps(x)
    print(z)