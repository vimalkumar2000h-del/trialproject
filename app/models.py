from django.db import models
# Create your models here.

class Students(models.Model):
    name = models.CharField(max_length=100)
    class_name = models.CharField(max_length=50)
    age = models.IntegerField()
    place = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} - {self.class_name} - {self.age} - {self.place}"
