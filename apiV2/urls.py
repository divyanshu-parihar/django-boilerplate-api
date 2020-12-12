from django.urls import path
from .views import get_student,change_student

urlpatterns = [
    path('',get_student.as_view()),
    path('<int:pk>/',change_student.as_view()),
]