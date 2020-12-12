from django.shortcuts import render
from rest_framework.response import Response
from .models import students
from .serializers import studentSerializers
from rest_framework.views import APIView
from rest_framework import status
# <----------------CLASS BASED APIVIEW -------------->

class homeApi(APIView):
	def get(self,request,pk=None,format=None):
		id = pk
		if id is not None:
			student = students.objects.get(id= id)
			serialzer = studentSerializers(student)
			return Response(serialzer.data)
		else:
			student = students.objects.all()
			serializer = studentSerializers(student ,many = True)
			return Response(serializer.data)
	def post(self,request,format=None):
		data = request.data
		serializer = studentSerializers(data=data)
		if serializer.is_valid():
			serializer.save()
			return Response({'msg':serializer.data})
		return Response({'msg':serializer.errors})
	def put(self,request,pk,format= None):
		id = pk
		student = students.objects.get(id= id)
		serializer = studentSerializers(student,data= request.data)
		if serializer.is_valid():
			serializer.save()
			return Response({"msg":'complete data updated'})
		return Response(serializer.errors)