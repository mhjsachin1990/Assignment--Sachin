# Generated by Django 4.1 on 2022-08-31 11:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentmodels',
            old_name='firstname',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='studentmodels',
            old_name='lastname',
            new_name='last_name',
        ),
    ]
