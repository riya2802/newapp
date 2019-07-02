# Generated by Django 2.2.2 on 2019-06-29 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employeeDetails', '0013_auto_20190628_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=55, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='employeefamily',
            name='employeeFamilyNumberOfChild',
            field=models.CharField(default='0', max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='leaveWorkflow',
            field=models.CharField(max_length=30, null=True),
        ),
    ]