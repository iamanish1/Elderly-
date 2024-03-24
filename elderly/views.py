from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"index.html")

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

def doctor(request):
    return render(request,"doctor.html")
