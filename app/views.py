from django.core.paginator import Paginator
from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.views.generic import ListView

from . import models
from .models import QUESTIONS


def loged(request):
    context = {'questions': models.QUESTIONS, 'tags': models.TAGS}
    return render(request, 'index.html', context=context)


def mainpage(request):
    contact_list = models.QUESTIONS
    context = {'questions': models.QUESTIONS, 'tags': models.TAGS, 'page_obj': pagging(contact_list, request)}
    return render(request, 'index1.html', context=context)


def tagpage(request, tag_id: int):
    contact_list = models.QUESTIONS
    context = {'questions': models.QUESTIONS, 'tags': models.TAGS, 'query': models.TAGS[tag_id], 'page_obj':pagging(contact_list, request)}
    return render(request, 'index2.html', context=context)


def settings(request):
    context = {'tags': models.TAGS}
    return render(request, 'index3.html', context=context)


def login(request):
    context = {'tags': models.TAGS}
    return render(request, 'index4.html', context=context)


def signup(request):
    context = {'tags': models.TAGS}
    return render(request, 'index5.html', context=context)


def ask(request):
    context = {'tags': models.TAGS}
    return render(request, 'index6.html', context=context)


def question(request, question_id: int):
    contact_list = models.ANSWERS
    context = {'question': models.QUESTIONS[question_id], 'answers': models.ANSWERS, 'tags': models.TAGS,
               'page_obj': pagging(contact_list, request)}
    return render(request, 'index7.html', context=context)


def hot(request):
    contact_list = models.HOTQUESTIONS
    context = {'questions': models.HOTQUESTIONS, 'tags': models.TAGS, 'page_obj': pagging(contact_list, request)}
    return render(request, 'index8.html', context=context)


def pagging(contact_list, request):
    paginator = Paginator(contact_list, 3)
    page_number = request.GET.get('page')
    #if int(page_number) > paginator.num_pages: raise Http404
    return paginator.get_page(page_number)
