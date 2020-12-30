from django.shortcuts import render

# Create your views here.
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.decorators import api_view


from rest_framework.generics import *  #ListAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView,CreateAPIView



class FormationAPI(ListCreateAPIView):
	queryset=Formation.objects.all()
	serializer_class=FormationtSerializer


#iraja3 resultat w ya3mel update w ifasakh
class FormationAPIDetail(RetrieveUpdateDestroyAPIView):
	queryset=Formation.objects.all()
	serializer_class=FormationtSerializer
	lookup_field='id'



class UniversityAPI(ListCreateAPIView):
	queryset=University.objects.all()
	serializer_class=UniversitytSerializer

class UniversityAPIDetail(RetrieveUpdateDestroyAPIView):
	queryset=University.objects.all()
	serializer_class=UniversitytSerializer
	lookup_field='id'



