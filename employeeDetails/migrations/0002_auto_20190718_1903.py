# Generated by Django 2.2.2 on 2019-07-18 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employeeDetails', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='employeeGender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('U', 'Unknown')], max_length=15),
        ),
    ]
