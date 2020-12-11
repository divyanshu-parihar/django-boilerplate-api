from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import students
from .serializers import studentSerializers

#<------------------ function based view----------------->




# which is handled by imported in rest_framework Response
# @api_view(['GET','POST']) # note --> by default GET is passed as list .
# #api_view imported to see everything in the browser!
# def homeApi(request): #normal view 
# 	if request.method == 'POST':
# 		return Response({'msg':'THIS IS A POST REQUEST','data':request.data})
	
# 	return Response({'msg':'THIS IS A GET REQUEST','data':request.data})
#<------------------ function based view ENDING----------------->

#<------------------ CRUD FUNCTIONALITY----------------->
@api_view(['GET','POST','PUT','DELETE'])
def homeApi(request):
	if request.method == 'GET':
		id = request.data.get('id')
		if id is not None:
			student = students.objects.all(id= id)
			serialzer = studentSerializers(student)
			return Response(serialzer.data)
		else:
			student = students.objects.all()
			serializer = studentSerializers(student ,many = True)
			return Response(serializer.data)
	
	if request.method == 'POST':
		data = request.data
		serializer = studentSerializers(data=data)
		if serializer.is_valid():
			serializer.save()
			return Response({'msg':serializer.data})
		return Response({'msg':serializer.errors})