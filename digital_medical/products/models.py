from django.db import models

# Create your models here.
class ProductModel(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()

    OUM_CHOICES = [
        ("kg", "KG"),
        ("gm", "GM"),
        ("pis", "PIS"),
        ("box", "BOX")
    ]

    oum = models.CharField(max_length=10, choices=OUM_CHOICES)
    price = models.FloatField()
    stock = models.IntegerField()
    exp_date = models.DateField()

    def __str__(self):
        return f"{self.name}-{self.price}"