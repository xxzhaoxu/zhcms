# from django.shortcuts import render, redirect, HttpResponseRedirect
from zhCMS.common.HttpUtils import JSONResponse
import django_redis
from zhCMS.common.ResultUtils import fail
from zhCMS.common.AESUtils import decrypt_oralce, encrypt_oracle
import re

try:
    from django.utils.deprecation import MiddlewareMixin  # Django 1.10.x
except ImportError:
    MiddlewareMixin = object  # Django 1.4.x - Django 1.9.x


class SimpleMiddleware(MiddlewareMixin):
    def process_request(self, request):
        path = request.path
        if '/login' == path or '/' == path or re.match(r'^/find', path) is not None:
            pass
        else:
            token = request.META.get("HTTP_TOKEN")
            try:
                conn = django_redis.get_redis_connection()
                dec = decrypt_oralce(token)
                redis_token = conn.get(dec.split('_')[0])
                if str(redis_token, 'utf-8') == token:
                    conn.set(dec.split('_')[0], token, 30 * 60)
                    pass
                else:
                    return JSONResponse(fail(401, '用户验证失败，请重新登录'))
            except:
                return JSONResponse(fail(401, '用户验证失败，请重新登录'))

