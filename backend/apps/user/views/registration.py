from __future__ import unicode_literals
from ..models import *
from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import json
@csrf_exempt
def registration(request):
    print(type(request.POST['password']))
    if request.method == "POST":
        if request.POST['password'] and \
           request.POST['password'] == request.POST['confirm_password'] and \
           request.POST["name"] and \
           request.POST['username'] and \
           request.POST['email'] :
            hash1 = make_password(request.POST['password'])
            user_new = User.objects.create(name=request.POST['name'], username=request.POST['username'], password=hash1, email=request.POST['email'])
            data = serializers.serialize('json', [User.objects.get(id=user_new.id)], ensure_ascii=False)[1:-1]
            return HttpResponse(json.dumps({'data':data, 'success': True}), content_type='application/json')
        return HttpResponse(json.dumps({'success': False}), content_type='application/json')