from __future__ import print_function

from django.shortcuts import render
from django.contrib import auth

def home(request):
    return render(request, 'index.html', {})
