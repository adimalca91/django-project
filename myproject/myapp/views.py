from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Welcome to the Little Lemon!")

# Path Parameters
def pathview(request, name, id):
    return HttpResponse(f"Path Parameters: Name: {name}, User ID: {id}")

# Query String Parameters
def qryview(request):
    name = request.GET['name']
    id = request.GET['id']
    return HttpResponse(f"Query String Parameters: Name: {name}, User ID: {id}")


    
