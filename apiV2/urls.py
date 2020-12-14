from django.urls import path,include
from .views import studentReadOnlyModelViewSet
from rest_framework.routers import DefaultRouter



router = DefaultRouter()


router.register('student',studentReadOnlyModelViewSet,basename='student')
urlpatterns = [
    path('',include(router.urls)),
]