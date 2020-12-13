from django.urls import path
from .views import studentList,studentUpdate

urlpatterns = [
    path('',studentList.as_view()),
    path('update/<int:pk>',studentUpdate.as_view()),
]