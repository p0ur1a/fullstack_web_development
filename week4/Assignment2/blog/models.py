from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    date_of_birth = models.DateField()
    enrolled = models.DateField()
    grade = models.IntegerField()
    
    class Meta:
        verbose_name_plural = "Students"
        
    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.enrolled}"
