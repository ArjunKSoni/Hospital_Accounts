from django.db import models
from auth_user.models import Doctors_Detail, Patients_Detail, Department

#Records Model
class Patients_Record(models.Model):
    record_id = models.AutoField(primary_key=True, unique=True) 
    Patient_id = models.ForeignKey(Patients_Detail, on_delete=models.CASCADE, null=False, default=0)
    Doctor_id = models.ForeignKey(Doctors_Detail, on_delete=models.CASCADE, null=False, default=0)
    Created_date = models.CharField(max_length=50)
    Diagnostics = models.CharField(max_length=50)
    Observations = models.CharField(max_length=50)
    Treatments = models.CharField(max_length=50)
    Department_id = models.ForeignKey(Department, on_delete=models.CASCADE)
    Misc = models.CharField(max_length=200, blank=True)
    
    def __str__(self):
        return "Patient id: " + str(self.Patient_id) + ", " + "Record id: " + str(self.record_id)

