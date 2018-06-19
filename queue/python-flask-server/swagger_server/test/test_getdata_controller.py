# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.data1 import Data1  # noqa: E501
from swagger_server.models.inline_response20012 import InlineResponse20012  # noqa: E501
from swagger_server.models.inline_response500 import InlineResponse500  # noqa: E501
from swagger_server.test import BaseTestCase


class TestGetdataController(BaseTestCase):
    """GetdataController integration test stubs"""

    def test_get_data(self):
        """Test case for get_data

        get data
        """
        data = Data1()
        response = self.client.open(
            '/v1/get_data',
            method='POST',
            data=json.dumps(data),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_data_all(self):
        """Test case for get_data_all

        get data all
        """
        data = Data1()
        response = self.client.open(
            '/v1/get_data_all',
            method='POST',
            data=json.dumps(data),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
