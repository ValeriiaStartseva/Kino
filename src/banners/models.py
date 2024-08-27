from django.db import models
from src.core.models import GalleryImage


class MainPageBanners(models.Model):
    rotation_speed = models.IntegerField()
    status = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        # Перетворення секунд в мілісекунди перед збереженням
        self.rotation_speed = self.rotation_speed * 1000
        super().save(*args, **kwargs)


class MainPageNewsBanners(models.Model):
    rotation_speed = models.IntegerField()
    status = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        # Перетворення секунд в мілісекунди перед збереженням
        self.rotation_speed = self.rotation_speed * 1000
        super().save(*args, **kwargs)


class BannerImage(models.Model):
    gallery_image = models.ForeignKey(GalleryImage, on_delete=models.CASCADE)
    url = models.URLField(max_length=200, blank=True, null=True)
    main_page_banner = models.ForeignKey(MainPageBanners, on_delete=models.CASCADE, related_name='banner_images', null=True, blank=True)
    news_banner = models.ForeignKey(MainPageNewsBanners, on_delete=models.CASCADE, related_name='news_images', null=True, blank=True)





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






