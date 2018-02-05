# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from django.shortcuts import redirect
# Create your views here.
def index(request):
	context = { }
	return render(request, 'home/main.html', context)

def about(request):
    context = {}
    return render(request,'home/about.html', context)

def services(request):
    context = {}
    return render(request,'home/services.html', context)

def contact(request):
    context = {}
    return render(request,'home/contacts.html', context)
def career(request):
    context = {}
    return render(request,'home/careers.html', context)

