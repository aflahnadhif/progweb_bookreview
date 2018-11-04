from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User

# Create your models here.

class Book(models.Model):
    bookname = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publishedyear = models.DateTimeField('date published')
    description = models.CharField(max_length=200)
    def __str__(self):
        return self.bookname

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    def __str__(self):
        return self.description

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['description']

