from .models import students
from .serializers import studentSerializers
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

# class studentModelViewSet(viewsets.ModelViewSet):#only change the inherited class it will haange everyting by itserlf.
# 	queryset = students.objects.all()
# 	serializer_class = studentSerializers
# read only model viewset
class studentReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
 	queryset = students.objects.all()
 	serializer_class = studentSerializers