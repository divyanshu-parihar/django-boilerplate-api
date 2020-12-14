from .models import students
from .serializers import studentSerializers
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response

class studentList(viewsets.ViewSet):#only change the inherited class it will haange everyting by itserlf.
	def get(self,request):
		student = students.objects.all()
		serializer= studentSerializers(student,many= True)
		return Response(serializer.data)


	def retrieve(self,request,pk):
		id= pk
		if id is not None:
			stu = students.objects.get(id= id)
			serializer = studentSerializers(stu)
			return Response(serializer.data)
	
	def create(self,request):
		serializer = studentSerializers(data= request.data)
		if serializer.is_valid():
			return Response({'msg' : 'Data created'},status= status.HTTP_201_CREATED)
		return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)