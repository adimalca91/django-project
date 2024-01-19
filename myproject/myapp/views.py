from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return HttpResponse("Welcome to the Little Lemon!")

# Path Parameters
def pathview(request, name, id):
    return HttpResponse(f"Path Parameters: Name: {name}, User ID: {id}")

# Query String Parameters - for GET requests
def qryview(request):
    name = request.GET['name']
    id = request.GET['id']
    return HttpResponse(f"Query String Parameters: Name: {name}, User ID: {id}")

# Body Parameters - for POST requests
def showform(request):
    return render(request, "bodyparamform.html")

def getform(request):
    if request.method == "POST":
        id = request.POST['userid']
        name = request.POST['name']
    return HttpResponse(f"Body Parameters: Name: {name}, User ID: {id}")