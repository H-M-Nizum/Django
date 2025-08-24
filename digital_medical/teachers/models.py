from django.db import models

# Create your models here.
class TeacherModel(models.Model):
    name = models.CharField(max_length=250)
    age = models.IntegerField()
    subject = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    join_date = models.DateField()

    def __str__(self):
        return f"{self.name}-{self.join_date}"