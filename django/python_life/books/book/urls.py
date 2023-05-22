from django.urls import path
from .views import *

urlpatterns = [
    path('', book_list, name ='bookList'),
    path('add/', post_book, name = 'postBook'),
    path('update/<int:id>', update_book, name= 'updateBook'),
    path('delete/<int:id>', delete_book, name= 'deleteBook')

]