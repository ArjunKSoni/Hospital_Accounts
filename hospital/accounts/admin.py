from django.contrib import admin

# Register your models here.
from accounts.models import Patients_Record
from auth_user.models import Doctors_Detail, Patients_Detail, Department

admin.site.register(Doctors_Detail)
admin.site.register(Department)
admin.site.register(Patients_Detail)
admin.site.register(Patients_Record)