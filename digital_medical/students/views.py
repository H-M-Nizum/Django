from django.shortcuts import render
from .models import StudentModel
from .serializers import StudentSerializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class StudentsApiView(APIView):

    # --------------------------
    # Helper response functions
    # --------------------------
    def success_response(self, message, data=None, code=status.HTTP_200_OK):
        """Standardized success response"""
        return Response({
            "status": True,
            "message": message,
            "data": data or {}
        }, status=code)

    def error_response(self, message, errors=None, code=status.HTTP_400_BAD_REQUEST):
        """Standardized error response"""
        return Response({
            "status": False,
            "message": message,
            "errors": errors or {}
        }, status=code)

    # --------------------------
    # CRUD Methods
    # --------------------------
    def get(self, request, pk=None, format=None):
        if pk is not None:
            try:
                student_instance = StudentModel.objects.get(id = pk)
            except StudentModel.DoesNotExist:
                return self.error_response("No student found.", errors={"detail": "No students available."}, code=status.HTTP_404_NOT_FOUND)

            serializer_data = StudentSerializers(student_instance)
            return self.success_response("Student retrieved successfully.", data=serializer_data.data)
            
        else:
            student_list = StudentModel.objects.all()
            if not student_list.exists():
                return self.error_response("No students found.", errors={"detail": "No students available."}, code=status.HTTP_404_NOT_FOUND)
            
            serializer_data = StudentSerializers(student_list, many=True)
            return self.success_response("Students retrieved successfully.", data=serializer_data.data)
    
    def post(self, request, format=None):
        serializer_data = StudentSerializers(data = request.data)
        if serializer_data.is_valid():
            serializer_data.save()
            return self.success_response("Student created successfully.", data=serializer_data.data, code=status.HTTP_201_CREATED)
            
        else:
            return self.error_response("Failed to create student.", errors={"detail": serializer_data.errors}, code=status.HTTP_400_BAD_REQUEST)
            
        
    def put(self, request, pk, format=None):
        try:
            student_instance = StudentModel.objects.get(id=pk)
        except StudentModel.DoesNotExist:
            return self.error_response("No student found.", errors={"detail": "No students available."}, code=status.HTTP_404_NOT_FOUND)
        
        serializer_data = StudentSerializers(student_instance, data = request.data)
        if serializer_data.is_valid():
            serializer_data.save()
            return self.success_response("Student updated successfully.", data=serializer_data.data)

        return self.error_response("Validation error while updating student.", errors={"detail": serializer_data.errors}, code=status.HTTP_400_BAD_REQUEST)
    
        
    def patch(self, request, pk, format=None):
        try:
            student_instance = StudentModel.objects.get(id=pk)
        except StudentModel.DoesNotExist:
            return self.error_response("No student found.", errors={"detail": "No students available."}, code=status.HTTP_404_NOT_FOUND)
        
        serializer_data = StudentSerializers(student_instance, data=request.data, partial=True)
        if serializer_data.is_valid():
            serializer_data.save()
            return self.success_response("Student updated successfully.", data=serializer_data.data)

        return self.error_response("Validation error while updating student.", errors={"detail": serializer_data.errors}, code=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk, format=None):
        try:
            student_instance = StudentModel.objects.get(id=pk)
        except StudentModel.DoesNotExist:
            return self.error_response("No student found.", errors={"detail": "No students available."}, code=status.HTTP_404_NOT_FOUND)
        
        serializer_data = StudentSerializers(student_instance)
        student_instance.delete()
        return self.success_response("Student Deleted successfully.", data=serializer_data.data)