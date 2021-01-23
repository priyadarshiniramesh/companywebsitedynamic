from django.shortcuts import render
from .models import product

from .models import people
# Create your views here.

def home(request):
    context = {}
    return render(request, 'companywebsite/home.html', context)

def productlist(request):
    context = {}
    context['products'] = product.objects.all()

    return render(request, 'companywebsite/product.html', context)    


def peoplelist(request):
    context = {}
    context['peoples'] = people.objects.all()
    return render(request, 'companywebsite/people.html', context)  


def contactus(request):
    context = {}
    return render(request, 'companywebsite/contact.html', context)  