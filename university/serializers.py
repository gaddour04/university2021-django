from rest_framework import serializers
from .models import *


class FormationtSerializer(serializers.ModelSerializer):
	class Meta:
		model=Formation
		fields='__all__'


class UniversitytSerializer(serializers.ModelSerializer):
	class Meta:
		model=University
		fields='__all__'
		depth=1