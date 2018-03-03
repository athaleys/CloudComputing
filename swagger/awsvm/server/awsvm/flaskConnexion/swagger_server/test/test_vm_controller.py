# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.vm import VM  # noqa: E501
from swagger_server.test import BaseTestCase


class TestVmController(BaseTestCase):
    """VmController integration test stubs"""

    def test_create_vm(self):
        """Test case for create_vm

        create a new vm
        """
        body = VM()
        response = self.client.open(
            '/aws/vm',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_vm_by_id(self):
        """Test case for get_vm_by_id

        Find vm by ID
        """
        response = self.client.open(
            '/aws/vms/{vmId}'.format(vmId=789),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
