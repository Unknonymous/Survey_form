# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    if 'count' not in request.session:
        request.session['count'] = 0
    return render( request, 'surfo/index.html')

def result(request):
    return render ( request, 'surfo/result.html')

def process(request):
    request.session['count'] += 1
    request.session['name'] = request.POST['name']
    if not request.session['name']:
        request.session['name'] = 'none'
    request.session['where'] = request.POST['where']
    request.session['what'] = request.POST['what']
    request.session['comment'] = request.POST['comments']
    return redirect ( '/result')

def back(request):
    #request.session['count'] = 0
    return redirect ('/')