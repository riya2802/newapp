# Generated by Django 2.2.2 on 2019-07-08 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employeeDetails', '0030_auto_20190708_0306'),
    ]

    operations = [
        migrations.CreateModel(
            name='maritalStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Maritalstatus', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='numberOfChild',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numberOfChild', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='employee',
            name='employeeEthnicity',
            field=models.CharField(blank=True, default='NA', max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='employeeReligion',
            field=models.CharField(blank=True, default='NA', max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='employeechildren',
            name='employeeChildrenMaritalStatus',
            field=models.CharField(default='Unmarried', max_length=1),
        ),
        migrations.AlterField(
            model_name='employeefamily',
            name='employeeFamilyMaritalStatus',
            field=models.CharField(default='Unmarried', max_length=15),
        ),
        migrations.AlterField(
            model_name='employeefamily',
            name='employeeFamilySpouseEthnicity',
            field=models.CharField(blank=True, default='NA', max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='employeefamily',
            name='employeeFamilySpouseReligion',
            field=models.CharField(blank=True, default='NA', max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='employeehealth',
            name='employeeHealthBloodGroup',
            field=models.CharField(blank=True, default="Don't No", max_length=5, null=True),
        ),
    ]
