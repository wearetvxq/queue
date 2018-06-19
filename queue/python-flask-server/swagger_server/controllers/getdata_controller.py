import connexion
import six,time,json
from swagger_server.controllers.public import *
from flask import Flask, request
from swagger_server.controllers.RedisQueue import *
from swagger_server.models.inline_response20012 import InlineResponse20012  # noqa: E501
from swagger_server.models.inline_response500 import InlineResponse500  # noqa: E501
from swagger_server import util


def get_data(data):  # noqa: E501
    """get data

    取指定消息队列单条数据 # noqa: E501

    :param name: 消息队列名
    :type name: str

    :rtype: InlineResponse20012
    """
    try:
        start_time = time.time()
        if connexion.request.is_json:
            data = connexion.request.get_json()
        name = data['name']
        q = RedisQueue(name)
        end_time = time.time()
        use_time = end_time - start_time
        data=[eval(q.get().decode('utf-8'))]
        msg={
            "code": 0,
            "msg": "success",
            'data': data,
            'use_time': use_time,
        }
        return msg
    except:
        msg={
            "code": -1, "msg": "Error"
        }
        return msg


def get_data_all(data):  # noqa: E501
    """get data all

    取指定消息队列所有数据 # noqa: E501

    :param name: 消息队列名
    :type name: str

    :rtype: InlineResponse20012
    """
    try:
        start_time = time.time()
        if connexion.request.is_json:
            data = connexion.request.get_json()
        name = data['name']
        q = RedisQueue(name)
        end_time = time.time()
        data = q.get_all()
        use_time = end_time - start_time
        msg={
            'code':0,
            "msg": "success",
            'data': data,
            'use_time': use_time,
        }
        return msg
    except:
        msg={
            "code": -1, "msg": "Error"
        }
        return msg
