from django.http import HttpResponse

class HttpResponseMixin(object):
    def render_to_http_responce(self,json_Data):
        return HttpResponse(json_Data,content_type = 'application/json')
