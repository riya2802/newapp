# Generated by Django 2.2.2 on 2019-06-29 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employeeDetails', '0015_auto_20190629_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='employeeNationalId',
            field=models.IntegerField(),
        ),
    ]
