# Generated by Django 4.1 on 2022-08-31 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DepartmentModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(max_length=255)),
                ('course_number', models.IntegerField()),
                ('teacher_number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='StudentModels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=25)),
                ('lastname', models.CharField(max_length=255)),
                ('dob', models.DateField()),
                ('roll_number', models.IntegerField()),
                ('department_name', models.CharField(max_length=255)),
                ('course_name', models.CharField(max_length=255)),
                ('semester_number', models.IntegerField()),
                ('age', models.IntegerField(default=0)),
            ],
        ),
    ]
