from django.core.paginator import Paginator
from django.http import HttpResponse, Http404, HttpResponseBadRequest
from django.shortcuts import render
from django.views.generic import ListView
from . import models


def loged(request):
    context = {'questions': models.QUESTIONS, 'tags': models.TAGS}
    return render(request, 'index.html', context=context)


def mainpage(request):
    contact_list = models.Question.objects.get_new_questions()
    context = {'questions': models.Question, 'tags': models.Tag,
               'page_obj': pagging(contact_list, request), 'profiles': models.Profile, 'likes': models.LikeQuestion}
    return render(request, 'index1.html', context=context)


def question(request, question_id: int):
    contact_list = models.Answer.objects.get_answers(question_id)
    context = {'question': models.Question.objects.find_by_id(question_id), 'answers': models.Answer,
               'tags': models.Tag,
               'page_obj': pagging(contact_list, request)}
    return render(request, 'index7.html', context=context)


def tagpage(request, tag_id: int):
    contact_list = models.Question.objects.get_tagged_questions(tag_id)
    context = {'questions': models.Question, 'tags': models.Tag, 'tag': models.Tag.objects.find_by_id(tag_id),
               'page_obj': pagging(contact_list, request)}
    return render(request, 'index2.html', context=context)


def hot(request):
    contact_list = models.Question.objects.get_hot_questions()
    context = {'questions': models.Question, 'tags': models.Tag, 'page_obj': pagging(contact_list, request)}
    return render(request, 'index8.html', context=context)


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


def pagging(contact_list, request):
    paginator = Paginator(contact_list, 3)
    page_number = request.GET.get('page', 1)
    try:
        page = int(page_number)
        if page > paginator.num_pages: raise Http404
    except ValueError:
        return HttpResponseBadRequest()
    return paginator.get_page(page_number)


def likes(question_like, answer_like):
    likes_count = {'questions': models.Like.objects.get_questions_likes(question_like),
                   'answers': models.Like.objects.get_answers_likes(answer_like)}
    return likes_count
