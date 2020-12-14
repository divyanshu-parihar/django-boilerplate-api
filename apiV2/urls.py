from django.urls import path,include
from .views import studentModelViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('', studentModelViewSet)
urlpatterns = [
    path('',include(router.urls)),
    path('auth/',include('rest_framework.urls'))
]