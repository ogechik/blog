from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_published = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

