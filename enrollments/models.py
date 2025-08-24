# enrollments/models.py
from django.db import models
from users.models import User
from workshops.models import Workshop

class Enrollment(models.Model):
    participant = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role':'participant'})
    workshop = models.ForeignKey(Workshop, on_delete=models.CASCADE)
    enrolled_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('participant', 'workshop')
