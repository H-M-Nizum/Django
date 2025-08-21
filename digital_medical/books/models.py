from django.db import models

# Create your models here.
class BooksModel(models.Model):
    name = models.CharField(max_length=250)
    author = models.CharField(max_length=250)
    price = models.FloatField()
    pages = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.author}"