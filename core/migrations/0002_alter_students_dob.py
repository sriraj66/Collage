# Generated by Django 4.0.3 on 2022-03-13 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='dob',
            field=models.DateField(),
        ),
    ]