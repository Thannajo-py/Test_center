from django.db import models


class Student(models.Model):
    name = models.CharField('nom', max_length=200, unique=True)
    identifier = models.CharField('id', max_length=25, unique=True)
    def __str__(self):
        return self.name



class EnglishTest(models.Model):
    name = models.CharField('nom', max_length=200, unique=True)
    solution_string = models.CharField('solution', max_length=200)
    test_body = models.TextField('corps du test', blank=True)
    def __str__(self):
        return self.name



class Attempt(models.Model):
    created_at = models.DateTimeField('date de tentative', auto_now_add=True)
    score = models.IntegerField('score', null=True, blank=True)
    test = models.CharField('nom du test', max_length=200)
    student = models.CharField('étudiant', max_length=200, blank=True, null=True)
