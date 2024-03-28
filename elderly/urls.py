from django.contrib import admin
from django.urls import path,include
from elderly import views 

urlpatterns = [
          path("",views.index,name="index"),
          path("doctor1",views.doctor_1,name="doctor"),
          path("mental_health",views.mental_health,name="mental_health"),
          path("health_report",views.health_report,name="health_report"),
          path("doctors/v1/<str:val>",views.doctor_api,name="doctor_api"),
          path("hospitals/v1/<str:val>",views.hospitals_api,name="hospitals"),
          path("signup",views.sign,name="sign.html"),
          path("login",views.login1,name="login.html"),
          path("dashboard",views.dashboard,name="dashboard"),
          path("hospitals",views.hospital,name="hospital"),
          path("logout",views.logout,name="logout")
    
]

