# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse,redirect
from django.conf.urls.static import static
import os
from django.core.files.storage import FileSystemStorage
from django.utils.crypto import get_random_string
import time
from django.http import JsonResponse
# Create your views here.



from django.conf import settings
import sys
'''
import clr

from System import *
from System.Drawing import Point
from System.Collections import *
from System.Collections.Generic import *
'''
from django.conf import settings

import os

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

#clr.AddReference(os.path.join(PROJECT_ROOT, 'dll/KidneySegmentation.dll'))

#from KidneySegmentation import InitializeSegmentation, Segmentation

'''
def testdddl(request):
    ID = String("ID")
    RootPath = String("RootPath")
    referance = 5
    data = [String("Path1"), String("Path2"), String("Path3")]
    KidneyPoints = [Point(1, 1), Point(2, 1), Point(1, 3)]
    ROIPoints = [Point(1, 1), Point(2, 1), Point(1, 3)]
    CortexPoints = [KidneyPoints, ROIPoints]
    width = 256
    height = 256
    XScaler = 1
    YScaler = 1
    path = String(os.path.join(PROJECT_ROOT, 'AC-003'))
    print path
    init = InitializeSegmentation.LoadState(path)

    if init is not None:
        seg = Segmentation.KidneySegmentation(init, os.path.join(PROJECT_ROOT,'FFD_Registeration'))
    else:
        print 'nulll'

    print settings.MEDIA_ROOT

    return HttpResponse("Hello, world. You're at the polls index.")

'''
def Home(request):
    context={}
    print 'asd'
    return render(request,'kideny/home.html',context)

def Load(request):
    context={}
    request.session['uploaded_file_url']=''
    request.session['ImagFoldar']=''

    if request.method == 'POST': #and request.FILES['myfile']:
        # create diroctry for each user
        unique_id = get_random_string(length=32)
        # loop on files and upload it
        index=0
        count=len(request.FILES.getlist('myfile'))
        for img in request.FILES.getlist('myfile'):
            index+=1
            fs =  FileSystemStorage(
                location=settings.MEDIA_ROOT+'\\'+unique_id
                    )
            filename = fs.save(img.name, img)
            '''
            time.sleep(.5)
            return render(request, 'kideny/Load.html', {
                'Count': count,
                'Done':index,
            })'''
        request.session['ImagFoldar'] =unique_id
        request.session['uploaded_file_url'] = str(index) + ' Slices have been uploaded '
        context['uploaded_file_url'] = str(index) + ' Slices have been uploaded Now you can intialize'
        return render(request, 'kideny/Load.html', context)
    else :
        context['uploaded_file_url']=''

    return render(request, 'kideny/Load.html',context)

def Initialization(request):
    context={}
    #get user slices
    if request.session['ImagFoldar']:
        fs = FileSystemStorage(
            location=settings.MEDIA_ROOT + '\\' + request.session['ImagFoldar']
        )
        Slices=fs.listdir(settings.MEDIA_ROOT + '\\' + request.session['ImagFoldar'])
        context['Slices']=Slices[1]
        context['media_root']= settings.MEDIA_ROOT
        context['media_url']=settings.MEDIA_URL

    return render(request, 'kideny/Initialization.html',context)

def SelectRef(request,refnumber,path):
    context = {}
    request.session['SelectRef'] = refnumber.split('/')[0]
    request.session['Selectedimgpath'] = path
    data = {
        'data': refnumber,
        'status':'Done'
    }
    return JsonResponse(data)

