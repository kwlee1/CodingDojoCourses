# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import Courses

# Create your views here.
def index(request):
    context = {
        "courses": Courses.objects.all(), 
        "errors": request.session['errors']
    }
    return render(request, 'courses_app/index.html', context)

def create(request):
    if 'errors' not in request.session:
        request.session['errors'] = []
    request.session['errors'] = Courses.objects.namelen(request.POST)
    if request.session['errors']['name'] == "" and request.session['errors']['desc'] == "": 
        Courses.objects.create(name=request.POST['name'],desc=request.POST['desc'])
    else: 
        print "does it work? "
    print request.session['errors']['name']
    print request.session['errors']['desc']
    return redirect('/')

def destroy(request,id):
    context = {
        "course": Courses.objects.get(id=id)
    }
    return render(request, 'courses_app/destroy.html', context)

def delete(request,id):
    Courses.objects.get(id=id).delete()
    return redirect('/')