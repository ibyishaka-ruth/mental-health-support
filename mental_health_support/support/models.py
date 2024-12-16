from django.db import models
from django.contrib.auth.models import User

class Testimony(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

class Photo(models.Model):  
    url = models.URLField()
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

class AISupport(models.Model):  
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    issue_detected = models.TextField()
    suggested_solutions = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

class Session(models.Model):  
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    feedback = models.TextField()

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
