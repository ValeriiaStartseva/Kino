from django.db import models
from django.urls import reverse
from django.utils import timezone
from src.core.models import Gallery, GalleryImage
from src.core.models import SEOMixin
from django.utils.text import slugify


class Post(SEOMixin, models.Model):
    TYPE = (
        ('news', 'Новина'),
        ('prom', 'Акція'),
    )
    name = models.CharField(max_length=40)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    published_date = models.DateField(default=timezone.now)
    description = models.TextField()
    status = models.BooleanField(default=False)
    link = models.URLField()
    type = models.CharField(max_length=4, choices=TYPE)
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, null=True, blank=True)
    main_image = models.OneToOneField(
        GalleryImage,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='main_image_for'
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if hasattr(self, 'name_en') and self.name_en:
            self.slug = slugify(self.name_en)
        else:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('promotion_detail', args=[str(self.slug)])
