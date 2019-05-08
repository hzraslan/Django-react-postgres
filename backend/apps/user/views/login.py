from __future__ import unicode_literals
from ..models import *
from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from django.core import serializers
import json
import jwt
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import datetime
@csrf_exempt
def login(request):
    data = json.loads(request.body.decode('utf-8'))
    password = data['password']
    email = data['email']
    user = authenticate(request, email=email, password=password)
    if user: 
        token = jwt.encode({'username': user.email}, 'secreta',  algorithm='HS256')
        return HttpResponse(json.dumps({'token':str(token), 'success': True}), content_type='application/json')
    else:
        return HttpResponse(json.dumps({'success': False}), content_type='application/json')