from rest_framework import serializers
from .models import *

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = BooksModel