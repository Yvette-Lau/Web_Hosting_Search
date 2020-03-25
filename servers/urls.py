from django.urls import re_path,path
from django.conf.urls import url
from . import views


urlpatterns = [
    path('index/', views.index, name='index'),
    re_path(r'^serverInfo/', views.serverInfo, name='serverInfo'),

]

