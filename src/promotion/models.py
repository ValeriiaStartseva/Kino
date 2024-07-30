from django.db import models
from django.utils import timezone
from src.core.models import Gallery, GalleryImage
from src.core.models import SEOMixin


class Post(SEOMixin, models.Model):
    TYPE = (
        ('news', 'Новина'),
        ('prom', 'Акція'),
    )
    name = models.CharField(max_length=40)
    published_date = models.DateField(default=timezone.now)
    description = models.TextField()
    status = models.BooleanField(default=False)
    link = models.URLField()
    type = models.CharField(max_length=4, choices=TYPE)
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE)
    main_image = models.OneToOneField(
        GalleryImage,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='main_image_for'
    )

    def __str__(self):
        return self.name
