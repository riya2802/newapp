# Generated by Django 2.2.2 on 2019-07-02 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employeeDetails', '0019_auto_20190701_0147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='mobile',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]
