import uuid
import shelve
import sys
import json
import time
import os
from datetime import datetime

# definitions of class File
class FileDBHandler:
    def __init__(self):
        self.database = shelve.open("database/db.dat", writeback=True)

    def createData(self, filename: str):
        if filename is None:
            return False
        
        if self.exist(filename):
            self.update(filename)
            return False

        fileID = str( uuid.uuid4() )
        fileNameWExt, fileExt = os.path.splitext(filename)
        fileName = fileNameWExt + fileExt
        timestamp = datetime.now()
        fileSize = os.path.getsize(filename)
        fixedData = {
            "id": str(fileID),
            "fileName": fileName,
            "fileExtension": fileExt,
            "fileSize": fileSize,
            "timestamps": str(timestamp)
        }

        self.database[fileID] = fixedData
        return True

    def exist(self, filename: str):
        for i in self.database.keys():
            if self.database[i]["fileName"] == filename:
                return True
        
        return False
    
    def update(self, filename: str):
        timestamp = datetime.now()
        for i in self.database.keys():
            if self.database[i]["fileName"] == filename:
                self.database[i]["timestamps"] = str(timestamp)
                break

    def getAll(self):
        ret = [ self.database[i] for i in self.database.keys() ]
        return ret
    
    def get(self, filename: str):
        for i in self.database.keys():
            if self.database[i]["fileName"] == filename:
                return self.database[i]