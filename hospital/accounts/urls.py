from django.contrib import admin
from django.urls import path
from accounts.views import doctors, department, get_doctor, patients, get_patient, patient_records, get_patient_record, get_doctor_in_department, get_patient_in_department

urlpatterns = [
    path('doctors/', doctors, name='doctors'),
    path('doctors/<int:id>/', get_doctor, name='get_doctor'),
    path('patients/', patients, name='patients'),
    path('patients/<int:id>/', get_patient, name='get_patient'),
    path('patient_records/', patient_records, name='patient_records'),
    path('patient_records/<int:id>/', get_patient_record, name='get_patient_record'),
    path('departments/', department, name='departments'),
    path('department/<int:did>/doctors/', get_doctor_in_department, name='get_doctor_in_department'),
    path('department/<int:did>/patients/', get_patient_in_department, name='get_patient_in_department'),
]
