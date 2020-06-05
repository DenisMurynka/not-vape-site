













from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from .views import (
    sent_mail,checked
)#it is only UI issue,move on


urlpatterns = [

    url(r'^sent/', sent_mail),
    path('checked/', checked, name='checked'),

]
