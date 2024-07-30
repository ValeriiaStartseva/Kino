from django.contrib import admin
from .models import GalleryImage, Gallery
from .forms import GalleryImageForm


class GalleryImageAdmin(admin.ModelAdmin):
    form = GalleryImageForm
    list_display = ('alt_text', 'gallery')
    change_form_template = 'admin/upload_image.html'

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['gallery'].queryset = Gallery.objects.all()
        return form


admin.site.register(GalleryImage, GalleryImageAdmin)
