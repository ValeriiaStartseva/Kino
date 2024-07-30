from django.contrib import admin
from .models import Cinema, Hall
from .forms import CinemaForm, HallForm


class CinemaAdmin(admin.ModelAdmin):
    form = CinemaForm
    list_display = ('name', 'title', 'city', 'gallery', 'main_image', 'logo')
    change_form_template = 'admin/add_cinema.html'
    fieldsets = (
        (None, {
            'fields': ('name', 'title', 'city', 'gallery', 'main_image', 'logo')
        }),
        ('SEO блок', {
            'classes': ('collapse',),
            'fields': ('url_seo', 'title_seo', 'keywords_seo', 'description_seo')
        }),
    )

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        return form


class HallAdmin(admin.ModelAdmin):
    form = HallForm
    list_display = ('name', 'description', 'schema_json', 'gallery', 'main_image', 'schema_picture', 'created_at')
    readonly_fields = ('created_at',)
    change_form_template = 'admin/add_hall.html'

    fieldsets = (
        (None, {
            'fields': ('name', 'description', 'schema_json', 'gallery', 'main_image', 'schema_picture', 'created_at')
        }),
        ('SEO блок', {
            'classes': ('collapse',),
            'fields': ('url_seo', 'title_seo', 'keywords_seo', 'description_seo')
        }),
    )

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        return form


admin.site.register(Hall, HallAdmin)





admin.site.register(Cinema, CinemaAdmin)


