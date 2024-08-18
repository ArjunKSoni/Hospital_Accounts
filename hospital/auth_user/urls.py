from django.contrib import admin
from django.urls import path, include
from auth_user.views import Login_user, Signup_P, Signup_D, Logout_user

urlpatterns = [
    path("", Login_user, name='Login_user'),
    path("signup_patient/", Signup_P, name='Signup_P'),
    path('signup_doctor/', Signup_D, name='Signup_D'),
    path("logout", Logout_user, name='Logout_user'),
]
