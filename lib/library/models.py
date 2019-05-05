from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from itsdangerous import TimedJSONWebSignatureSerializer as Seria
# Create your models here.


class Student(User):
    collage = models.CharField(max_length=255, null=True, blank=True)
    num = models.IntegerField(null=True, blank=True)


class Book(models.Model):
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publish_com = models.CharField(max_length=255)
    publish_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class History(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_borrow = models.DateTimeField(auto_now_add=True)
    date_return = models.DateTimeField(blank=True, null=True)
    statue = models.BooleanField()


class Pic(models.Model):
    name = models.CharField(max_length=20)
    img = models.ImageField(upload_to='pic')
    index = models.SmallIntegerField(unique=True)

    def __str__(self):
        return self.name


class Message(models.Model):
    name = models.CharField(max_length=20)
    content = HTMLField()

    def __str__(self):
        return self.name
