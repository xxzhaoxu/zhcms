import json

from django.core import serializers


def success(obj):
    try:
        return json.dumps({'code': 200, 'data': obj, 'msg': 'ok', 'token': ''})
    except:
        return json.dumps(
            {'code': 200, 'data': json.loads(serializers.serialize("json", obj)), 'msg': 'ok', 'token': ''})


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
