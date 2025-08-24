from django.shortcuts import render
from .models import TeacherModel
from .serializers import TeacherSerializers
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveDestroyAPIView, RetrieveUpdateAPIView
from rest_framework.viewsets import ModelViewSet
# Create your views here.


# View for List and Create
class TeacherListCreateView(ListCreateAPIView):
    queryset = TeacherModel.objects.all()
    serializer_class = TeacherSerializers


# View for Retrive, Update And Destroy
class TeacherRetriveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = TeacherModel.objects.all()
    serializer_class = TeacherSerializers

# View for Retrive and Destroy
class TeacherRetriveDestroyView(RetrieveDestroyAPIView):
    queryset = TeacherModel.objects.all()
    serializer_class = TeacherSerializers


# View for Retrive and Update
class TeacherRetriveUpdateView(RetrieveUpdateAPIView):
    queryset = TeacherModel.objects.all()
    serializer_class = TeacherSerializers

# View for List, Create, Retrive, Update And Destroy using ModelViewset
class TeacherModelViewSetView(ModelViewSet):
    queryset = TeacherModel.objects.all()
    serializer_class = TeacherSerializers