from django.contrib import admin
from .models import Appointment, Plan
from import_export.admin import ImportExportModelAdmin


# Register your models here.
class Appointments(ImportExportModelAdmin, admin.ModelAdmin):
    ...


admin.site.register(Appointment,Appointments)

admin.site.register(Plan)
