from django.core.serializers import serialize
import json
from django.http import HttpResponse

class SerializeMixin:
    def serializer(self,qs):
        json_data = serialize('json',qs,fields=('eno','ename','eaddr'))
        #to remove additional fields from json_data output
        final_data=[]
        pdict = json.loads(json_data)
        for obj in pdict:
            emp =  obj['fields']
            final_data.append(emp)
        trimmed_json_data = json.dumps(final_data)
        return trimmed_json_data

class HttpResponseMixin:
    def render_http_response(self, json_data,status=200):
        return HttpResponse(json_data,content_type='application/json',status=status)
