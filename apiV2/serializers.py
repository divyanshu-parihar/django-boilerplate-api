from rest_framework import serializers
from apiV2.models import students

class studentSerializers(serializers.ModelSerializer):
	class Meta:
		fields = ['id ', 'name',' age ', 'phone_number', 'father_name']

# class studentSerializers(serializers.Serializer):
# 	id = serializers.IntegerField(read_only=True)
# 	name = serializers.CharField(max_length=100)
# 	age=serializers.IntegerField()
# 	phone_number=serializers.IntegerField()
# 	father_name=serializers.CharField(max_length=100)


# 	def create(self,valided_data):
# 		return students.objects.create(**valided_data)

# 	# field level validation
# 	# def validate_email(self,value):
# 	# 	if len(value)>20:
# 	# 		raise serializers.ValidationError('email is invalid')
# 	# 	return value

# 	#object level validations
# 	def validate(self,data):
# 		name =data.get('name')
# 		phone_number = data.get('phone_number')
# 		if len(name)==0 or len(str(phone_number))== 0:
# 			raise serializers.ValidationError('enter the valid length')
# 		return data

# 	def update(self,instance, validated_data):
# 		instance.name = validated_data.get('name')
# 		instance.age = validated_data.get('age')
# 		instance.father_name = validated_data.get('father_name')
# 		instance.phone_number = validated_data.get('phone_number')

# 		instance.save()
# 		return instance
	


# 	class Meta:
# 		model = students
# 		fields = ['id']



