from django.shortcuts import render

# Create your views here.
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view


from rest_framework.generics import *  #ListAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView,CreateAPIView



class GetAllFormationAPI(ListAPIView):
	queryset=Formation.objects.all()
	serializer_class=FormationtSerializer

class CreateFormationAPI(CreateAPIView):
	queryset=Formation.objects.all()
	serializer_class=FormationtSerializer


class DeleteFormationAPI(RetrieveDestroyAPIView):
	queryset=Formation.objects.all()
	serializer_class=FormationtSerializer
	lookup_field='id'

class UpdateFormationAPI(RetrieveUpdateAPIView):
	queryset=Formation.objects.all()
	serializer_class=FormationtSerializer
	lookup_field='id'



#iraja3 resultat w ya3mel update w ifasakh
class FormationAPIDetail(RetrieveUpdateDestroyAPIView):
	queryset=Formation.objects.all()
	serializer_class=FormationtSerializer
	lookup_field='id'



class GetAllUniversityAPI(ListAPIView):
	queryset=Universitie.objects.all()
	serializer_class=UniversitytGetSerializer

class CreateUniversityAPI(CreateAPIView):
	queryset=Universitie.objects.all()
	serializer_class=UniversitytPostSerializer

class UpdateUniversityAPI(RetrieveUpdateAPIView):
	queryset=Universitie.objects.all()
	serializer_class=UniversitytGetSerializer
	lookup_field='id'

class DeleteUniversityAPI(RetrieveDestroyAPIView):
	queryset=Universitie.objects.all()
	serializer_class=UniversitytGetSerializer
	lookup_field='id'



