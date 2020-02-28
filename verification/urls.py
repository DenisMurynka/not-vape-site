













from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from .views import (
    sent_mail,checked
)# vse good HZ HULI VUYOB


urlpatterns = [

    url(r'^sent/', sent_mail),
    path('checked/', checked, name='checked'),

]