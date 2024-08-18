from django.shortcuts import render
from django.http import JsonResponse
from .models import Patients_Record
from auth_user.models import Doctors_Detail, Patients_Detail, Department
from django.contrib.auth.decorators import login_required

# Get a Doctor
@login_required(login_url='/')
def get_doctor(request, id):
    try:
        doctor = Doctors_Detail.objects.get(id=id)
        if not request.user.is_staff:
            return JsonResponse({'status': 'You are not authorized to view this'})
    except Doctors_Detail.DoesNotExist:
        return JsonResponse({'status': 'Doctor not found'})
    if request.method == 'GET':
        return JsonResponse({
            'Name': doctor.Name,
            'Age': doctor.Age,
            'Department': doctor.Department_id.Name
        })
    if request.method == 'PUT':
        doctor.Name = request.POST.get('Name')
        doctor.Age = request.POST.get('Age')
        doctor.Department_id = request.POST.get('Department_id')
        doctor.save()
        return JsonResponse({'status': 'Doctor updated successfully'})
    if request.method == 'DELETE':
        doctor.delete()
        return JsonResponse({'status': 'Doctor deleted successfully'})

# Get and ADD doctors
@login_required(login_url='/')
def doctors(request):
    if not request.user.is_staff:
                return JsonResponse({'status': 'You are not authorized to view this'})
    if request.method == 'GET':
        try:
            doctor = Doctors_Detail.objects.all()
        except Doctors_Detail.DoesNotExist:
            return JsonResponse({'status': 'Doctor not found'})
        doctors_list = list(doctor.values())
        return JsonResponse(doctors_list, safe=False)
    if request.method == 'POST':
        doctor = Doctors_Detail.objects.create(
            Name=request.POST.get('Name'),
            Age=request.POST.get('Age'),
            Department_id=request.POST.get('Department_id'),
            Email=request.POST.get('Email')
        )
        doctor.save()
        return JsonResponse({'status': 'Doctor created successfully'})
# Get and ADD department
@login_required(login_url='/')
def department(request):
    if not request.user.is_staff:
        return JsonResponse({'status': 'You are not authorized to view this'})
    if request.method == 'GET':
        departments = Department.objects.all()
        departments_list = list(departments.values())
        return JsonResponse(departments_list, safe=False)
    elif request.method == 'POST':
        department = Department.objects.create(
            Name=request.POST.get('Name'),
            Diagnostics=request.POST.get('Diagnostics'),
            Location=request.POST.get('Location'),
            Specialization=request.POST.get('Specialization')
        )
        department.save()
        return JsonResponse({'status': 'Department created successfully'})

# Get and ADD patients
@login_required(login_url='/')
def patients(request):
    if not request.user.is_staff:
        return JsonResponse({'status': 'You are not authorized to view this'})
    if request.method == 'GET':
        patients = Patients_Detail.objects.all()
        patients_list = list(patients.values())
        return JsonResponse(patients_list, safe=False)
    elif request.method == 'POST':
        patient = Patients_Detail.objects.create(
            Name=request.POST.get('Name'),
            Age=request.POST.get('Age'),
            Email=request.POST.get('Email')
        )
        patient.save()
        return JsonResponse({'status': 'Patient created successfully'})

# Get a Patient
@login_required(login_url='/')
def get_patient(request, id):
    if not request.user.is_staff:
        return JsonResponse({'status': 'You are not authorized to view this'})
    if request.method == 'GET':
        patient = Patients_Detail.objects.get(id=id)
        return JsonResponse({
            'Name': patient.Name,
            'Age': patient.Age
        })
    if request.method == 'PUT':
        patient = Patients_Detail.objects.get(id=id)
        patient.Name = request.POST.get('Name')
        patient.Age = request.POST.get('Age')
        patient.save()
        return JsonResponse({'status': 'Patient updated successfully'})
    if request.method == 'DELETE':
        patient = Patients_Detail.objects.get(id=id)
        patient.delete()
        return JsonResponse({'status': 'Patient deleted successfully'})

# Get and ADD patient records
@login_required(login_url='/')
def patient_records(request):
    if not request.user.is_staff:
        return JsonResponse({'status': 'You are not authorized to view this'})
    if request.method == 'GET':
        records = Patients_Record.objects.all()
        records_list = list(records.values())
        return JsonResponse(records_list, safe=False)
    elif request.method == 'POST':
        record = Patients_Record.objects.create(
            Patient_id=request.POST.get('Patient_id'),
            Doctor_id=request.POST.get('Doctor_id'),
            Created_date=request.POST.get('Created_date'),
            Diagnostics=request.POST.get('Diagnostics'),
            Observations=request.POST.get('Observations'),
            Treatments=request.POST.get('Treatments'),
            Department_id=request.POST.get('Department_id'),
            Misc=request.POST.get('Misc')
        )
        record.save()
        return JsonResponse({'status': 'Record created successfully'})
    
# Get a Patient Record
@login_required(login_url='/')
def get_patient_record(request, id):
    try:
        record = Patients_Record.objects.get(Patient_id=id)
        if(request.user.username != record.Patient_id.Email):
            return JsonResponse({'status': 'You are not authorized to view this record'})
    except Patients_Record.DoesNotExist:
        return JsonResponse({'status': 'No Reports found'})
    if request.method == 'GET':
        return JsonResponse({
            'Patient_id': record.Patient_id.id,
            'Patient_name': record.Patient_id.Name,
            'Doctor_id': record.Doctor_id.id,
            'Doctor_name': record.Doctor_id.Name,
            'Created_date': record.Created_date,
            'Diagnostics': record.Diagnostics,
            'Observations': record.Observations,
            'Treatments': record.Treatments,
            'Department_id': record.Department_id.Name,
            'Misc': record.Misc
        })
    if request.method == 'PUT':
        record.Patient_id = request.POST.get('Patient_id')
        record.Doctor_id = request.POST.get('Doctor_id')
        record.Created_date = request.POST.get('Created_date')
        record.Diagnostics = request.POST.get('Diagnostics')
        record.Observations = request.POST.get('Observations')
        record.Treatments = request.POST.get('Treatments')
        record.Department_id = request.POST.get('Department_id')
        record.Misc = request.POST.get('Misc')
        record.save()
        return JsonResponse({'status': 'Record updated successfully'})
    if request.method == 'DELETE':
        record = Patients_Record.objects.get(record_id=id)
        record.delete()
        return JsonResponse({'status': 'Record deleted successfully'})
    
# Get a doctor in particular department
@login_required(login_url='/')
def get_doctor_in_department(request, did):
    if not request.user.is_staff:
        return JsonResponse({'status': 'You are not authorized to view this'})
    if request.method == 'GET':
        doctors = Doctors_Detail.objects.filter(Department_id=did)
        doctors_list = list(doctors.values())
        return JsonResponse(doctors_list, safe=False)
    
# Get a patients in particular department
@login_required(login_url='/')
def get_patient_in_department(request, did):
    if not request.user.is_staff:
        return JsonResponse({'status': 'You are not authorized to view this'})
    if request.method == 'GET':
        patients = Patients_Record.objects.filter(Department_id=did)
        patients_list = list(patients.values())
        return JsonResponse(patients_list, safe=False)