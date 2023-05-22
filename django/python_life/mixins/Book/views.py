from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from .serializer import *
from .models import *

# Create your views here.

# list & create
class Student_List_Create(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # read
    def get(self, request):
        return self.list(request)
    # create
    def post(self, request):
        return self.create(request)
    
# retrieve, update & delete
class Student_Dis_Up_Del(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # retrieve
    def get(self, request, **kwargs):
        return self.retrieve(request, **kwargs)
    # update 
    def put(self, request, **kwargs):
        return self.update(request, **kwargs)
    # delete
    def delete(self, request, **kwargs):
        return self.destroy(request, **kwargs)
    

