from __future__ import unicode_literals
from ..models import *
from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from django.core import serializers
import json
from jose import jws
from django.http import HttpResponse
import datetime
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    email = request.POST['email']
    user = authenticate(username=username, password=password)
    print(user)
    if user: 
        expiry = datetime.date.today() + timedelta(days=50)
        token = jws.sign({'username': user.username, 'expiry':expiry}, 'seKre8',  algorithm='HS256')
        return HttpResponse(json.dumps({'token':token}), content_type='application/json')
    else:
        return HttpResponse(json.dumps({'success': False}), content_type='application/json')