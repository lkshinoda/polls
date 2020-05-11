from django.shortcuts import render
from django.http import HttpResponse
from django import template
from .models import Question, Test, Poll
from django.views import generic

from .models import Poll


def indexpage(request):
    client_ip = request.META['REMOTE_ADDR']

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
    polls = Poll.objects.all()
    return render(
        request, 
        'polls/polls.html', 
        {
            'polls':polls,
            'header':'Список опросов',
            }
    )