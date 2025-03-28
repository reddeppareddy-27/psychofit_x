from django.db import models

class YogaPlan(models.Model):
    day = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    Yoga= models.TextField()
    

    def __str__(self):
        return self.day