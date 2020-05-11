from django.urls import path
from . import views

app_name = ''
urlpatterns = [
    path('', views.indexpage),
    path('poll/', views.poll),
]