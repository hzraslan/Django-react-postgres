from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
def main(request):
    return HttpResponse("You're voting on question %s." %1)