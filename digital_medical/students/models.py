from django.db import models
from django.core.validators import MinLengthValidator, MaxValueValidator, MinValueValidator


class StudentModel(models.Model):
    student_name = models.CharField(max_length=250)

    # Roll must be exactly 6 characters
    roll = models.CharField(
        max_length=6,
        unique=True,  # Prevent duplicate roll numbers
        validators=[MinLengthValidator(6)]
    )

    # Age with validation (example: 5 to 25 years)
    age = models.IntegerField(
        validators=[MinValueValidator(5), MaxValueValidator(25)]
    )

    address = models.TextField()

    # Class choices in words
    CLASS_CHOICES = [
        ("one", "One"),
        ("two", "Two"),
        ("three", "Three"),
        ("four", "Four"),
        ("five", "Five"),
        ("six", "Six"),
        ("seven", "Seven"),
        ("eight", "Eight"),
        ("nine", "Nine"),
        ("ten", "Ten"),
    ]
    class_name = models.CharField(max_length=10, choices=CLASS_CHOICES)

    def __str__(self):
        return f"{self.student_name} (Roll: {self.roll}, Class: {self.class_name.title()})"
