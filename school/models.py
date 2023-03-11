from django.db import models

# Create your models here.
class Section(models.Model):
    label = models.CharField(max_length=50)
    description = models.TextField()

class Subject(models.Model):
    label = models.CharField(max_length=50)
    description = models.TextField()
    section = models.ForeignKey(Section, on_delete=models.SET_NULL,null=True)

class Prof(models.Model):
    full_name = models.CharField(max_length=50)
    CIN = models.CharField(max_length=10)
    salaire = models.FloatField()
    subject = models.OneToOneField(Subject, on_delete=models.CASCADE)
    
class Student(models.Model):
    full_name = models.CharField(max_length=50)
    massar_code = models.CharField(max_length=20)
    section = models.ForeignKey(Section, on_delete=models.SET_NULL,null=True)

class Exam(models.Model):
    season = models.CharField(max_length=20)
    exam_date = models.DateField()
    observation = models.TextField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

class Mark(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    attendence = models.BooleanField(default=True)
    note = models.FloatField()
