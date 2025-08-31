from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserRegisterSerializers, UserLoginSerializers
from django.contrib.auth import authenticate
from .renderers import UserRenderers
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import AuthenticationFailed

# Creating tokens manually
def get_tokens_for_user(user):
    if not user.is_active:
      raise AuthenticationFailed("User is not active")

    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
# View for Register
class UserRegistrationViews(APIView):
    renderer_classes = [UserRenderers]
    def post(self, request, format=None):
        serializer_data = UserRegisterSerializers(data = request.data)
        if serializer_data.is_valid(raise_exception=True):
            user = serializer_data.save()
            token = get_tokens_for_user(user)
            return Response({'status': 'success', 'msg': 'User Registration Successfully Complete', 'data' : serializer_data.data, 'token': token}, status=status.HTTP_201_CREATED)
        return Response({'status': 'error', 'msg' : 'Failed to Register User', 'error' : serializer_data.errors}, status=status.HTTP_400_BAD_REQUEST)
    

# View for Login
class UserLoginViews(APIView):
    renderer_classes = [UserRenderers]
    def post(self, request, format=None):
        serializers_data = UserLoginSerializers(data = request.data)
        if serializers_data.is_valid(raise_exception=True):
            email = serializers_data.data.get("email")
            password = serializers_data.data.get("password")
            
            user = authenticate(email=email, password=password)
            if user is not None:
                token = get_tokens_for_user(user)
                return Response({'status': 'success', 'msg': 'User Login Successfully Complete', 'token': token}, status=status.HTTP_200_OK)
            else:
                return Response({'status': 'error', 'msg': 'Failed to User Login', 'error' : {'non_field_error' : 'Email or Password is not valid'}}, status=status.HTTP_404_NOT_FOUND)


        return Response({'status': 'error', 'msg': serializers_data.errors}, status=status.HTTP_400_BAD_REQUEST)
