from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

class CustomUser(AbstractUser):
    is_author = models.BooleanField(default=False)
    is_reviewer = models.BooleanField(default=False)

class Paper(models.Model):
    title = models.CharField(max_length=255)
    abstract = models.TextField()
    keywords = models.CharField(max_length=255)
    pdf = models.FileField(upload_to='papers/')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    submission_date = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)

class Review(models.Model):
    paper = models.ForeignKey(Paper, on_delete=models.CASCADE)
    reviewer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    feedback = models.TextField()
    score = models.IntegerField()
    date_reviewed = models.DateTimeField(auto_now_add=True)
