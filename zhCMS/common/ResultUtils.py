import json
from zhCMS.common.AESUtils import encrypt_oracle
from django.core import serializers
import django_redis


def success(*obj):
    token = ''
    if len(obj) == 2:
        token = obj[1]
    try:
        re = json.dumps({'code': 200, 'data': obj[0], 'msg': 'ok', 'token': token})
        return re
    except:
        re = json.dumps(
            {'code': 200, 'data': json.loads(serializers.serialize("json", obj[0])), 'msg': 'ok', 'token': token})
        return re


def fail(code, msg):
    return json.dumps({'code': code, 'data': 'fail', 'msg': msg, 'token': ''})


'''
total_num 总条数
pag_num 总页数
curuent_page_num 前页数
curuent_page 当前页的数据
'''


def page_handler(total_num, pag_num, page_index, list):
    data = {
        'total_num': total_num,
        'pag_num': pag_num,
        'page_index': page_index,
        'list': json.loads(serializers.serialize("json", list))
    }
    return success(data)
