from django.urls import path
from . import views

urlpatterns = [
    path('', views.shorter, name="shorterUrl")
]