from .models import students
from .serializers import studentSerializers
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
class studentModelViewSet(ModelViewSet):
	queryset = students.objects.all()
	serializer_class = studentSerializers
	# authentication_classes = [BasicAuthentication]
	# permission_classes = [IsAuthenticated]