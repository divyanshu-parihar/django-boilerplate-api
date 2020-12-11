from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view



# function based view
# which is handled by imported in rest_framework Response
@api_view(['GET','POST']) # note --> by default GET is passed as list .
#api_view imported to see everything in the browser!
def homeApi(request): #normal view 
	if request.method == 'POST':
		return Response({'msg':'THIS IS A POST REQUEST'})
	return Response({'msg':'THIS IS A GET REQUEST'})
