from django.contrib import admin
from django.urls import path

from quiz.views import QuizListAPIView, QuestionListAPIView, AnswerAPIView, QuizTakerAPIView, UserAnswerAPIView

from rest_framework import routers

urlpatterns = []

router = routers.DefaultRouter()
router.register(r'quiz', QuizListAPIView)
router.register(r'question', QuestionListAPIView)
router.register(r'answer', AnswerAPIView)
router.register(r'employee', QuizTakerAPIView)
router.register(r'user-answers', UserAnswerAPIView)

urlpatterns = router.urls
