# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse,redirect
from django.conf.urls.static import static
from Kidenydashboard import  settings

import os
from django.core.files.storage import FileSystemStorage
from django.utils.crypto import get_random_string
import time
from django.http import JsonResponse
# Create your views here.



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

def SelectRef(request,refnumber):
    context = {}
    request.session['SelectRef'] = refnumber
    data = {
        'data': refnumber,
        'status':'Done'
    }
    return JsonResponse(data)