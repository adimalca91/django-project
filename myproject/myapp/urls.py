from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('getuser/<name>/<id>', views.pathview, name='pathview'), # Path Parameters
    path('getuser/', views.qryview, name='qryview'), # Query String Parameters - GET requests
    path('showform/', views.showform, name='showform'), # Body Parameters - POST requests
    path('myapp/getform/', views.getform, name='getform'), # Body Parameters - POST requests
]
