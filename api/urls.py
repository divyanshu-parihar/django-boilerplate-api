from django.urls import path
from . import views

urlpatterns = [
path('',views.homeApi),
path('update/',views.updateStudent),
path('update/<int:id>',views.viewStudent),
]