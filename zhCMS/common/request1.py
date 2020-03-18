def post(param):
    from django.http import HttpRequest
    print(param)
    return HttpRequest.POST.get(param)
