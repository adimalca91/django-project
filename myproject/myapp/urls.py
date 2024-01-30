from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('getuser/<name>/<id>', views.pathview, name='pathview'), # Path Parameters
    path('getuser/', views.qryview, name='qryview'), # Query String Parameters - GET requests
    path('showform/', views.showform, name='showform'), # Body Parameters - POST requests
    path('myapp/getform/', views.getform, name='getform'), # Body Parameters - POST requests + according to the action attribute in the html file
    path('drinks/', views.showdrinks, name='drink_name'), # URL parameters with type converter
    path('drinks/<str:drink_name>', views.drinks, name='drink_name'), # URL parameters with type converter
    path("home/", views.form_view), # Creating Forms using Form Class in Django
    path("booking/", views.bookingForm_view), # Creating ModelForm for making a reservation in the restaurant
    path("about/", views.about), # working with tamplates lab
    path("menu/", views.menu), # working with tamplates lab
    path("menufromdatabase/", views.menu_models_templates),
    path('book/', views.book),
]
