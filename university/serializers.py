from rest_framework import serializers
from .models import *


class FormationtSerializer(serializers.ModelSerializer):
	class Meta:
		model=Formation
		fields='__all__'



class UniversitytGetSerializer(serializers.ModelSerializer):
	#formation= serializers.StringRelatedField(many=True)

	class Meta:
		model=University
		fields='__all__'
		depth=1


class UniversitytPostSerializer(serializers.ModelSerializer):
	#formation= serializers.StringRelatedField(many=True)

	class Meta:
		model=University
		fields='__all__'
		



