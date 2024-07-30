from django.db import models
from src.core.models import Gallery, GalleryImage


class MainPageBanners(models.Model):
    rotation_speed = models.IntegerField()
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)


class BackgroundBanner(models.Model):
    TYPE = (
        ('css', 'css фото'),
        ('photo', 'фото')
    )
    back = models.CharField(max_length=12, choices=TYPE)
    background_color = models.CharField(max_length=7, blank=True, null=True)
    background_image = models.OneToOneField(
        GalleryImage,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='back_img'
    )


class MainPageNewsBanners(models.Model):
    rotation_speed = models.IntegerField()
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

