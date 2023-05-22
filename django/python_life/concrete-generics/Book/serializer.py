from rest_framework.serializers import ModelSerializer
from .models import Student

class StudentSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Student