from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout,authenticate 
from django.core.mail import send_mail
# Create your views here.
from django.contrib import messages
from .models import *
from .forms import Usercredentials
import requests


def loginusereegridintel(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)
        
        if user is not None and user.is_active:
            login(request,user)
            #return redirect('https://ee-plus.maps.arcgis.com/apps/opsdashboard/index.html#/76037806b1fc4f4792ceadda5a658347')
            return render(request,'registration/arcgispage.html')
        else:
            messages.info(request,"Username or Password is incorrect")
            

    return render(request,'registration/login.html')


def logoutuser(request):
    #logout(request)
    return redirect('/loginusercredentialseegridintel-8bd7ae92e39296d811adede9642bafbdd6942fbb0ce207971c7ff60764a2be87da365c5db6e70e9c53533f9deb')


def register(request):

    form = Usercredentials()
    username = request.POST.get('username')
    password = request.POST.get('password')
    if request.method == "POST":
        form = Usercredentials(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_active = False
            user.save()
            user = form.cleaned_data.get('username')
            requests.post(
            "https://api.mailgun.net/v3/sandbox37bb2de9a8914eaba41e4cc5c8c23856.mailgun.org/messages",
            auth=("api", "b04a3466176e5ddba49ca37d985ff0be-07bc7b05-af614be2"),
            data={"from": "Excited User <mailgun@sandbox37bb2de9a8914eaba41e4cc5c8c23856.mailgun.org>",
                "to": ["jk@eeplus.com"],
                "subject": "Message from EEGRIDINTEL OMT!",
                "text": "A new user registered to Outage mapping tool GIS platform.Please validate the permissions. Please see to the link attached https://eegridintel.herokuapp.com/admin/login/?next=/admin/"})
            messages.success(request,"Account for "+user+" will be activated soon")
            return redirect('/loginusercredentialseegridintel-8bd7ae92e39296d811adede9642bafbdd6942fbb0ce207971c7ff60764a2be87da365c5db6e70e9c53533f9deb')

    context = {'form':form}
    return render(request,'registration/signup.html',context)
