from __future__ import unicode_literals
from ..models import *
from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from django.core import serializers
import json
from jose import jws
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
@csrf_exempt
def login(request):
    # User.objects.all().delete()
    # data = serializers.serialize('json', User.objects.all(), ensure_ascii=False)
    # return HttpResponse(data, content_type="application/json")
    username = request.POST['username']
    password = request.POST['password']
    email = request.POST['email']
    user = authenticate(request, email=email, password=password)
    if user: 
        token = jws.sign({'username': user.email}, 'pythonforum',  algorithm='HS256')
        print(token)
        return HttpResponse(json.dumps({'token':token, 'success': True}), content_type='application/json')
    else:
        return HttpResponse(json.dumps({'success': False}), content_type='application/json')