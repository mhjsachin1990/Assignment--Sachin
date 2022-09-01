from django.db import models


class StudentModels(models.Model):
    first_name = models.CharField(max_length=25,)
    last_name = models.CharField(max_length=255)
    dob = models.DateField()
    roll_number = models.IntegerField()
    department_name = models.CharField(max_length=255)
    course_name = models.CharField(max_length=255)
    semester_number = models.IntegerField()
    age = models.IntegerField(default=0)


class DepartmentModels(models.Model):
    department_name = models.CharField(max_length=255)
    course_number = models.IntegerField()
    teacher_number = models.IntegerField()