

from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
    #ip-add
    url(r'^', include('home.urls')),
    #ip-add/admin/
    url(r'^admin/', admin.site.urls),

        ]
