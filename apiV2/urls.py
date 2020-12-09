from django.urls import path
from .views import *

urlpatterns = [
path('',homeApi),
path('update/',updateStudent),
path('update/<int:id>',viewStudent),
]