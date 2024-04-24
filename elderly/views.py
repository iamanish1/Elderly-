from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import JsonResponse,HttpResponse
from elderly.models import api_keys,doctor,hospitals
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout as logouts
from elderly.models import RegUser,doctor,patients,prescription,ambulance_book,RegUser2
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.core.mail import send_mail
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
    if request.method=="POST":
        name=request.POST.get("name")
        mobile=request.POST.get('phone')
        patName=request.POST.get("patname")
        location=request.POST.get("location")
        email=request.POST.get("email")
        password=request.POST.get("password")
        user=User.objects.create_user(username=name,password=password,email=email)
        user.save()

        regObj=RegUser(name=name,mobile=mobile,location=location,email=email,patName=patName)
        regObj.save()
        return redirect("/login")
    return render(request,"sign.html")


def logout(request):
    logouts(request)
    return redirect("/")

@login_required(login_url="/login")
def dashboard(request):
    return render(request,"dashboard.html")


def doctor_1(request):
    return render(request,"doctor.html")

def hospital(request):
     return render(request,"hospital.html")

def hospitals_api(request,val):

    api_keys_data=api_keys.objects.all()
    hospitals_data=hospitals.objects.all()
    lst=[]
    for a in api_keys_data:
        lst.append(a.api_key)
    if val in lst:
        return JsonResponse(list(hospitals_data.values()),safe=False)
    return HttpResponse("Invalid API Key")
@login_required(login_url="/login")
def user(request):
    return render(request,"user.html")
def ambulance(request):
    return render(request,"ambulance.html")
@login_required(login_url="/login")
def video(request):
    return render(request,"video.html")
def ambulance_api(request,val):
    api_keys_data=api_keys.objects.all()
    ambu_data=ambulance_book.objects.all()
    lst=[]
    for a in api_keys_data:
        lst.append(a.api_key)
    if val in lst:
        return JsonResponse(list(ambu_data.values()),safe=False)
    return HttpResponse("Invalid API Key")
def prompt(request):
    return render(request,"prompt.html")
@csrf_protect
def Login(request):
   
    if request.method=="POST":
        uname=request.POST.get("uname")
        password=request.POST.get("password")
        user=authenticate(request,username=uname,password=password)
        if user is not None:
            login(request,user)
            return redirect("user")
        else:
            return HttpResponse("Invalid username or password")
    return render(request,"login.html")
def user_api(request,val):
    api_keys_data=api_keys.objects.all()
    user_data=RegUser2.objects.all()
    lst=[]
    for a in api_keys_data:
        lst.append(a.api_key)
    if val in lst:
        return JsonResponse(list(user_data.values()),safe=False)
    return HttpResponse("Invalid API Key")
