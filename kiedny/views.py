# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse,redirect

from Kidenydashboard import  settings
import os
# Create your views here.
def Home(request):
    context={}
    print '==================='
    print settings.BASE_DIR
    print '==================='
    return render(request,'kideny/home.html',context)
