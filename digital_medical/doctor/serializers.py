from rest_framework import serializers
from . models import DoctorModel

# ModelSerializer auto-generates fields from your model.
# fields = '__all__' includes all fields — you can also manually write:
# class DoctorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = DoctorModel
#         fields = '__all__'  # or list fields manually if you want control
#         read_only_fields = ['created_at', 'updated_at']  # prevent editing via API

# ###### This code also work but less optimize
class DoctorSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=250)
    designation = serializers.CharField(max_length=250, required=False, allow_blank=True, allow_null=True)
    email = serializers.EmailField(max_length=250)
    phone = serializers.CharField(max_length=12)
    age = serializers.IntegerField()
    
    # Auto timestamp fields
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)  

    def create(self, validated_data):
        return DoctorModel.objects.create(**validated_data)