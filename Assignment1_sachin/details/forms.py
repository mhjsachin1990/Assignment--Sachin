from django import forms


class Students(forms.Form):
    first_name = forms.CharField(error_messages={'required':'Enter your name'})
    last_name = forms.CharField()
    dob = forms.DateField()
    roll_number = forms.IntegerField()
    department_name = forms.CharField()
    course_name = forms.CharField()
    semester_number = forms.IntegerField()


class Department(forms.Form):
    department_name = forms.CharField()
    course_number = forms.IntegerField()
    teacher_number = forms.IntegerField()
