# Generated by Django 2.2.2 on 2019-07-06 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employeeDetails', '0024_auto_20190706_1058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(blank=True, max_length=55, null=True, unique=True),
        ),
    ]