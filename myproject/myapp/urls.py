from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('getuser/<name>/<id>', views.pathview, name='pathview'), # Path Parameters
    path('getuser/', views.qryview, name='qryview'), # Query String Parameters - GET requests
    path('showform/', views.showform, name='showform'), # Body Parameters - POST requests
    path('myapp/getform/', views.getform, name='getform'), # Body Parameters - POST requests + according to the action attribute in the html file
    path('drinks/<str:drink_name>', views.drinks, name='drink_name'), # URL parameters with type converter
]
