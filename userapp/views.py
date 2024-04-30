from django.shortcuts import render, redirect
 

# Create your views here.
def home(request):
    return render(request,'index.html')
def contact(request):
    return render(request,'contact.html')
def client(request):
    return render(request,'client.html')
def products(request):
    return render(request,'products.html')
def about(request):
    return render(request,'about.html')
