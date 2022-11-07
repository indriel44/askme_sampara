from django.http import HttpResponse
from django.shortcuts import render
from . import models


def loged(request):
    context = {'questions': models.QUESTIONS}
    return render(request, 'index.html', context=context)


def mainpage(request):
    context = {'questions': models.QUESTIONS}
    return render(request, 'index1.html', context=context)


def tagpage(request):
    context = {'questions': models.QUESTIONS}
    return render(request, 'index2.html', context=context)


def settings(request):
    return render(request, 'index3.html')


def login(request):
    return render(request, 'index4.html')


def signup(request):
    return render(request, 'index5.html')


def ask(request):
    return render(request, 'index6.html')


def question(request, question_id: int):
    context = {'question': models.QUESTIONS[question_id], 'answer': models.ANSWERS[question_id]}
    return render(request, 'index7.html', context=context)


def hot(request):
    context = {'questions': models.HOTQUESTIONS}
    return render(request, 'index8.html', context=context)
