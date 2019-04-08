from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
def getall(request):
    return JsonResponse({ 'success': False, 'data': 'Nothing'})