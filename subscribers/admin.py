from django.contrib import admin
from .models import *
# Register your models here.



class SubscriberAdmin(admin.ModelAdmin):
    list_display = ["name", "email"]

    class Meta:
        model = Subscriber


admin.site.register(Subscriber,SubscriberAdmin)