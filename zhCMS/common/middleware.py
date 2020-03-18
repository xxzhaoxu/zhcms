from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect

try:

    from django.utils.deprecation import MiddlewareMixin  # Django 1.10.x
except ImportError:
    MiddlewareMixin = object  # Django 1.4.x - Django 1.9.x


def process_request(request):
    print('process_request')
    pass


class SimpleMiddleware(MiddlewareMixin):
    print('SimpleMiddleware')
    pass
