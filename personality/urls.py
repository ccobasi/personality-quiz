from django.urls import path

from . import views
from .views import *


urlpatterns = [
    path('', Quiz.as_view(), name='quiz'),
    path('q/<str:topic>/', QuizQuestion.as_view(), name='questions')
]
