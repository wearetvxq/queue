# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class InlineResponse20021(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, switchtype: str=None, line: str=None, station: str=None, eletype: str=None, swtichstatus: str=None):  # noqa: E501
        """InlineResponse20021 - a model defined in Swagger

        :param switchtype: The switchtype of this InlineResponse20021.  # noqa: E501
        :type switchtype: str
        :param line: The line of this InlineResponse20021.  # noqa: E501
        :type line: str
        :param station: The station of this InlineResponse20021.  # noqa: E501
        :type station: str
        :param eletype: The eletype of this InlineResponse20021.  # noqa: E501
        :type eletype: str
        :param swtichstatus: The swtichstatus of this InlineResponse20021.  # noqa: E501
        :type swtichstatus: str
        """
        self.swagger_types = {
            'switchtype': str,
            'line': str,
            'station': str,
            'eletype': str,
            'swtichstatus': str
        }

        self.attribute_map = {
            'switchtype': 'switchtype',
            'line': 'line',
            'station': 'station',
            'eletype': 'eletype',
            'swtichstatus': 'swtichstatus'
        }

        self._switchtype = switchtype
        self._line = line
        self._station = station
        self._eletype = eletype
        self._swtichstatus = swtichstatus

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse20021':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_200_2_1 of this InlineResponse20021.  # noqa: E501
        :rtype: InlineResponse20021
        """
        return util.deserialize_model(dikt, cls)

    @property
    def switchtype(self) -> str:
        """Gets the switchtype of this InlineResponse20021.

        the tyoe of switch  # noqa: E501

        :return: The switchtype of this InlineResponse20021.
        :rtype: str
        """
        return self._switchtype

    @switchtype.setter
    def switchtype(self, switchtype: str):
        """Sets the switchtype of this InlineResponse20021.

        the tyoe of switch  # noqa: E501

        :param switchtype: The switchtype of this InlineResponse20021.
        :type switchtype: str
        """

        self._switchtype = switchtype

    @property
    def line(self) -> str:
        """Gets the line of this InlineResponse20021.

        the name of line  # noqa: E501

        :return: The line of this InlineResponse20021.
        :rtype: str
        """
        return self._line

    @line.setter
    def line(self, line: str):
        """Sets the line of this InlineResponse20021.

        the name of line  # noqa: E501

        :param line: The line of this InlineResponse20021.
        :type line: str
        """

        self._line = line

    @property
    def station(self) -> str:
        """Gets the station of this InlineResponse20021.

        the information of station  # noqa: E501

        :return: The station of this InlineResponse20021.
        :rtype: str
        """
        return self._station

    @station.setter
    def station(self, station: str):
        """Sets the station of this InlineResponse20021.

        the information of station  # noqa: E501

        :param station: The station of this InlineResponse20021.
        :type station: str
        """

        self._station = station

    @property
    def eletype(self) -> str:
        """Gets the eletype of this InlineResponse20021.

        the information of station  # noqa: E501

        :return: The eletype of this InlineResponse20021.
        :rtype: str
        """
        return self._eletype

    @eletype.setter
    def eletype(self, eletype: str):
        """Sets the eletype of this InlineResponse20021.

        the information of station  # noqa: E501

        :param eletype: The eletype of this InlineResponse20021.
        :type eletype: str
        """

        self._eletype = eletype

    @property
    def swtichstatus(self) -> str:
        """Gets the swtichstatus of this InlineResponse20021.

        the status of station  # noqa: E501

        :return: The swtichstatus of this InlineResponse20021.
        :rtype: str
        """
        return self._swtichstatus

    @swtichstatus.setter
    def swtichstatus(self, swtichstatus: str):
        """Sets the swtichstatus of this InlineResponse20021.

        the status of station  # noqa: E501

        :param swtichstatus: The swtichstatus of this InlineResponse20021.
        :type swtichstatus: str
        """

        self._swtichstatus = swtichstatus
