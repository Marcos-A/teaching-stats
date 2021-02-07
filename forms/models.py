from django.db import models

# Create your models here.

class Evaluation(models.Model):
    timestamp = models.CharField(max_length=19)
    level = models.CharField(max_length=25)
    classgroup = models.CharField(max_length=10, null=True)
    item1 = models.IntegerField()
    item2 = models.IntegerField()
    item3 = models.IntegerField()
    item4 = models.IntegerField()
    item5 = models.IntegerField()
    opinion = models.CharField(max_length=280, null=True)


class EnrolledStudent(models.Model):
    email = models.EmailField(max_length=75, unique=True)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    level = models.CharField(max_length=25)
    classgroup = models.CharField(max_length=10, null=True)


class StudentEvaluation(models.Model):
    email = models.EmailField(max_length=75, unique=True)
    evaluation_timestamp = models.CharField(max_length=19, null=True)
