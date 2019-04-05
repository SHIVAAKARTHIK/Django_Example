from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def emp_date_view(request):
    emp_date = {
    'eno':100,
    'ename':'Sunny',
    'esal':1000,
    'eadd':'Mumbai',
    }

    resp = '<h1>Emp No:{}<br> Emp Name:{} <br> Emp Sal:{} <br> Emp Add:{}</h1>'.format(emp_date['eno'],emp_date['ename'],emp_date['esal'],emp_date['eadd'])
    return HttpResponse(resp)

import json
def emp_date_jsonview(request):
    emp_date = {
    'eno':100,
    'ename':'Sunny',
    'esal':1000,
    'eadd':'Mumbai',
    }
    json_data = json.dumps(emp_date)
    return HttpResponse(json_data,content_type = 'application/json')

from django.http import JsonResponse
def emp_date_jsonview2(request):
    emp_date = {
    'eno':100,
    'ename':'Sunny',
    'esal':1000,
    'eadd':'Mumbai',
    }
    return JsonResponse(emp_date)

from django.views.generic import View
from testapp.mixin import HttpResponseMixin
class JsonCBV(HttpResponseMixin,View):
    def get(self,request,*args,**kwargs):
        json_Data = json.dumps({'msg':'This is from get request'})
        return self.render_to_http_responce(json_Data)
    def post(self,request,*args,**kwargs):
        json_Data = json.dumps({'msg':'This is from post request'})
        return self.render_to_http_responce(json_Data)
    def put(self,request,*args,**kwargs):
        json_Data = json.dumps({'msg':'This is from put request'})
        return self.render_to_http_responce(json_Data)
    def delete(self,request,*args,**kwargs):
        json_Data = json.dumps({'msg':'This is from delete request'})
        return self.render_to_http_responce(json_Data)
