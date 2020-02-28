from django.shortcuts import render
from .forms import SubscribersForm
from django.utils.deprecation import MiddlewareMixin
#import Cookies
# Create your views here.
def landing(request):

    #csrftoken = Cookies.get('csrftoken');

    form= SubscribersForm(request.POST or None)
    #fname = request.POST.get('fname')
    if request.method == "POST" and form.is_valid():
        newForm = form.save()       #save data from fields


    return render(request,'landing/landing.html',locals())