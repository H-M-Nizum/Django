from django.shortcuts import render
from .models import BooksModel
from .serializers import BooksSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def booksApiView(request, pk=None):
    # GET
    if request.method == "GET":
        if pk is not None:
            try:
                book_instance = BooksModel.objects.get(id=pk)
            except BooksModel.DoesNotExist:
                return Response(
                    {"error": "Book not found"},
                    status=status.HTTP_404_NOT_FOUND
                )

            serialize_data = BooksSerializer(book_instance)
            return Response(
                serialize_data.data,
                status=status.HTTP_200_OK
            )

        else:
            book_list = BooksModel.objects.all()
            serialize_data = BooksSerializer(book_list, many=True)

            return Response(
                serialize_data.data,
                status=status.HTTP_200_OK
            )
    
    # POST
    if request.method == "POST":
        serialize_data = BooksSerializer(data = request.data)
        if serialize_data.is_valid():
            serialize_data.save()
            return Response({
                "status": True,
                "message" : "Book Create Successfully.",
                "data" : serialize_data.data
            }, status=status.HTTP_201_CREATED)
        else:
            return Response({
                "status": False,
                "message": "Validation Error",
                "errors": serialize_data.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        
    
    # PUT
    if request.method == "PUT":
        book_instance = BooksModel.objects.get(id=pk)
        serialize_data = BooksSerializer(book_instance, data = request.data)
        if serialize_data.is_valid():
            serialize_data.save()
            return Response({
                "status": True,
                "message" : "Book Update Successfully.",
                "data" : serialize_data.data
            }, status=status.HTTP_201_CREATED)
        else:
            return Response({
                "status": False,
                "message": "Validation Error",
                "errors": serialize_data.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        

    # PATCH
    if request.method == "PATCH":
        book_instance = BooksModel.objects.get(id=pk)
        serialize_data = BooksSerializer(book_instance, data = request.data, partial=True)
        if serialize_data.is_valid():
            serialize_data.save()
            return Response({
                "status": True,
                "message" : "Book Partially Update Successfully.",
                "data" : serialize_data.data
            }, status=status.HTTP_201_CREATED)
        else:
            return Response({
                "status": False,
                "message": "Validation Error",
                "errors": serialize_data.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        
    # DELETE
    if request.method == "DELETE":
        try:
            book_instance = BooksModel.objects.get(id=pk)
        except BooksModel.DoesNotExist:
            return Response({
                    "status": False,
                    "message": f"Book with id={pk} not found"
                }, status=status.HTTP_404_NOT_FOUND)

        # serialize before deleting, if you want to return deleted data
        serialized = BooksSerializer(book_instance).data
        book_instance.delete()

        return Response({
                "status": True,
                "message": "Book deleted successfully",
                "data": serialized
            }, status=status.HTTP_200_OK)
        
    # Anything else (POST, PUT, DELETE, etc.)
    return Response(
        {"error": "Method not allowed"},
        status=status.HTTP_405_METHOD_NOT_ALLOWED
    )