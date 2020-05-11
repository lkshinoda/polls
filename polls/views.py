from django.shortcuts import render
from django.http import HttpResponse
from django import template
from .models import Question, Test, Poll
from django.views import generic
from datetime import datetime

from .models import Poll


def indexpage(request):
    client_ip = request.META['REMOTE_ADDR']
    clock = datetime.now()

    return render(
        request,
        'polls/index.html',
        {
            'header':'Заголовок основой странички',
            'body':'Тело основной странички',
            'ip': client_ip,
            'time':clock,
        }
    )

def poll(request):
    tests = Test.objects.all()
    polls = Poll.objects.all()
    return render(
        request, 
        'polls/polls.html', 
        {
            'header':'Список опросов',
            'polls':polls,
            'tests':tests,
            }
    )