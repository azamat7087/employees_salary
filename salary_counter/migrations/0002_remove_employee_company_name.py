# Generated by Django 3.1.6 on 2021-03-27 10:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('salary_counter', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='company_name',
        ),
    ]
