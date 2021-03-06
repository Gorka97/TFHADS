"""
AQUI VAN LAS "CLASES"
"""

from django.db import models
from django.db.models.fields import CharField,BooleanField

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

TOPICS = (
    ('Los_de_atras','LosDeAtras'),
    ('HADS','HADS'),
    ('SW', 'SW'),
    ('IS','IS'),   
)
class QuizQuestion(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    topic = models.CharField(max_length=18, choices=TOPICS, default='LosDeAtras')

class QuizChoice(models.Model):
    question = models.ForeignKey(QuizQuestion)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    correctAnswer = models.BooleanField(default=False)

class User(models.Model):
    email = models.CharField(max_length=200)
    nombre = models.CharField(max_length=200)

