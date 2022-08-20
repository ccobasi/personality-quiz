from re import template
from django.shortcuts import render
from .models import *
# from django.views.generic import ListView
from django.http import HttpResponse


# class QuizListView(ListView):
#     pass

def index(request):
    html = "<html><body><h1>Hello World</h1></body></html>"
    return HttpResponse(html)
