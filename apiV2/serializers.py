from rest_framework import serializers
from apiV2.models import students

class studentSerializers(serializers.ModelSerializer):
	class Meta:
		model = students
		fields = fields = '__all__'
		# validators = ['validate_father_name']

	def validate_father_name(self,value):
		if value.lower() == 'xyz':
			raise serializers.ValidationError('enter valid father name')
		return value

