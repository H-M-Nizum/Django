from django.shortcuts import render
from django.template.context_processors import request
import json
from .tasks import add, sub

# Create your views here.
def homeView(request):
    # Enque Task using delay()
    result = add.delay(30, 40)
    print("Inside Home View ===================== ", result)
    return render(request, "myapp/home.html")


def aboutView(request):
    #Enaue Task using 
    # result = sub.apply_async(args=[90, 23])
    # print("Inside About Page ======== : ", result)
    return render(request, 'myapp/about.html')

def servicesView(request):
    return render(request, 'myapp/services.html')

def contactView(request):
    return render(request, 'myapp/contact.html')

def displayTaskView(request):
    result = sub.apply_async(args=[90, 23])
    print("Inside About Page ======== : ", result)
    return render(request, 'myapp/display_addition_value_after_task_exicution.html', {
        'task_id': result.id
    })


from django.http import JsonResponse
from celery.result import AsyncResult

def get_task_result(request, task_id):
    result = AsyncResult(str(task_id))
    print("Get Task Result --- ", result)
    if result.ready():
        data = {
            'id': task_id,
            'status': result.status,
            'state': result.state,
            'result': result.result,
        }
        return JsonResponse({'status': 'done', 'result': data})
    else:
        return JsonResponse({'status': 'pending'})
