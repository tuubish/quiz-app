from quiz.serializer import QuizSerializer, QuestionSerializer, AnswerSerializer, QuizTakerSerializer, \
    UserAnswerSerializer
from quiz.models import Quiz, Question, Answer, QuizTaker, UserAnswer
from rest_framework import viewsets
from rest_framework.response import Response


class QuizListAPIView(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer


class QuestionListAPIView(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class AnswerAPIView(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class QuizTakerAPIView(viewsets.ModelViewSet):
    queryset = QuizTaker.objects.all()
    serializer_class = QuizTakerSerializer


class UserAnswerAPIView(viewsets.ModelViewSet):
    queryset = UserAnswer.objects.all()
    serializer_class = UserAnswerSerializer