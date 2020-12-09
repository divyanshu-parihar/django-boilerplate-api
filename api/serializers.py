from rest_framework import serializers
from api.models import students



class studentSerializers(serializers.Serializer):
	id = serializers.IntegerField(read_only=True)
	name = serializers.CharField(max_length=100)
	email = serializers.EmailField()


	def create(self,valided_data):
		return students.objects.create(**valided_data)

	# field level validation
	# def validate_email(self,value):
	# 	if len(value)>20:
	# 		raise serializers.ValidationError('email is invalid')
	# 	return value

	#object level validations
	def validate(self,data):
		name =data.get('name')
		email = data.get('email')
		if len(email)== 0:
			raise serializers.ValidationError('enter the valid length')
		return data

	def update(self,instance, validated_data):
		instance.name = validated_data.get('name')
		instance.email = validated_data.get('email')

		instance.save()
		return instance
	


	class Meta:
		model = students
		fields = ['id', 'name', 'email']



