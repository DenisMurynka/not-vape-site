




from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from .views import (
    liqpay_callback
)


urlpatterns = [

    url(r'^pay/', liqpay_callback),

]