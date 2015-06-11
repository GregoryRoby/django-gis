from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def index(request):
  return HttpResponse("Filler Page for Login")

def MainMap(request):
  return HttpResponse("Filler Page for Main Map Page")
  
