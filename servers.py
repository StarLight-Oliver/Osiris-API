
import os
import json

serverList = {}

class Server():
    def __init__(self, id, name, ip, dbInfo):
        self.id = id
        self.name = name
        self.ip = ip
        self.dbInfo = dbInfo
    def GetStatus(self):
        return True
    def GetName(self):
        return self.name
    def GetID(self):
        return self.id
    def GetIP(self):
        return self.ip
    def Update(self, name, ip, dbInfo):
        self.name = name
        self.ip = ip
        self.dbInfo = dbInfo

def ReadServers():
    for filename in os.listdir("./servers"):
        filePath = os.path.join("./servers", filename)
        with open(filePath) as f:
            serverJson = f.read()
            serverDict = json.loads(serverJson)
            AddServer(serverDict["id"], serverDict["name"], serverDict["ip"], serverDict["dbInfo"])

def AddServer(id, name, ip, dbInfo):
    if id in serverList:
        return False, "ID Already exists"
    else:
        serverList[id] = Server(id, name, ip, dbInfo)

def UpdateServer(id, name, ip, dbInfo):

    if id in serverList:
        serverList[id].Update(name, ip, dbInfo)
    else:
        return False, "ID not in List"

def GetAll():
    if len(serverList) == 0:
        ReadServers()
    return serverList
