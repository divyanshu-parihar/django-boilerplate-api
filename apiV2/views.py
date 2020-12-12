from django.shortcuts import render
from .models import students
from .serializers import studentSerializers
from rest_framework import status
#<-----------Generic model serialier and mixins------------>
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin

class get_student(GenericAPIView,ListModelMixin,CreateModelMixin):
	queryset = students.objects.all()
	serializer_class = studentSerializers


	def get(self, request,*args,**kwargs):
		return self.list(request,*args,**kwargs)
	
	def post(self,request,*args,**kwargs):
		return self.create(request ,*args,**kwargs)


# <_________all below these pk value as a argument.you can change it._____________>
class change_student(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
	queryset = students.objects.all()
	serializer_class = studentSerializers
	
	def get(self,request,*args,**kwargs):
		return self.retrieve(request ,*args,**kwargs)
	
	def put(self,request,*args,**kwargs):
		return self.update(request ,*args,**kwargs)

	def delete(self,request,*args,**kwargs):
		return self.destroy(request ,*args,**kwargs)
