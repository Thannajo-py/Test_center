# Generated by Django 3.2 on 2021-05-03 08:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EnglishTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='nom')),
                ('solution_string', models.CharField(max_length=200, verbose_name='solution')),
                ('test_body', models.TextField(blank=True, verbose_name='corps du test')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='nom')),
                ('identifier', models.CharField(max_length=25, unique=True, verbose_name='id')),
                ('score', models.IntegerField(blank=True, null=True, verbose_name='score')),
            ],
        ),
        migrations.CreateModel(
            name='Attempt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='date de tentative')),
                ('score', models.IntegerField(blank=True, null=True, verbose_name='score')),
                ('test', models.CharField(max_length=200, verbose_name='nom du test')),
                ('student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='étudiant', to='API.student', verbose_name='étudiant')),
            ],
        ),
    ]
