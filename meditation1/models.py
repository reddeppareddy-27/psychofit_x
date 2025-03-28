from django.db import models

class MeditationPlan(models.Model):
    day = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    Meditation= models.TextField()
    

    def __str__(self):
        return self.day