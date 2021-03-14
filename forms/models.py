from django.db import models
from django.db.models.base import Model


class Evaluation(models.Model):
    id = models.AutoField(primary_key=True)
    timestamp = models.DateTimeField()
    classgroup_id = models.SmallIntegerField()
    trainer_id = models.SmallIntegerField(null=True)
    subject_id = models.SmallIntegerField()
    level_id = models.SmallIntegerField()

class Answer(models.Model):
    id = models.AutoField(primary_key=True)
    value = models.TextField(null=True)
    question_id = models.SmallIntegerField()
    evaluation = models.ForeignKey(Evaluation,
                                   to_field='id',
                                   on_delete=models.RESTRICT,
                                   related_name='answers_of_evaluation')

class Participation(models.Model):
    id = models.AutoField(primary_key=True)
    timestamp = models.DateTimeField()
    email = models.EmailField(max_length=75, unique=True)
