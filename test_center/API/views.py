from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import EnglishTest, Attempt, Student
from django.db import transaction, DatabaseError
from django.core.exceptions import ObjectDoesNotExist

import json
# Create your views here.


@api_view(['POST'])
@transaction.atomic
def answer_list(request):
    if request.method == 'POST':
        score = 0
        request_body = json.loads(request.body)
        try:
            student = Student.objects.get(name=request_body['name'])
        except ObjectDoesNotExist:
            return Response({'validation': 'incorrect', 'body': 'wrong name or id'})
        if student.identifier != request_body['id']:
            return Response({'validation': 'incorrect', 'body': 'wrong name or id'})
        try:
            test = EnglishTest.objects.get(name=request_body['test'])
        except ObjectDoesNotExist:
            return Response({'validation': 'incorrect', 'body': 'wrong test name'})
        test_answer = test.solution_string
        student_answer = request_body['answer']
        for answer, correction in zip(student_answer, test_answer):
            if answer == correction:
                score += 1
        attempt = Attempt.objects.create(score=score, test=test.name, student=student.name)
        attempt.save()
        return Response({'validation': 'correct', 'score': score, 'test_answer': test.solution_string})


@api_view(['POST'])
def authentication(request):
    if request.method == 'POST':
        request_body = json.loads(request.body)
        try:
            student = Student.objects.get(name=request_body['name'])
        except ObjectDoesNotExist:
            return Response({'validation': 'incorrect', 'body': 'wrong name or id'})
        if student.identifier != request_body['id']:
            return Response({'validation': 'incorrect', 'body': 'wrong name or id'})
        try:
            test = EnglishTest.objects.get(name=request_body['test'])
        except ObjectDoesNotExist:
            return Response({'validation': 'incorrect', 'body': 'wrong test name'})
        return Response({'validation': 'correct', 'body': test.test_body})

