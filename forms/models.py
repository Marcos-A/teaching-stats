from django.db import models


# Create your models here.

class Degree(models.Model):
    short_name = models.CharField(primary_key=True, max_length=4)
    long_name = models.CharField(max_length=75, unique=True)
    department = models.CharField(max_length=50)


class EvaluableItem(models.Model):
    item = models.CharField(primary_key=True, max_length=10)


class Subject(models.Model):
    short_name = models.ForeignKey(EvaluableItem, to_field='item', on_delete=models.CASCADE,
                                   related_name='subject_information_of_subject_short_name')
    long_name = models.CharField(max_length=75, null=True)
    degree = models.ForeignKey(Degree, to_field='short_name', on_delete=models.CASCADE,
                               related_name='subjects_of_degree', null=True)

    class Meta:
        unique_together = ["short_name", "degree"]


class EnrolledStudent(models.Model):
    email = models.EmailField(primary_key=True, max_length=75)
    name = models.CharField(max_length=50, null=True)
    surname = models.CharField(max_length=50, null=True)
    level = models.CharField(max_length=25)
    classgroup = models.CharField(max_length=10, null=True)
    degree = models.ForeignKey(Degree, to_field='short_name', on_delete=models.CASCADE,
                               null=True, related_name='students_of_degree')
    enrolled_subjects = models.CharField(max_length=75, null=True)

    class Meta:
        constraints = [
            models.CheckConstraint(
                name = '%(app_label)s_%(class)s_check_cf_classgroup_not_null',
                check = 
                    ~models.Q(level__iexact='CF') |
                    models.Q(classgroup__isnull=False),
            ),
            models.CheckConstraint(
                name = '%(app_label)s_%(class)s_check_cf_classgroup_contains_course_1_or_2',
                check = 
                    ~models.Q(level__iexact='CF') |
                    (models.Q(classgroup__contains='1') | models.Q(classgroup__contains='2')),
            ),
            models.CheckConstraint(
                name = '%(app_label)s_%(class)s_check_cf_degree_not_null',
                check = 
                    ~models.Q(level__iexact='CF') |
                    models.Q(degree__isnull=False),
            ),
            models.CheckConstraint(
                name = '%(app_label)s_%(class)s_check_cf_enrolled_subjects_not_null',
                check = 
                    ~models.Q(level__iexact='CF') |
                    models.Q(enrolled_subjects__isnull=False),
            )
        ]

class Evaluation(models.Model):
    timestamp = models.CharField(max_length=26)
    subject = models.ForeignKey(EvaluableItem, to_field='item', on_delete=models.CASCADE,
                                   related_name='evaluation_of_subject')
    level = models.CharField(max_length=25, null=True)
    classgroup = models.CharField(max_length=10, null=True)
    degree = models.ForeignKey(Degree, to_field='short_name', on_delete=models.CASCADE,
                               null=True, related_name='evaluations_of_degree')
    question1 = models.IntegerField()
    question2 = models.IntegerField()
    question3 = models.IntegerField()
    question4 = models.IntegerField(null=True)
    question5 = models.IntegerField(null=True)
    question6 = models.IntegerField(null=True)
    opinion = models.CharField(max_length=280, null=True)

    class Meta:
        constraints = [
            models.CheckConstraint(
                name = '%(app_label)s_%(class)s_check_cf_degree',
                check = 
                    ~models.Q(level__iexact='CF') |
                    models.Q(degree__isnull=False),
            )
        ]


class StudentEvaluation(models.Model):
    email = models.ForeignKey(EnrolledStudent, to_field='email', on_delete=models.CASCADE,
                              related_name='student_evaluations')
    evaluation_timestamp = models.CharField(max_length=26, null=True)
