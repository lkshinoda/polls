from django.shortcuts import render
from django.http import HttpResponse
from django import template
from .models import Question, Test, Poll
from django.views import generic
from datetime import datetime

from .models import Poll

def get_client_ip(request):
    return request.META['REMOTE_ADDR']

def indexpage(request):
    client_ip = get_client_ip(request)

    return render(
        request,
        'polls/index.html',
        {
            'header':'Заголовок основой странички',
            'body':'Тело основной странички',
            'ip': client_ip,
        }
    )

def poll(request):
    client_ip = get_client_ip(request)
    tests = Test.objects.all()
    polls = Poll.objects.all()
    questions = Question.objects.all()
    return render(
        request, 
        'polls/polls.html', 
        {
            'header':'Список опросов',
            'polls':polls,
            'tests':tests,
            'questions':questions,
            'ip': client_ip,
            }
    )