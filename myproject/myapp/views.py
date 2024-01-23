from django.shortcuts import render
from django.http import HttpResponse
from myapp.forms import InputForm


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
        id = request.POST['userid']        # According to the name attribute in the html file
        name = request.POST['nameparam']   # According to the name attribute in the html file
    return HttpResponse(f"Body Parameters: Name: {name}, User ID: {id}")

# URL Parameters - with path converter
def showdrinks(request):
    return render(request, 'showdrinks.html')

def drinks(request, drink_name):
    drinks = {
        'mocha' : 'type of coffee',
        'tea' : 'type of beverage',
        'lemonade' : 'type of refreshment'
    }
    if drink_name not in drinks:
        drink_description = 'This drink is not available in our shop, please choose a different drink.'
    else:
        drink_description = drinks[drink_name]
    return HttpResponse(f"<h2>{drink_name}</h2> {drink_description}")

# Form Class - creating a form using the Django's form class
def form_view(request):
    form = InputForm() # an instance object of the InputForm class
    context = {"form":form}
    return render(request, "home.html", context)