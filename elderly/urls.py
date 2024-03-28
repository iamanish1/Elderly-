from django.contrib import admin
from django.urls import path,include
from elderly import views 

urlpatterns = [
          path("",views.index,name="index"),
          path("doctor_1",views.doctor_1,name="doctor"),
          path("mental_health",views.mental_health,name="mental_health"),
          path("health_report",views.health_report,name="health_report"),
          path("doctors/v1/<str:val>",views.doctor_api,name="doctor_api"),
          path("hospitals/v1/<str:val>",views.hospitals_api,name="hospitals"),
          path("sign",views.sign,name="sign.html"),
          path("login",views.login,name="login.html"),
          path("video_call",views.video_call,name="video_call.html"),
          path("hospitals",views.hospital,name="hospital")

    
]

