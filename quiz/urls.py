from django.urls import path
from django.contrib.auth.decorators import login_required
from .views  import HomeView, QuizView

# from quiz.api import QuizListAPIView, QuestionListAPIView, AnswerAPIView, QuizTakerAPIView, UserAnswerAPIView

# from rest_framework import routers

urlpatterns = [
    path('', HomeView.as_view(), name='home_page'),
    path("quiz/<int:quiz_id>", QuizView.as_view(), name="quiz"),
]

# router = routers.DefaultRouter()
# router.register(r'quiz', QuizListAPIView)
# router.register(r'question', QuestionListAPIView)
# router.register(r'answer', AnswerAPIView)
# router.register(r'employee', QuizTakerAPIView)
# router.register(r'user-answers', UserAnswerAPIView)
#
# urlpatterns = router.urls
