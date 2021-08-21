from django.contrib import admin
from nested_admin import nested
from quiz.models import Quiz, Question, Answer, QuizTaker, UserAnswer


class AnswerInline(nested.NestedTabularInline):
    model = Answer
    extra = 4
    max_num = 4


class QuestionInline(nested.NestedTabularInline):
    model = Question
    inlines = [AnswerInline, ]
    extra = 4


class QuizAdmin(nested.NestedModelAdmin):
    inlines = [QuestionInline, ]


class UserAnswerInline(admin.TabularInline):
    model = UserAnswer


class QuizTakerAdmin(admin.ModelAdmin):
    inlines = [UserAnswerInline, ]


admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(QuizTaker, QuizTakerAdmin)
admin.site.register(UserAnswer)
