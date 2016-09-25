from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.
class Qusetions(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Qusetions, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    voted = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
