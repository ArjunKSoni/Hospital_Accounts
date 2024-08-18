from django.db import models
from django.contrib.auth.models import User


#Patients model attributes
class Patients_Detail(models.Model):
    Name = models.CharField(max_length=50)
    Age = models.IntegerField()
    Email =models.EmailField(default="")
    
    def __str__(self):
        return "Patient id: " + str(self.id) + ", " + "Name: " + self.Name

#Docktors model attributes
class Doctors_Detail(models.Model):
    Name = models.CharField(max_length=50)
    Age = models.IntegerField()
    Department_id = models.ForeignKey("Department", on_delete=models.CASCADE)
    Email =models.EmailField(default="")
    
    def __str__(self):
        return "Doctor id: " + str(self.id) + ", " + "Name: " + self.Name
    
#Departments model attributes
class Department(models.Model):
    Name = models.CharField(max_length=50)
    Diagnostics = models.CharField(max_length=50)
    Location = models.CharField(max_length=50)
    Specialization = models.CharField(max_length=50)
    
    def __str__(self):
        return "Department id: " + str(self.id) + ", " + "Name: " + self.Name
    
