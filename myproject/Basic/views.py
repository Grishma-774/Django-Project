from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def details(request):
    info=request.GET.get('name','sanjay')
    location=request.GET.get('city','banglore')
    return HttpResponse(f"my name is {info} i am from {location}")

