from django.urls import path
from .views import homeApi

urlpatterns = [
    path('',homeApi.as_view()),
    path('user/<int:pk>/',homeApi.as_view()),
]