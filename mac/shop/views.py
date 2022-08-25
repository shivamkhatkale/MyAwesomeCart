from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'shop/index.html')

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    return render(request, 'shop/contactus.html')

def tracker(request):
    return HttpResponse("we are tracker")

def search(request):
    return HttpResponse("we are search")

def productView(request):
    return HttpResponse("we are productView")

def checkout(request):
    return HttpResponse("we are checkout")


