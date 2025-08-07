from django.shortcuts import render
from .models import DoctorModel
from .serializers import DoctorSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse

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
