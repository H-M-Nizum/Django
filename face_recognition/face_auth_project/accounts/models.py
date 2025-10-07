from django.db import models
# Django’s built-in User model, which stores authentication data (username, email, password, etc.).
from django.contrib.auth.models import User
# Django triggers this signal automatically after a model instance (like User) is saved in the database.
from django.db.models.signals import post_save
# receiver is a decorator that connects a function to a signal.
# When the signal is triggered, the connected function runs automatically.
from django.dispatch import receiver
import os


class UserProfile(models.Model):
    # one-to-one relationship between UserProfile and Django’s User model
    # on_delete=models.CASCADE → if the user is deleted, their profile is deleted too
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    # upload_to='face_images/' → uploaded images are stored in the MEDIA_ROOT/face_images/ folder.
    # null=True → allows NULL in the database (i.e., can be empty).
    # blank=True → allows the form to submit without this field.
    face_image = models.ImageField(upload_to='face_images/', null=True, blank=True)
    # Stores a string representation of the user’s face encoding (e.g., from face recognition).
    # TextField is used because the data may be long (like a serialized list of numbers).
    face_encoding = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Defines a human-readable string for the object — useful in the Django admin panel.
    def __str__(self):
        return f"{self.user.username}'s Profile"

    # how the model name is shown in the admin UI.
    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'


# When a new user is created, it automatically creates a related UserProfile instance.
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """Create UserProfile when User is created"""
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """Save UserProfile when User is saved"""
    instance.profile.save()