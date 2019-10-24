from django.urls import path
from . import views #. means this directory

#Set the routing
urlpatterns = [
    path('', views.home)
]
