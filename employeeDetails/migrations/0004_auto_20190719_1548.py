# Generated by Django 2.2.2 on 2019-07-19 10:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employeeDetails', '0003_auto_20190719_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeechildren',
            name='employeeForeignId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employeeDetails.employee'),
        ),
    ]
