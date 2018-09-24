# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse,redirect
from django.conf.urls.static import static
from Kidenydashboard import  settings

import os
from django.core.files.storage import FileSystemStorage
# Create your views here.


def Load(request):
    context={}
    if request.method == 'POST': #and request.FILES['myfile']:
    # create diroctry for each user
    # loop on files and upload it 
        for img in request.FILES.getlist('myfile'):
            fs =  FileSystemStorage(
    location=settings.MEDIA_URL+'a'

)
            filename = fs.save(img.name, img)
            print img.name
        return render(request, 'kideny/Load.html', {
            'uploaded_file_url': 'Done'
        })

    return render(request, 'kideny/Load.html')

def Home(request):
    context={}
    print '++++ Ho ++++++++++'
    return render(request,'kideny/home.html',context)

