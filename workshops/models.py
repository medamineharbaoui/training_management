# workshops/models.py
from django.db import models
from users.models import User

class Workshop(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    trainer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, limit_choices_to={'role':'trainer'})

    def __str__(self):
        return self.title
