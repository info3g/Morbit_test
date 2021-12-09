from django.db import models

# Create your models here.
class Student(models.Model):
    id = models.IntegerField(primary_key = True)
    name = models.CharField(max_length=100)
    rollno = models.IntegerField()
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name