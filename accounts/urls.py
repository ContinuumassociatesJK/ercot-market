from . import views
from django.urls import path,include

urlpatterns = [
    path('',views.register ),
    path('loginusercredentialseegridintel-8bd7ae92e39296d811adede9642bafbdd6942fbb0ce207971c7ff60764a2be87da365c5db6e70e9c53533f9deb',views.loginusereegridintel ),
    path('loginusercredentialseegridintel-8bd7ae92e39296d811adede9642bafbdd6942fbb0ce207971c7ff60764a2be87da365c5db6e70e9c53533f9deb',views.logoutuser ),
    path('register',views.register ),

]