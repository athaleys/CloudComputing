import connexion
import six

from swagger_server.models.vm import VM  # noqa: E501
from swagger_server import util

import json

import vmdao


def create_vm(body):  # noqa: E501
    """create a new vm

     # noqa: E501

    :param body: VM object that needs to be added
    :type body: dict | bytes

    :rtype: None
    """

    if connexion.request.is_json:
        body = VM.from_dict(connexion.request.get_json())  # noqa: E501

    vm = {
        "vmId": body.vm_id,
        "name": body.name,
        "image": body.image,
        "location": body.location,
        "ramSize": body.ram_size,
        "diskSize": body.disk_size,
        "status": body.status
        }


    vmid = vmdao.insertVM(vm)
    return "vm created"


def get_vm_by_id(vmId):  # noqa: E501
    """Find vm by ID

    Returns a single vm # noqa: E501

    :param vmId: ID of VM to return
    :type vmId: int

    :rtype: VM
    """
    vmInst = vmdao.getVMbyID(vmId)
    vm = VM(vm_id=vmInst['vmId'],
            name=vmInst['name'],
            image=vmInst['image'],
            location=vmInst['location'],
            ram_size=vmInst['ramSize'],
            disk_size=vmInst['diskSize'],
            status=vmInst['status']
            )

    return vm
