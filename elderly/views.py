from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from elderly.models import api_keys,doctor,hospitals
# Create your views here.
def index(request):
    
    return render(request,"index.html")
def doctor_api(request,val):
    api_keys_data=api_keys.objects.all()
    doctors_data=doctor.objects.all()
    lst=[]
    for a in api_keys_data:
        lst.append(a.api_key)
    if val in lst:
        return JsonResponse(list(doctors_data.values()),safe=False)
    return HttpResponse("Invalid API Key")
def mental_health(request):
    return render(request,"mental_health.html")

def health_report(request):
    return render(request,"health_report.html")

def sign(request):
    return render(request,"sign.html")

def login(request):
    return render(request,"login.html")

def video_call(request):
    return render(request,"video_call.html")

def doctor_1(request):
    return render(request,"doctor.html")
def hospitals_api(request,val):

    api_keys_data=api_keys.objects.all()
    hospitals_data=hospitals.objects.all()
    lst=[]
    for a in api_keys_data:
        lst.append(a.api_key)
    if val in lst:
        return JsonResponse(list(hospitals_data.values()),safe=False)
    return HttpResponse("Invalid API Key")