from django.contrib import admin
from django.urls import path
from userapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('contact/',contact,name='contact'),
    path('client/',client,name='client'),
    path('products/',products,name='products'),
    path('about/',about,name='about'),
    
]
