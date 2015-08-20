#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
	return render(request, 'home.html')

def index(request):
    return HttpResponse(u"Hello World")
# Create your views here.

def add(request):
	a = request.GET['a']
	b = request.GET['b']
	c = int(a) + int(b)
	return HttpResponse(str(c))

def add2(request, a, b):
	c = int(a) + int(b)
	return HttpResponse(str(c))
