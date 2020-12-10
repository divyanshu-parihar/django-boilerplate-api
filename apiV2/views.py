import io

from django.http import HttpResponse, JsonResponse
# Create your views here.
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .models import students
from .serializers import studentSerializers


# Create your views here.
# see all the students in the data base
def homeApi(request):
	try:
		student_list = students.objects.all()
		content_students = studentSerializers(student_list,many=True)
		json_data = JSONRenderer().render(content_students.data)
		return HttpResponse(json_data,content_type='application/json')
	except Exception as e:
		return HttpResponse({'error':e},content_type='application/json')



#view specific student form the database with id provided in url /api/<id>
def viewStudent(request,id):
	try:
		student = students.objects.get(id= id)
	except:
		return JsonResponse({'msg':"student not found!"})	
	content_students = studentSerializers(student)
	json_data = JSONRenderer().render(content_students.data)
	return HttpResponse(json_data,content_type='application/json')


#below this all the Post reqest are handled!
#below this all the CRUD functionality is added 
@csrf_exempt
def updateStudent(request):

	# to add to the database
	if request.method == 'POST':
		json_data = request.body
		stream = io.BytesIO(json_data)
		python_data = JSONParser().parse(stream)
		phone_number = python_data['phone_number']
		check = students.objects.filter(phone_number = phone_number).exists()
		if check:
			return JsonResponse({'msg':'student already exist'})
		serializer= studentSerializers(data=python_data)
		if serializer.is_valid():
			serializer.save()
			msg = {'msg':'data updated'}
			json_data = JSONRenderer().render(msg)
			return HttpResponse(json_data,content_type=
				'application/json')
		else:
			msg = {'msg':serializer.errors}
			json_data = JSONRenderer().render(msg)
			return HttpResponse(json_data,content_type=
				'application/json')
	

	# to delete the specific user from the database
	if request.method == 'DELETE':
		json_data = request.body
		stream = io.BytesIO(json_data)
		python_data = JSONParser().parse(stream)
		id  = python_data['id']
		check = students.objects.filter(id=id).exists()
		if check== False:
			return JsonResponse({'msg':'student donot exists'})
		student_delete = students.objects.get(id = id)

		student_delete.delete()
		return JsonResponse({"msg":'students deleted!'})
	
	# fully upadate the required student field
	if request.method == 'PUT':
		stream = io.BytesIO(request.body)
		data = JSONParser().parse(stream)
		id= data.get('id')

		check = students.objects.filter(id=id).exists()
		if check == False:
			return JsonResponse({'msg':'student donot exists'})
		student = students.objects.get(id=id)
		serializer = studentSerializers(student,data=data)
		if serializer.is_valid():
			serializer.save()
			return JsonResponse({'msg':serializer.data})
		return JsonResponse(serializer.errors)

	# parially update the field of student


	## partial update can not be done with present database because 
	# all the fiels are required till now .

	# if request.method == 'PATCH':
	# 	stream = io.BytesIO(request.body)
	# 	python_data = JSONParser().parse(stream)
	# 	id= python_data.get('id')

	# 	check = students.objects.filter(id=id).exists()
	# 	if check == False:
	# 		return JsonResponse({'msg':'student not found!'})

	# 	student = students.objects.get(id=id)
	# 	serializer = studentSerializers(student,data=python_data,partial=True)
	# 	if serializer.is_valid():
	# 		serializer.save()
	# 		return JsonResponse({'msg':'request data patched successfully'})
	# 	return JsonResponse({'msg':'request failed! check passed data'})
