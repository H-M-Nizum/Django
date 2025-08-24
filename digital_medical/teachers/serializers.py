from rest_framework import serializers
from .models import TeacherModel

class TeacherSerializers(serializers.ModelSerializer):
    class Meta:
        model = TeacherModel
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']