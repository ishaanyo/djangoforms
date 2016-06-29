from rest_framework import serializers
from .models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES,Question,Options,Album,Track,CustomForm,QuestionAnswer
from django.contrib.auth.models import User


class QuestionAnswerSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        many = kwargs.pop('many', True)
        super(QuestionAnswerSerializer, self).__init__(many=many, *args, **kwargs)
    class Meta:
        model = QuestionAnswer
        fields = ('question', 'question_answer', 'timestamp', 'userid')


class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Options
        fields = ('option_text','stype')


class QuestionSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ('id', 'question_text', 'ftype', 'options')

class CustomFormSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)
    class Meta:
        model = CustomForm
        fields = ('id','form_title','questions')



