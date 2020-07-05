from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.
def cse(request):
    return HttpResponse("Welcome on cse page")

def etc(request):
    return HttpResponse("Welcome on etc page")

def mech(request):
    return HttpResponse("Welcome on mech page")

def civil(request):
    return HttpResponse("Welcome on civil page")
            


    