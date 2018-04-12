import connexion
import six

from swagger_server.models.awsvm import AWSVM  # noqa: E501
from swagger_server import util

import aws_ec2

def find_by_region(region):  # noqa: E501
    """find_by_region

    Returns list on VMs # noqa: E501

    :param region: region
    :type region: str

    :rtype: List[AWSVM]
    """
    vms = []
    if region == "":
        return "Please provide AWS EC2 region"
    else:
        nodes = aws_ec2.getVMByRegion(region)
        for node in nodes:
            awsvm = AWSVM( vm_id=node.id, 
                          name=node.name, 
                          image=node.image, 
                          region=region, 
                          size=node.size, 
                          status=node.state)
            vms.append(awsvm)
        return vms
