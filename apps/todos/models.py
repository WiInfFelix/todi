from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Todo(models.Model):

    text = models.TextField(max_length=1024)
    status = models.BooleanField()

    created_at = models.DateTimeField(auto_now_add=True)
    
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey("projects.Project", blank = True, null = True, on_delete=models.CASCADE)