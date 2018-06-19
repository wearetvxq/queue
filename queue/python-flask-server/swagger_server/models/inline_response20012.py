# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.inline_response20021 import InlineResponse20021  # noqa: F401,E501
from swagger_server import util


class InlineResponse20012(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, code: str=None, msg: str=None, use_time: int=None, data: List[InlineResponse20021]=None):  # noqa: E501
        """InlineResponse20012 - a model defined in Swagger

        :param code: The code of this InlineResponse20012.  # noqa: E501
        :type code: str
        :param msg: The msg of this InlineResponse20012.  # noqa: E501
        :type msg: str
        :param use_time: The use_time of this InlineResponse20012.  # noqa: E501
        :type use_time: int
        :param data: The data of this InlineResponse20012.  # noqa: E501
        :type data: List[InlineResponse20021]
        """
        self.swagger_types = {
            'code': str,
            'msg': str,
            'use_time': int,
            'data': List[InlineResponse20021]
        }

        self.attribute_map = {
            'code': 'code',
            'msg': 'msg',
            'use_time': 'use_time',
            'data': 'data'
        }

        self._code = code
        self._msg = msg
        self._use_time = use_time
        self._data = data

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse20012':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_200_1_2 of this InlineResponse20012.  # noqa: E501
        :rtype: InlineResponse20012
        """
        return util.deserialize_model(dikt, cls)

    @property
    def code(self) -> str:
        """Gets the code of this InlineResponse20012.

        status_code  # noqa: E501

        :return: The code of this InlineResponse20012.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code: str):
        """Sets the code of this InlineResponse20012.

        status_code  # noqa: E501

        :param code: The code of this InlineResponse20012.
        :type code: str
        """

        self._code = code

    @property
    def msg(self) -> str:
        """Gets the msg of this InlineResponse20012.

        the msg of return  # noqa: E501

        :return: The msg of this InlineResponse20012.
        :rtype: str
        """
        return self._msg

    @msg.setter
    def msg(self, msg: str):
        """Sets the msg of this InlineResponse20012.

        the msg of return  # noqa: E501

        :param msg: The msg of this InlineResponse20012.
        :type msg: str
        """

        self._msg = msg

    @property
    def use_time(self) -> int:
        """Gets the use_time of this InlineResponse20012.

        the cost of time  # noqa: E501

        :return: The use_time of this InlineResponse20012.
        :rtype: int
        """
        return self._use_time

    @use_time.setter
    def use_time(self, use_time: int):
        """Sets the use_time of this InlineResponse20012.

        the cost of time  # noqa: E501

        :param use_time: The use_time of this InlineResponse20012.
        :type use_time: int
        """

        self._use_time = use_time

    @property
    def data(self) -> List[InlineResponse20021]:
        """Gets the data of this InlineResponse20012.

        the list of data  # noqa: E501

        :return: The data of this InlineResponse20012.
        :rtype: List[InlineResponse20021]
        """
        return self._data

    @data.setter
    def data(self, data: List[InlineResponse20021]):
        """Sets the data of this InlineResponse20012.

        the list of data  # noqa: E501

        :param data: The data of this InlineResponse20012.
        :type data: List[InlineResponse20021]
        """

        self._data = data