from django.db import models

# Create your models here.
class Question(models.Model):
    text = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    difficulty = models.IntegerField()

    def __str__(self):
        return self.text
