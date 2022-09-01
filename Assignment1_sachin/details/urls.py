from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('details/', views.details, name='details'),
    path('details/students/', views.students, name='students'),
    path('details/students/add_students/', views.add_students, name='add_students'),
    path('details/students/add_students/add_students_record/', views.add_students_record, name='add_students_record'),
    path('details/students/update_students/<int:id>', views.update_students, name='update_students'),
    path('details/students/update_students/update_students_record/<int:id>', views.update_students_record, name='update_students_record'),
    path('details/students/delete_students/<int:id>', views.delete_students, name='delete_students'),

    #   >>> Department  <<<
    path('details/department/', views.department, name='department'),
    path('details/department/add_department/',views.add_department, name='add_department'),
    path('details/department/add_department/add_department_record/', views.add_department_record, name='add_department_record'),
    path('details/department/update_department/<int:id>', views.update_department,name='update_department'),
    path('details/department/update_department/update_department_record/<int:id>', views.update_department_record, name='update_department_record'),
    path('details/department/delete_department/<int:id>', views.delete_department, name='delete_department')

]
