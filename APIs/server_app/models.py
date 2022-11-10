from django.db import models

# Create your models here.
#Staff Model
class Staff(models.Model):
    Staff_id = models.AutoField(primary_key=True)
    Name= models.CharField(max_length=75)
    Email=models.EmailField(null=False,blank=False,unique=True)
    Phone_Number:models.BigIntegerField(null=False,blank=False,unique=True)
    Designation=models.CharField(max_length=100)
    isActive=models.BooleanField(default=True)
    Password=models.CharField(null=False,blank=False,max_length=20)

    def __str__(self):
        return self.Name

class Student(models.Model):
    Student_id = models.AutoField(primary_key=True)
    Name= models.CharField(max_length=75)
    Email=models.EmailField(null=False,blank=False,unique=True)
    Field_of_study=models.CharField(max_length=100)
    isActive=models.BooleanField(default=True)
    Password=models.CharField(null=False,blank=False,max_length=20)

    def __str__(self):
        return self.Name

class Course(models.Model):
    Course_id = models.AutoField(primary_key=True)
    