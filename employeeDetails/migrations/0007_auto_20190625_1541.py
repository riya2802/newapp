# Generated by Django 2.2.2 on 2019-06-25 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employeeDetails', '0006_employeechildren_employeefamily_employeehealth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeefamily',
            name='employeeFamilySpouseBirthDate',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='employeefamily',
            name='employeeFamilySpouseNationalId',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='employeefamily',
            name='employeeFamilySpousePassport',
            field=models.IntegerField(null=True),
        ),
    ]