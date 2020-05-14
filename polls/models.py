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
    
    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Test(models.Model):
    question = models.ManyToManyField('polls.Question')
    title = models.CharField('Заголовок теста', max_length=255)
    slug = models.SlugField()
    description = models.TextField('Описание теста', max_length=2000)
    active = models.BooleanField()
    admin_comment = models.CharField('Комментарий адмиристратора', max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'


class Poll(models.Model):
    test = models.ManyToManyField('polls.Test')
    title = models.CharField('Заголовок', max_length=255)
    slug = models.SlugField()
    description = models.TextField('Описание', max_length=2000)
    active = models.BooleanField()
    admin_comment = models.CharField('Комментарий администратора', max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'
