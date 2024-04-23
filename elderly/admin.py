from django.contrib import admin

# Register your models here.
from elderly.models import doctor
from elderly.models import hospitals
from elderly.models import prescription,RegUser
from elderly.models import patients,api_keys
from elderly.models import ambulance_book
from elderly.models import  RegUser2
 



admin.site.register(doctor)
admin.site.register(hospitals)
admin.site.register(prescription)
admin.site.register(patients)
admin.site.register(api_keys)
admin.site.register(RegUser)
admin.site.register(ambulance_book)
admin.site.register(RegUser2)

