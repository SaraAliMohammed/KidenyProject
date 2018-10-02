from django.conf.urls import url,include
from views import Load , Home,Initialization,SelectRef#,testdddl
urlpatterns = [
    url(r'^$', Home,name='Home'),
    url(r'^Load$',Load,name='Load'),
    url(r'^Initialization$',Initialization,name='Initialization'),
    url(r'^SelectRef/(?P<refnumber>[0-9]/(?P<path>[\w\d@\.-]+))',SelectRef,name='SelectRef'),
#url(r'^testdddl$',testdddl,name='testdddl'),



]
