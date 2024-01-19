from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('getuser/<name>/<id>', views.pathview, name='pathview'),
]
