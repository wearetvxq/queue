# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.data import Data  # noqa: E501
from swagger_server.models.inline_response2001 import InlineResponse2001  # noqa: E501
from swagger_server.models.inline_response500 import InlineResponse500  # noqa: E501
from swagger_server.test import BaseTestCase


class TestPostdataController(BaseTestCase):
    """PostdataController integration test stubs"""

    def test_post_data(self):
        """Test case for post_data

        post data
        """
        data = Data()
        response = self.client.open(
            '/v1/post_data',
            method='POST',
            data=json.dumps(data),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
