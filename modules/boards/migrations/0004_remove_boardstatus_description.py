# Generated by Django 5.1 on 2024-12-06 11:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0003_boardstatus'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='boardstatus',
            name='description',
        ),
    ]