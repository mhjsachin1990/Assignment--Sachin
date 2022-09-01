from django.contrib import admin
from .models import StudentModels, DepartmentModels


class StudentModelsAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'dob', 'department_name', 'course_name')


admin.site.register(StudentModels, StudentModelsAdmin)
admin.site.register(DepartmentModels)

