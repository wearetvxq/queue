import connexion
import six,time,json
from swagger_server.controllers.public import *
from flask import Flask, request
from swagger_server.controllers.RedisQueue import *
from swagger_server.models.inline_response2001 import InlineResponse2001  # noqa: E501
from swagger_server.models.inline_response500 import InlineResponse500  # noqa: E501
from swagger_server import util


def post_data(data):  # noqa: E501
    """post data

    传输数据/写入消息队列 # noqa: E501

    :param name: 消息队列名
    :type name: str
    :param lists: 数据
    :type lists: str
    :param priority: 优先级
    :type priority: str

    :rtype: InlineResponse2001
    """
    try:
        config=[0,1,2,3,4,5,6,7,8,8,8]
        start_time=time.time()
        if connexion.request.is_json:
            data = connexion.request.get_json()
        lists=eval(data['data'])
        priority=data['priority']
        name=data['name']
        q=RedisQueue(name)
        num=int(len(lists)/100000)
        if num==0:
            # 第一种方式 pipline
            q.lput(lists,priority)
            end_time=time.time()
            use_time=end_time-start_time
            msg={
                'code':0,
                "msg": "success",
                'use_time':use_time,
            }

            return msg
        if num>0:
            if num >=10:
                mun=10
            thread=config[num]
            thread_pool(q.lput,thread,lists,priority)
            end_time = time.time()
            use_time = end_time - start_time
            msg = {
                'code':0,
                "msg": "success",
                'use_time': use_time,
            }

            return msg
    except:
        msg={
            "code": -1, "msg": "Error"
        }
        return msg

