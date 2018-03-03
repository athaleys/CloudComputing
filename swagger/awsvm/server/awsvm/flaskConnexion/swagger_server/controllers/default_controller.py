import connexion
import six

from swagger_server.models.vm import VM  # noqa: E501
from swagger_server import util

import vmdao


def vms_get():  # noqa: E501
    """vms_get

    Returns list on VMs # noqa: E501


    :rtype: List[VM]
    """
    vms = []
    for vmInst in vmdao.getAllVMS():
        vm = VM(vm_id=vmInst['vmId'],
                name=vmInst['name'],
                image=vmInst['image'],
                location=vmInst['location'],
                ram_size=vmInst['ramSize'],
                disk_size=vmInst['diskSize'],
                status=vmInst['status']
                )
        vms.append(vm)

    return vms
