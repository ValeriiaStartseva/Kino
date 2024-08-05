from django.db import models
from src.core.models import Gallery, GalleryImage
from src.core.models import SEOMixin
from django.core.exceptions import ValidationError


class Page(SEOMixin, models.Model):
    name = models.CharField(max_length=12, unique=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)
    main_image = models.OneToOneField(
        GalleryImage,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='page_banner'
    )

    def __str__(self):
        return self.name


class Contacts(models.Model):
    seo = models.ForeignKey(SEOMixin, on_delete=models.CASCADE, related_name='contacts', default=1)
    cinema_name = models.CharField(max_length=20, unique=True)
    adress_cinema_contacts = models.CharField(max_length=50)
    numbers_contacts = models.CharField(max_length=50)
    email_cinema_contacts = models.CharField(max_length=50)
    coordinates_long = models.CharField(max_length=12, default=0)
    coordinates_lat = models.CharField(max_length=12, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
    logo = models.OneToOneField(
        GalleryImage,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='logo_cinema'
    )

    def __str__(self):
        return self.cinema_name


class MainPage(SEOMixin, models.Model):
    status = models.BooleanField(default=False)
    phone = models.CharField(max_length=20, unique=True)
    seo_text_main_page = models.TextField()

    def save_main_page(self, *args, **kwargs):
        if not self.pk and MainPage.objects.exists():
            raise ValidationError('There is can be only one MainPage instance')
        return super(MainPage, self).save(*args, **kwargs)


