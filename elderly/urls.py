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
          path("ambulanceAPI/v1/<str:val>",views.ambulance_api,name="ambulanceAPI"),
          path("userAPI/v1/<str:val>",views.user_api,name="userAPI"),
          path("signup",views.sign,name="sign.html"),
          path("login",views.login1,name="login.html"),
          path("dashboard",views.dashboard,name="dashboard"),
          path("hospitals",views.hospital,name="hospital"),
          path("logout",views.logout,name="logout"),
          path("user",views.user,name="user"),
          path("ambulance",views.ambulance,name="ambulance"),
          path("video",views.video,name="video"),
          path("prompt",views.prompt,name="prompt")
    
]

