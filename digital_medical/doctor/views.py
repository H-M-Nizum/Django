from django.shortcuts import render
from .models import DoctorModel
from .serializers import DoctorSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
import io
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

# Create your views here.

# Get All Doctor record
def doctorViewAll(request):
    # Complex data
    doctors_data = DoctorModel.objects.all()

    # Python dict or Serializers data
    doctors_serializer = DoctorSerializer(doctors_data, many=True)

    # Json Data
    json_data = JSONRenderer().render(doctors_serializer.data)

    # Return Json Data
    return HttpResponse(json_data, content_type='application/json')

# Get Doctor record instance
def doctorInstanceView(request, pk):
    try:
        # Complex data
        doctors_data = DoctorModel.objects.get(id=pk)

        # Python dict or Serializers data
        doctors_serializer = DoctorSerializer(doctors_data)

        # Return Json Data
        return JsonResponse(doctors_serializer.data, safe=False)
    
    except DoctorModel.DoesNotExist:
        return JsonResponse({'error': 'Doctor not found'}, status=404)


@csrf_exempt
def createDoctorView(request):
    # Json data or request body data
    json_data = request.body
    print("json data : ", json_data)

    # json to Stream Data
    stream_data = io.BytesIO(json_data)
    print("stream Data : ", stream_data)

    # Stream to python data
    python_data = JSONParser().parse(stream_data)
    print("python data : ", python_data)

    # Python to complex data
    serializer_data = DoctorSerializer(data=python_data)
    print("Serializer Data : ", serializer_data)

    # Validation check
    if serializer_data.is_valid():
        serializer_data.save()
        response_data = JSONRenderer().render({"msg" : "Successfully Create a Doctor instance"})
    else:
        response_data = JSONRenderer().render({"msg" : "Validation Error", "error" : serializer_data.errors})
    return HttpResponse(response_data, content_type='application/json')

