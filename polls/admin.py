from django.contrib import admin

from .models import Question, Poll, Test

admin.site.register(Question)
admin.site.register(Test)
admin.site.register(Poll)