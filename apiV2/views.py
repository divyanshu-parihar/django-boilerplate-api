from .models import students
from .serializers import studentSerializers
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView


class studentList(ListCreateAPIView):#only change the inherited class it will haange everyting by itserlf.
	queryset = students.objects.all()
	serializer_class = studentSerializers


class studentUpdate(RetrieveUpdateDestroyAPIView):#only change the inherited class it will haange everyting by itserlf.
	queryset = students.objects.all()
	serializer_class = studentSerializers