from django.conf.urls import url,include
from views import Home,Load
urlpatterns = [
    url(r'', Home),
    url(r'^load/',Load),

]
