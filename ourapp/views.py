from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    print("Index got executed!")
    return HttpResponse("Hello World")

def about(request):
    print("About got executed!")
    return HttpResponse("This is about page")