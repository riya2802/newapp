# Generated by Django 2.2.2 on 2019-07-06 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employeeDetails', '0027_auto_20190706_1423'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bloodgroup',
            old_name='bg',
            new_name='bloodgroup',
        ),
    ]
