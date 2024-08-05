from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password=password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    LANGUAGES = (
        ('ru', 'RU'),
        ('ua', 'UA'),
    )

    GENDERS = (
        ('F', 'Female'),
        ('M', 'Male'),
    )

    name = models.CharField(max_length=10, blank=True)
    last_name = models.CharField(max_length=12, blank=True)
    nickname = models.CharField(max_length=10, unique=True)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=30)
    num_card = models.CharField(max_length=12)
    language = models.CharField(max_length=3, choices=LANGUAGES, default='ua')
    gender = models.CharField(max_length=1, choices=GENDERS)
    phone = PhoneNumberField(blank=True, region='UA')
    date_birthday = models.DateField(blank=True, null=True)
    city = models.CharField(max_length=12)

    is_staff = models.BooleanField(_('staff status'), default=False)
    is_active = models.BooleanField(_('active'), default=True)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    last_login = models.DateTimeField(_('last login'), blank=True, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nickname']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.email
