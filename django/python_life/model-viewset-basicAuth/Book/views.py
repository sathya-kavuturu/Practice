from django.shortcuts import render
from .models import *
from .serializer import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
# from rest_framework.authentication import BasicAuthentication
# from rest_framework.permissions import IsAuthenticated
# Create your views here.

class Studentmodelviewset(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]