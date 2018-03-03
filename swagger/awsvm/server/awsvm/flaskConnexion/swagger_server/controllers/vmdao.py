import pymongo
from pymongo import MongoClient
import pprint
#from swagger_server.models.vm import VM

MONGO_URL = "mongodb://localhost:27017/"
MONGO_DATABASE = "virtual_machine"
MONGO_COLLECTION = "vm"

client = MongoClient(MONGO_URL)
db = client[MONGO_DATABASE]
vmCollection = db[MONGO_COLLECTION]

pprint.pprint(vmCollection.find_one())

def getAllVMS():
    vms = []
    for vmInst in vmCollection.find():
        """
        vm = VM(vm_id=vmInst['vmId'],
                name=result['name'],
                image=result['image'],
                location=result['location'],
                ram_size=result['ramSize'],
                disk_size=result['diskSize'],
                status=result['status']
                )
                """
        vms.append(vmInst)

    return vms

print(getAllVMS())

def getVMbyID(vmId):
    return vmCollection.find_one({"vmId": vmId})

print("get by id - ", getVMbyID(2))

def insertVM(vm):
    vmID = vmCollection.insert_one(vm).inserted_id
    return vmID

vm = {
   "vmId": 1,
   "name": 'aws vm 2',
   "image": 'windows 10',
   "location": 'US',
   "ramSize": 3048,
   "diskSize": 30720,
   "status": 'STOPPED'
}

#print ("create vm - ", insertVM(vm))