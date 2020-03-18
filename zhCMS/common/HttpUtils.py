from django.http import HttpResponse


class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(data, **kwargs)
