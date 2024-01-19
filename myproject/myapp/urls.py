from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('getuser/<name>/<id>', views.pathview, name='pathview'), # Path Parameters
    path('getuser/', views.qryview, name='qryview'), # Query String Parameters
]
