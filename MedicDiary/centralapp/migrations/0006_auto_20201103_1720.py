# Generated by Django 3.1.1 on 2020-11-03 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('centralapp', '0005_auto_20201021_1435'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctorprofile',
            name='user',
        ),
        migrations.RemoveField(
            model_name='patientprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='PatientVitals',
        ),
        migrations.DeleteModel(
            name='DoctorProfile',
        ),
        migrations.DeleteModel(
            name='PatientProfile',
        ),
    ]