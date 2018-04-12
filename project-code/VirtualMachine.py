# -*- coding: utf-8 -*-
import util

class VirtualMachine(object):
    DEFAULT_SIZE_ID = util.getAWSDefSize()
    DEFAULT_REGION = util.getAWSDefRegion()
    DEFAULT_AMI = util.getAWSDefAMI()

    def __init__(self, name, size, image, region, status):
        self.name = name
        self.status = status
        
        if (size == ""):
            self.size = VirtualMachine.DEFAULT_SIZE_ID
        else:
            self.size = size
        
        if (image == ""):
            self.image = VirtualMachine.DEFAULT_AMI
        else:
            self.image = image
        
        if (region == ""):
            self.region = VirtualMachine.DEFAULT_REGION
        else:
            self.region = region
