from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify


class Quiz(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('Quiz name'))
    description = models.CharField(max_length=100, verbose_name=_('Description'))
    slug = models.SlugField(blank=True)
    roll_out = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['timestamp']
        verbose_name = _('Quiz')
        verbose_name_plural = _('Quizzes')

    def __str__(self):
        return self.name


class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    label = models.CharField(max_length=100, verbose_name=_('Question text'))
    order = models.IntegerField(default=0, verbose_name=_('Order'))

    class Meta:
        verbose_name = _('Question')
        verbose_name_plural = _('Questions')

    def __str__(self):
        return self.label


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    label = models.CharField(max_length=100, verbose_name=_('Answer text'))
    is_correct = models.BooleanField(default=False, verbose_name=_('Correct answer'))

    class Meta:
        verbose_name = _('Answer')
        verbose_name_plural = _('Answers')

    def __str__(self):
        return self.label


class QuizTaker(models.Model):
    quiz_taker = models.CharField(max_length=100, verbose_name=_('Employee'))
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, verbose_name=_('Quiz'))
    score = models.IntegerField(default=0)
    competed = models.BooleanField(default=False, verbose_name=_('Competed'))
    date_finished = models.DateTimeField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _('Employee')
        verbose_name_plural = _('Employees')

    def __str__(self):
        return self.quiz_taker


class UserAnswer(models.Model):
    quiz_taker = models.ForeignKey(QuizTaker, on_delete=models.CASCADE, verbose_name=_('Quiz taker'))
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name=_('Question'))
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, verbose_name=_('Answer'))

    class Meta:
        verbose_name = _('User answer')
        verbose_name_plural = _('User answers')

    def __str__(self):
        return self.question.label


@receiver(pre_save, sender=Quiz)
def slugify_name(sender, instance, *args, **kwargs):
    instance.slug = slugify(instance.name)