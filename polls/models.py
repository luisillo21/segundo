from django.db import models

class Question(models.Model):
    id = models.AutoField(primary_key=True)
    question_text = models.CharField(blank=False, null=False, max_length=200)
    pub_date = models.DateField('date published', blank=False, null=False)

class Choice(models.Model):
    id = models.AutoField(primary_key=True)
    choice_text = models.CharField(blank=False, null=False, max_length=200)
    question = models.ForeignKey(Question, on_delete= models.CASCADE)
