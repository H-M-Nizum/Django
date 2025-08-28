from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.core.validators import MinLengthValidator, MaxLengthValidator

class UserManager(BaseUserManager):
    def create_user(self, email, full_name, phone_number, t_c, address, password=None, password2=None):
        """
        Creates and saves a User with the given email, full_name, phone_number, t_c, address and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            full_name=full_name,
            phone_number=phone_number,
            t_c=t_c,
            address=address
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, full_name, phone_number, t_c, address, password):
        """
        Creates and saves a superuser with the given email, full_name, phone_number, t_c, address and password.
        """
        user = self.create_user(
            email,
            password=password,
            full_name=full_name,
            phone_number=phone_number,
            t_c=t_c,
            address=address
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(
        verbose_name='email',
        max_length=255,
        unique=True,
    )
    # date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=12, validators=[MinLengthValidator(11)])
    address = models.CharField(max_length=250)
    t_c = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name', 'phone_number', 't_c', 'address']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin