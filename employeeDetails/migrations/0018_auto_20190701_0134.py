# Generated by Django 2.2.2 on 2019-06-30 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employeeDetails', '0017_auto_20190701_0116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='housePhone',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='mobile',
            field=models.IntegerField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='mobilePhone',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='officePhone',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='postCode',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]