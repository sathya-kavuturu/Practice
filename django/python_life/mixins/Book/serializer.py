from rest_framework.serializers import ModelSerializer
from .models import *

class StudentSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Student