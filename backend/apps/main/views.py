from __future__ import unicode_literals
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
import json
from django.core import serializers

@csrf_exempt
def index(request):
    user = authenticate(request)
    data = serializers.serialize('json', [User.objects.get(id=user.id)], ensure_ascii=False)[1:-1]
    if not user:
        return HttpResponse(json.dumps({'success': True}), content_type='application/json')
    return HttpResponse(json.dumps({'success': True, 'data': data }), content_type='application/json')