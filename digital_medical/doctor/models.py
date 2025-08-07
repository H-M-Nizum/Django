from django.db import models

class DoctorModel(models.Model):
    name = models.CharField(max_length=250)
    designation = models.CharField(max_length=250, blank=True, null=True)
    email = models.EmailField(max_length=250)
    phone = models.CharField(max_length=12)
    age = models.IntegerField()
    
    # max_length=250: Maximum 250 characters.
    # blank=True: Allows this field to be blank in forms (not required).
    # null=True: Allows NULL in the database.

    # Auto timestamp fields
    created_at = models.DateTimeField(auto_now_add=True)  # Set only once when the record is created
    updated_at = models.DateTimeField(auto_now=True)      # Updated every time the record is saved

    def __str__(self):
        return f"{self.name} ({self.designation})"

    # This is a special method in Python classes called __str__. 
    # In Django models, it's used to define what should be shown when you print a model instance or view it in the Django admin panel, shell, or template.