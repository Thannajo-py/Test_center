# Generated by Django 3.2 on 2021-05-03 09:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='score',
        ),
    ]