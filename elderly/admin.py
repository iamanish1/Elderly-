from django.contrib import admin

# Register your models here.
from elderly.models import doctor
from elderly.models import health_reporte
from elderly.models import preciption
from elderly.models import patients


admin.site.register(doctor)
admin.site.register(health_reporte)
admin.site.register(preciption)
admin.site.register(patients)
