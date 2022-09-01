from django.shortcuts import render
from .forms import Students, Department
from django.http import HttpResponse
from .models import StudentModels, DepartmentModels
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from datetime import date

def home(request):
    return render(request, 'home.html')


def details(request):
    return render(request, 'details.html')


def students(request):
    students_querySet = StudentModels.objects.all() #for getting specific using pk-objects.get(pk=1) and remove for loop
    today = date.today()
    for i in students_querySet:
        i.age = today.year - i.dob.year - ((today.month, today.day) < (i.dob.month, i.dob.day))
        a = StudentModels.objects.get(pk=i.id)
        # a.age = i['age']
        a.save()
    return render(request, 'students.html', {'students': students_querySet})


def add_students(request):
    students_obj = Students(initial={'dob':'YYYY-MM-DD'})
    return render(request, 'add_students.html', {'add_students': students_obj})


def add_students_record(request):
    a = request.POST['first_name']
    b = request.POST['last_name']
    c = request.POST['dob']
    d = request.POST['roll_number']
    e = request.POST['department_name']
    f = request.POST['course_name']
    g = request.POST['semester_number']
    students = StudentModels(first_name=a, last_name=b, dob=c, roll_number=d, department_name=e, course_name=f,
                       semester_number=g)
    students.save()
    return HttpResponseRedirect(reverse('students'))

def update_students(request,id):
    students_querySet=StudentModels.objects.get(id=id)
    return render(request,'update_students.html',{'students':students_querySet})

def update_students_record(request,id):
    a = request.POST['first_name']
    b = request.POST['last_name']
    c = request.POST['dob']
    d = request.POST['roll_number']
    e = request.POST['department_name']
    f = request.POST['course_name']
    g = request.POST['semester_number']
    students = StudentModels.objects.get(id=id)
    students.first_name = a
    students.last_name = b
    students.dob = c
    students.roll_number = d
    students.department_name = e
    students.course_name = f
    students.semester_number = g
    students.save()
    return HttpResponseRedirect(reverse('students'))

def delete_students(request,id):
    students=StudentModels.objects.get(id=id)
    students.delete()
    return HttpResponseRedirect(reverse('students'))

"""       >>>>>> ***** DEPARTMENT ******* <<<<<<     """

def department(request):
    dept_querySet=DepartmentModels.objects.all().values()
    return render(request,'department.html',{'department':dept_querySet})

def add_department(request):
    dept_obj= Department()
    return render(request,'add_department.html',{'add_department':dept_obj})

def add_department_record(request):
    a = request.POST['department_name']
    b = request.POST['course_number']
    c = request.POST['teacher_number']
    dept = DepartmentModels(department_name=a, course_number=b, teacher_number=c)
    dept.save()
    return HttpResponseRedirect(reverse('department'))

def update_department(request,id):
    dept=DepartmentModels.objects.get(id=id)
    return render(request,'update_department.html',{'department':dept})

def update_department_record(request,id):
    a = request.POST['department_name']
    b = request.POST['course_number']
    c = request.POST['teacher_number']
    dept = DepartmentModels.objects.get(id=id)
    dept.department_name = a
    dept.course_number = b
    dept.teacher_number = c
    dept.save()
    return HttpResponseRedirect(reverse('department'))

def delete_department(request,id):
    dept=DepartmentModels.objects.get(id=id)
    dept.delete()
    return HttpResponseRedirect(reverse('department'))