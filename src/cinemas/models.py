from django.db import models
from src.core.models import Gallery, GalleryImage
from src.core.models import SEOMixin


class Cinema(SEOMixin, models.Model):
    name = models.CharField(max_length=20, unique=True)
    title = models.TextField()
    city = models.CharField(max_length=12)
    logo = models.OneToOneField(
        GalleryImage,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='cinema_logo'
    )
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)
    main_image = models.OneToOneField(
        GalleryImage,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='cinema_main_image'
    )

    def __str__(self):
        return self.name


class Hall(SEOMixin, models.Model):
    name = models.CharField(max_length=20, unique=True)
    description = models.TextField()
    schema_json = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    schema_picture = models.OneToOneField(
        GalleryImage,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='hall_schema_picture'
    )
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)
    main_image = models.OneToOneField(
        GalleryImage,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='hall_main_image'
    )
    cinema_hall = models.ForeignKey(
        Cinema,
        on_delete=models.CASCADE,
        related_name='halls',
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name
