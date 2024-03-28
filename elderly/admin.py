from django.contrib import admin

# Register your models here.
from elderly.models import doctor
from elderly.models import hospitals
from elderly.models import prescription,RegUser
from elderly.models import patients,api_keys


admin.site.register(doctor)
admin.site.register(hospitals)
admin.site.register(prescription)
admin.site.register(patients)
admin.site.register(api_keys)
admin.site.register(RegUser)
