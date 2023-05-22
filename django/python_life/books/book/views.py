from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import *
from .models import *
# Create your views here.

#read
@api_view(['GET'])
def book_list(request):
    books_obj = BooksModel.objects.all() # queryset
    serializer = BookSerializer(books_obj, many = True)
    return Response({'status': 200, 'payload': serializer.data})


#create
@api_view(['POST'])
def post_book(request):
    #books_obj = BooksModel.objects.all() # queryset
    serializer = BookSerializer(data= request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


#update
@api_view(['POST'])
def update_book(request, id):
    books_obj = BooksModel.objects.get(id=id) # queryset
    serializer = BookSerializer(instance= books_obj, data= request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

#delete
@api_view(['DELETE'])
def delete_book(request, id):
    books_obj = BooksModel.objects.get(id=id) # queryset
    books_obj.delete()
    return Response(f"Book with id {id} is deleted ")