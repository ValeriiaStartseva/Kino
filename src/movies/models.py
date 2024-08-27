from django.db import models
from src.core.models import Gallery, GalleryImage
from src.core.models import SEOMixin
from multiselectfield import MultiSelectField
from django.utils.text import slugify
from django import template

class Movie(SEOMixin, models.Model):
    AGE_CHOICES = (
        ('14+', '14+'),
        ('16+', '16+'),
        ('18+', '18+'),
    )

    TYPE_CHOICES = (
        ('IMAX', 'IMAX'),
        ('2D', '2D'),
        ('3D', '3D'),
    )

    name = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    description = models.TextField()
    trailer = models.URLField()

    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)
    main_image = models.OneToOneField(
        GalleryImage,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='main_image_for_movie'
    )

    type = MultiSelectField(choices=TYPE_CHOICES, default='3D')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)




register = template.Library()

@register.filter
def youtube_embed_url(url):
    return url.replace("watch?v=", "embed/")
