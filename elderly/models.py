from django.db import models

# Create your models here.
class doctor(models.Model):
 name=models.AutoField(primary_key=True)
 age=models.IntegerField()
 experience=models.IntegerField()
 speciality=models.CharField(max_length=15)
 id=models.IntegerField()
 location=models.CharField(max_length=15)

class health_reporte(models.Model):
 bpm=models.IntegerField()
 spo_2=models.IntegerField()
 temperature=models.IntegerField()
 ecg=models.CharField(max_length=15)

class preciption(models.Model):
  id=models.AutoField(primary_key=True)
  patien_id=models.IntegerField()
  medecine=models.CharField(max_length=15)
  reason=models.CharField(max_length=15)
  Time_medication=models.CharField(max_length=15)

class patients(models.Model):
   id=models.AutoField(primary_key=True)
   name=models.CharField(max_length=15)
   age=models.IntegerField()
   medical_history=models.CharField(max_length=15)
   allarges=models.CharField(max_length=15)
   health_status=models.BooleanField()
   mental_health=models.BooleanField()