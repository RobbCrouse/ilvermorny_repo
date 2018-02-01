# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, redirect
import random
from models import *
from forms import RegForm

# Create your views here.
def new(request):

    num = random.randint(3,11)
    context = {
        'num': num,
        'form' : RegForm()
    }

    print "yo"
    return render(request, 'houses/new.html', context)

def create(request):
    print "let's create"
    
    errors = Student.objects.basic_validator(request.POST)
    
    if len(errors) == 0:
        print "form was valid"

        #request.session['peep'] = 'Roberto'
        return redirect("/students")

    else:
        for error in errors:
            messages.error(request, errors[error])

        return redirect('/')
         



def index(request):
    context = {
        'thunderbirds': Student.objects.filter(cult__name='Thunderbird'),
        'wampii': Student.objects.filter(cult__name='Wanpus'),
        'snakes': House.objects.get(name='Horned Serpent').peeps.all(),
        'puks': House.objects.get(name='Pukwudgie').peeps.all()

    }
    return render(request, 'houses/index.html', context)

def show(request, info):
    print info
    return