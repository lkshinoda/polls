from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib import admin

class Question(models.Model):
    question_text = models.CharField('Вопрос', max_length=255)
    active = models.BinaryField()
    true_answer = models.CharField('Правильный ответ', max_length=50)

    def __str__(self):
        return self.question_text

class Test(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    title = models.CharField('Заголовок теста', max_length=255)
    slug = models.SlugField()
    description = models.TextField('Описание теста', max_length=2000)
    active = models.BooleanField()
    admin_comment = models.CharField('Комментарий адмиристратора', max_length=255)

    def __str__(self):
        return self.title

class Poll(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    title = models.CharField('Заголовок', max_length=255)
    slug = models.SlugField()
    description = models.TextField('Описание', max_length=2000)
    active = models.BooleanField()
    admin_comment = models.CharField('Комментарий администратора', max_length=255)

    def __str__(self):
        return self.title

