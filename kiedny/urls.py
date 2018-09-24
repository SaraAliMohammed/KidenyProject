from django.conf.urls import url,include
from views import Load , Home
urlpatterns = [
    url(r'^$', Home,name='Home'),
    url(r'^Load$',Load,name='Load'),
    url(r'^Load$',Load,name='Load'),


]
