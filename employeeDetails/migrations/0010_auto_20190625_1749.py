# Generated by Django 2.2.2 on 2019-06-25 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employeeDetails', '0009_auto_20190625_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeechildren',
            name='employeeChildrenGender',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('U', 'Unknown')], default='U', max_length=1, null=True),
        ),
    ]
