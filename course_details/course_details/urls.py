from django.contrib import admin

from django.conf.urls import url
from django.conf.urls import include
from django.urls import path

urlpatterns = [
    path('course/', include('course.urls')),
    path('admin/', admin.site.urls),
]