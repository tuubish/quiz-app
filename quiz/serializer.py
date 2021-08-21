from quiz.models import Quiz, Question, Answer, QuizTaker, UserAnswer
from rest_framework import serializers


class QuizSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Quiz
        fields = ['id', 'name', 'description', 'slug', 'roll_out', 'timestamp']


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'quiz', 'label', 'order']


class AnswerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'question', 'label', 'is_correct']


class QuizTakerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = QuizTaker
        fields = ['id', 'quiz_taker', 'quiz', 'score', 'competed', 'date_finished', 'timestamp']


class UserAnswerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserAnswer
        fields = ['id', 'quiz_taker', 'question', 'answer']