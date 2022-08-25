from django.shortcuts import render
from .models import Product
from math import ceil

from django.http import HttpResponse

# Create your views here.
def index(request):
    products= Product.objects.all()
    n= len(products)
    nSlides= n//4 + ceil((n/4) + (n//4))
    params={'no_of_slides':nSlides, 'range':range(1,nSlides), 'product': products}
    return render(request,"shop/index.html", params)

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


