import os
import django

# Налаштування Django оточення
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')  # Замість 'your_project_name' вкажіть назву вашого проекту
django.setup()

from src.core.models import GalleryImage

# Видалення рядків, де image порожнє або дорівнює 0
GalleryImage.objects.filter(image__isnull=True).delete()
GalleryImage.objects.filter(image='').delete()
