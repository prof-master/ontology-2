from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Ontology(models.Model):
    ACCESS_CHOICES=[
        ('Global', 'Общедоступная'),
        ('Private', 'Приватная'),
        ]
    name=models.CharField(max_length=100, verbose_name=('Наименование онтологии'))
    access=models.CharField(
        max_length=50,
        choices=ACCESS_CHOICES,
        default='Global',
        verbose_name=('Доступность')
        )
    created_at = models.DateTimeField(default=timezone.now, verbose_name=('Дата создания'))
    owner=models.ForeignKey(
        User,
        related_name='ontology',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=('Владелец')
        )
    

    def __str__(self):
        return self.name

class Subject(models.Model):
    name=models.CharField(max_length=100)
    uri=models.CharField(max_length=100)
    description=models.TextField()
    created_at=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.uri
class Object(models.Model):
    name=models.CharField(max_length=100)
    uri=models.CharField(max_length=100)
    description=models.TextField()
    created_at=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.uri
class rdf_type(models.Model):
    name=models.CharField(max_length=100)
    uri=models.CharField(max_length=100)
    description=models.TextField()
    created_at=models.DateTimeField(default=timezone.now)
    ontology=models.ForeignKey(
        Ontology,
        related_name='ontology',
        on_delete=models.CASCADE
        )
    subject=models.ForeignKey(
        Subject,
        related_name='ontology',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
        )
    object=models.ForeignKey(
        Object,
        related_name='ontology',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
        )
    def __str__(self):
        return self.uri


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title