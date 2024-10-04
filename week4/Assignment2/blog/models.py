from django.db import models
from django.core.validators import EmailValidator, MinValueValidator, MaxValueValidator


# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(
        max_length=254, 
        validators=[EmailValidator(message="Enter a valid email address.")]
    )
    date_of_birth = models.DateField()
    enrolled = models.DateField()
    grade = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(12)]
    )
        
    class Meta:
        verbose_name_plural = "Students"
        
    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.enrolled}"
