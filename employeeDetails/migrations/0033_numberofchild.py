# Generated by Django 2.2.2 on 2019-07-08 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employeeDetails', '0032_delete_numberofchild'),
    ]

    operations = [
        migrations.CreateModel(
            name='numberOfChild',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numberOfchild', models.CharField(max_length=30)),
            ],
        ),
    ]
