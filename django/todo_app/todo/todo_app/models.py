from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200, null=False)
    description = models.TextField(null=True)
    is_completed = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return f"{self.title} - {self.is_completed}"
    