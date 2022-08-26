from unicodedata import category
from .models import *
from rest_framework import generics
from rest_framework.response import Response
from .serializers import *
from rest_framework.views import APIView


class Quiz(generics.ListAPIView):

    serializer_class = QuizSerializer
    queryset = Quizzes.objects.all()


# class StartQuiz(APIView):

#     def get(self, request, **kwargs):
#         quiz = Quizzes.objects.filter(category__name=kwargs['title'])
#         serializer = QuizSerializer(quiz, many=True)
#         return Response(serializer.data)


class QuizList(APIView):
    def get(self, request, format=None):
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)


class RandomQuestion(APIView):

    def get(self, request, format=None, **kwargs):
        question = Question.objects.filter(
            quiz__title=kwargs['topic']).order_by('?')[:1]
        serializer = RandomQuestionSerializer(question, many=True)
        return Response(serializer.data)


class QuizQuestion(APIView):

    def get(self, request, format=None, **kwargs):
        quiz = Question.objects.filter(
            quiz__title=kwargs['topic']).order_by('?')[:1]
        serializer = QuestionSerializer(quiz, many=True)
        return Response(serializer.data)
