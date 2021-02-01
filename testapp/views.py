from django.shortcuts import render
from django.views.generic import View
from .models import Employee
import json
from django.http import HttpResponse
from django.core.serializers import serialize
from .mixins import SerializeMixin,HttpResponseMixin

# Create your views here.
class EmployeeDetailCBV(View,HttpResponseMixin):
    def get(self,request,id,*args,**kwargs):
        try:

            emp =  Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            json_data = json.dumps({'msg':'Employee not found'})
            return self.render_http_response(json_data,status=404)
        else:
            json_data = serialize('json',[emp],fields=('eno','ename','eaddr'))
            return self.render_http_response(json_data)
        # emp_data = {
        # "ename":emp.ename,
        # "eno":emp.eno,
        # "eaddr":emp.eaddr,
        # "esal":emp.esal}
        # json_data = json.dumps(emp_data)



        #return HttpResponse(json_data,content_type='Application/json')


class AllEmployeeDetailCBV(SerializeMixin,View):
    def get(self,request,*args,**kwargs):
        qs =  Employee.objects.all()
        # emp_data = {
        # "ename":emp.ename,
        # "eno":emp.eno,
        # "eaddr":emp.eaddr,
        # "esal":emp.esal}
        # json_data = json.dumps(emp_data)
        #json_data = serialize('json',qs,fields=('eno','ename','eaddr'))
        #to remove additional fields from json_data output
        #final_data=[]
        # pdict = json.loads(json_data)
        # for obj in pdict:
        #     emp =  obj['fields']
        #     final_data.append(emp)
        # trimmed_json_data = json.dumps(final_data)

        #above functionality  we have now inckuded in SerializeMixin class
        trimmed_json_data=self.serializer(qs)

        return HttpResponse(trimmed_json_data,content_type='Application/json')
