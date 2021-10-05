from django.shortcuts import render
from django.views.generic import TemplateView

from quiz.models import Quiz, Question, Answer, QuizTaker, UserAnswer


class HomeView(TemplateView):

    def dispatch(self, request, *args, **kwargs):
        quizzes = Quiz.objects.all()
        return render(request, template_name='quiz/main.html', context={
            'quizzes': quizzes
        })


class QuizView(TemplateView):
    template_name = "quiz/quiz.html"

    def get_context_data(self, **kwargs):
        quiz_id = kwargs["quiz_id"]
        quiz = Quiz.objects.get(id=quiz_id)

        return {
            'quiz': quiz
        }
