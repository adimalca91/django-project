from django.shortcuts import render
from django.http import HttpResponse
# from myapp.forms import InputForm
from myapp.forms import LogForm, BookingForm


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

# # Form Class - creating a form using the Django's form class
# def form_view(request):
#     form = InputForm() # an instance object of the InputForm class
#     context = {"form":form}
#     return render(request, "home.html", context)

def form_view(request):
    form = LogForm()
    if request.method == 'POST':
        form = LogForm(request.POST) # updates the form object with the contents of the POST inside the request object (that was submitted - first_name, last_name, time_log)
        if form.is_valid():
            form.save()
    context = {"form" : form}
    return render(request, "home.html", context)

'''
Note, this view function is first being invoked (called) when we enter the local host url with the ending of "bookink/"
and we basically create a GET request for this view. Therefore, the first time we do NOT enter the if statement here
and we only create a form instace object that is empty / not populated with data and we render it with booking.html
and display it to the user - so untill now the user just sees an empty form to fill and submit.
Then, the user fills the reservation form and submits it. When it's submitted a POST request is being created and sent to
the server with the details entered by the user in the body of the request. Also, this view function is being invoked
once again but this time with a POST request - so a form instance object is being created again, but now it's being
populated by the data from the submitted form. Then it's being checked if its valid and if it is then it's saved.
Only, now it's being rendered with the booking.html file, with the details of the user. Also, it's being saved in the
Booking Model to connect to a database table which will save amd store all that information! 
'''
def bookingForm_view(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST) # updates the form object with the contents of the POST inside the request object (that was submitted - first_name, last_name, time_log)
        if form.is_valid():
            form.save()
    context = {"form" : form}
    return render(request, "booking.html", context)