from django.urls import path,include
from .views import studentModelViewSet
from rest_framework.routers import DefaultRouter



router = DefaultRouter()


router.register('student',studentModelViewSet,basename='student')
urlpatterns = [
    path('',include(router.urls)),
]