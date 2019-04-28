from __future__ import unicode_literals
from ..models import *
from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
import bcrypt
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers

@csrf_exempt
def registration(request):
    if request.method == "POST":
        if request.POST['password'] and \
           request.POST['password'] == request.POST['confirm_password'] and \
           request.POST["name"] and \
           request.POST['username'] and \
           request.POST['email'] :
            hash1 = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
            user_new = User.objects.create(name=request.POST['name'], username=request.POST['username'], password=hash1, email=request.POST['email'])
            return JsonResponse({'success': True, 'data': user_new.id})
    return JsonResponse({ 'success': False, 'data': 'Nothing'})