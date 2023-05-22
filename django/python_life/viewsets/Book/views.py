from django.shortcuts import render
from .models import *
from .serializer import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

class Studentviewsets(viewsets.ViewSet):
    # list (get)
    def list(self, request):
        queryset = Student.objects.all()
        serializer = StudentSerializer(queryset, many=True)
        return Response(serializer.data)

    # retrieve (get)
    def retrieve(self, request, pk=None):
        id = pk
        if id is not None:
            queryset = Student.objects.get(id=id)
            serializer = StudentSerializer(queryset)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # create (post)
    def create(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Complete data created'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # update (put)
    def update(self, request, pk=None):
        id = pk
        queryset = Student.objects.get(id=id)
        serializer = StudentSerializer(queryset, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Complete data Updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # delete (delete)
    def destroy(self, request, pk=None):
        id = pk
        queryset = Student.objects.get(id=id)
        queryset.delete()
        return Response({'msg': 'deleted'})

