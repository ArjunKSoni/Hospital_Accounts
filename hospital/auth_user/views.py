from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Patients_Detail, Doctors_Detail, Department

def Login_user(request):
    if request.method == 'POST':
        Email = request.POST.get('Email')
        Password = request.POST.get('Password')
        user = authenticate(username=Email, password=Password)
        if user is not None:
            if user.is_staff:
                User_detail=Doctors_Detail.objects.get(Email=Email)
                login(request, user)
                return redirect('/api/v1/accounts/doctors/')
            else:
                User_detail=Patients_Detail.objects.get(Email=Email)
                login(request, user)
                return redirect(f'/api/v1/accounts/patient_records/{User_detail.id}/')
            
        else:
            return redirect('/signup_patient/')
    else:
        return render(request, 'login.html')
    
def Signup_P(request):
    if request.method == 'POST':
        user=User.objects.create(
            username=request.POST.get('Email'),
            is_staff=False
        )
        user.set_password(request.POST.get('Password'))
        user.save()
        patient = Patients_Detail.objects.create(
            Name=request.POST.get('Name'),
            Age=request.POST.get('Age'),
            Email=request.POST.get('Email')
        )
        patient.save()
        return redirect('/api/v1/accounts/patients/')
    
    else:
        return render(request, 'signupp.html')
    
def Signup_D(request):
    if request.method == 'POST':
        user=User.objects.create(
            username=request.POST.get('Email'),
            is_staff=True
        )
        user.set_password(request.POST.get('Password'))
        user.save()
        try:
            department=Department.objects.get(id=request.POST.get('Department_id'))
        except Department.DoesNotExist:
            return JsonResponse({'status': 'Department not found'})
        doctor = Doctors_Detail.objects.create(
            Name=request.POST.get('Name'),
            Age=request.POST.get('Age'),
            Email=request.POST.get('Email'),
            Department_id=department
        )
        doctor.save()
        return redirect('/api/v1/accounts/doctors/')
    else:
        return render(request, 'signupd.html')
    
def Logout_user(request):
    logout(request)
    return JsonResponse({'status': 'Logout successful'})