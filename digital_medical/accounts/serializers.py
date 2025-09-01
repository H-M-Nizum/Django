from rest_framework import serializers
from .models import User
from django.utils.encoding import smart_str, force_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from .utils import Util

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

class UserProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'full_name', 'phone_number', 't_c', 'address']
        read_only_fields = ['created_at', 'updated_at']

class UserChangePasswordSerializers(serializers.Serializer):
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})
    password2 = serializers.CharField(write_only=True, style={'input_type': 'password'})

    class Meta:
        fields = ['password', 'password2']

    # check Password and password2 same or not
    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        user = self.context.get('user')
        if password != password2:
            raise serializers.ValidationError("Password and Confirm Password doesn't match")
        
        user.set_password(password)
        user.save()
        return attrs

class sendPasswordResetEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)
    class Meta:
        fields = ['email']

    def validate(self, attrs):
        email = attrs.get('email')
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            # uid = user.id # But i need encoded uid
            uid = urlsafe_base64_encode(force_bytes(user.id))
            print("uid ------------------------------- ", user, user.id, uid)
            token = PasswordResetTokenGenerator().make_token(user)
            print("Token -=========================== ", token)
            link = 'http://localhost:3000/api/user/password-reset/' + uid + '/' + token
            print("Link ------------------------------------ ", link)
            
            # TODO : Send Email With Reset Password Link
            data = {
                "subject": "Password Reset Link",
                "body": f"Click Following Link To Reset Your Password  {link}",
                "to_email": user.email
            }
            Util.send_email(data)

            return attrs
        else:
            raise serializers.ValidationError("User Not Register")



class UserResetPasswordSerializers(serializers.Serializer):
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})
    password2 = serializers.CharField(write_only=True, style={'input_type': 'password'})

    class Meta:
        fields = ['password', 'password2']

    # check Password and password2 same or not
    def validate(self, attrs):
        try:
            password = attrs.get('password')
            password2 = attrs.get('password2')
            uid = self.context.get('uid')
            token = self.context.get('token')
            if password != password2:
                raise serializers.ValidationError("Password and Confirm Password doesn't match")
            
            # Decode Uid
            id = smart_str(urlsafe_base64_decode(uid))
            user = User.objects.get(id=id)

            # Check Valid or not
            if not PasswordResetTokenGenerator().check_token(user, token):
                raise serializers.ValidationError("Token is Not valid Or Expaired")
            
            # Set Password
            user.set_password(password)
            user.save()
            return attrs
        except DjangoUnicodeDecodeError:
            raise serializers.ValidationError("Token is Not valid Or Expaired")