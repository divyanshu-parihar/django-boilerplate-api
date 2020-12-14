from .models import students
from .serializers import studentSerializers
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly
from .custompermission import MyPermission
# for function based views
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes,permission_classes

# add @authentication_classes(Authentication)
# @permission_classes(IsAuthenticated)



class studentModelViewSet(ModelViewSet):
	queryset = students.objects.all()
	serializer_class = studentSerializers
	authentication_classes = [SessionAuthentication]
	# permission_classes = [IsAuthenticated]
	# permission_classes = [IsAdminUser]
	# permission_classes = [IsAuthenticatedOrReadOnly]
	# permission_classes = [DjangoModelPermissions]
	# permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
	permission_classes = [MyPermission]
	
