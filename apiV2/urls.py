from django.urls import path,include
from .views import studentList
from rest_framework.routers import DefaultRouter



router = DefaultRouter()


router.register('',studentList,basename='student')
urlpatterns = [
    path('',include(router.urls)),
]