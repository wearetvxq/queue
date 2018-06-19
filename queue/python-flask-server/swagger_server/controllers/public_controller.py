import connexion
import six,time,json
from swagger_server.controllers.public import *
from flask import Flask, request
from swagger_server.controllers.RedisQueue import *
from swagger_server.models.inline_response2001 import InlineResponse2001  # noqa: E501
from swagger_server.models.inline_response20011 import InlineResponse20011  # noqa: E501
from swagger_server.models.inline_response500 import InlineResponse500  # noqa: E501
from swagger_server import util


def delete_queue(data):  # noqa: E501
    """delete queue

    删除指定队列 # noqa: E501

    :param name: 消息队列名
    :type name: str

    :rtype: InlineResponse2001
    """

    try:
        start_time = time.time()
        if connexion.request.is_json:
            data = connexion.request.get_json()
        name = data['name']
        q = RedisQueue(name)
        q.Rdel_all()
        end_time = time.time()
        use_time = end_time - start_time
        msg={
            'code':'0',
            "msg": "success",
            'use_time': use_time,
        }
        return msg
    except:
        msg={
            "code": -1, "msg": "Error"
        }
        return msg


def scan():  # noqa: E501
    """scan

    查看当前队列信息 # noqa: E501


    :rtype: InlineResponse20011
    """
    try:
        start_time = time.time()
        q=RedisQueue('default')
        data=q.scan()
        end_time = time.time()
        use_time = end_time - start_time
        msg = {
            'code':0,
            "msg": "success",
            'data':data,
            'use_time': use_time,
        }
        return msg
    except:
        msg = {
            "code": -1, "msg": "Error"
        }
        return msg
