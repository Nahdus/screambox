from django.conf.urls import url
from . import views

app_name = 'home'

urlpatterns = [
    #ip-add
    url(r'^$', views.home, name="home"),
    #ip-add/screams
    url(r'^screams$', views.screams, name="screams" ),
    
    
]
