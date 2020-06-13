from django.urls import path, include


# views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]