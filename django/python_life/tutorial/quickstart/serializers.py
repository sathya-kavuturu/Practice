from rest_framework import serializers
from .models import *

class StudentSerilizer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Student

