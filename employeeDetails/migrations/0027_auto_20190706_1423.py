# Generated by Django 2.2.2 on 2019-07-06 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employeeDetails', '0026_auto_20190706_1151'),
    ]

    operations = [
        migrations.CreateModel(
            name='bloodGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bg', models.CharField(max_length=30)),
            ],
        ),
        migrations.RenameField(
            model_name='linemanager',
            old_name='lineManagerList',
            new_name='lineManager',
        ),
    ]