




from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from .views import (
     landing
)# vse good HZ HULI VUYOB


urlpatterns = [

    url(r'^new/', landing),

]