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
def homeApi(request):
		return Response({'msg':'hello world!'})