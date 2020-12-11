from django.urls import path
from .views import homeApi

urlpatterns = [
    path('',homeApi),
]