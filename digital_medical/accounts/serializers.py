from rest_framework import serializers
from .models import User

class UserRegisterSerializers(serializers.ModelSerializer):
    password2 = serializers.CharField(
        write_only=True,
        style={'input_type': 'password'}
    )

    class Meta:
        model = User
        fields = "__all__"
        read_only_fields = ['created_at', 'updated_at']
        extra_kwargs = {
            'password': {'write_only': True},  # hide password in responses
        }


    # check Password and password2 same or not
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError("Password and Confirm Password doesn't match")
        return attrs
    
    # Create Method
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    

class UserLoginSerializers(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    class Meta:
        model = User
        fields = ['email', 'password']