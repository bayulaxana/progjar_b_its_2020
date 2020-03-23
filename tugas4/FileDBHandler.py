import uuid
import shelve
import sys
import json
import time
from datetime import datetime

# definitions of class File
class FileDBHandler:
    
    # Constructor
    ## it creates databases for storing attributes
    ## of files
    def __init__(self):
        self.database = shelve.open("database/db.dat", writeback=True)

    def createData(self, filename: str):
        if filename is None:
            return False
        
        if self.exist(filename):
            self.update(filename)
            return False

        fileID = str( uuid.uuid4() )
        fileName = filename
        timestamp = datetime.now()
        fixedData = {
            "id": str(fileID),
            "fileName": fileName,
            "lastModified": str(timestamp)
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
                self.database[i]["lastModified"] = str(timestamp)
                break

    def getData(self, filename: str):
        pass
    
    def deleteData(self, filename: str):
        pass

    def getAll(self):
        ret = [ self.database[i] for i in self.database.keys() ]
        return ret

if __name__ == "__main__":
    x = FileDBHandler()
    x.createData("haha.txt")
    print(x.getAll())
    time.sleep(5)
    x.createData("haha.txt")
    print(x.getAll())
