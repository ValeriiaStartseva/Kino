from django.contrib import admin
from .models import Movie
from .forms import MovieForm


class MovieAdmin(admin.ModelAdmin):
    form = MovieForm
    list_display = ('name', 'description', 'main_image', 'gallery', 'trailer', 'type')
    change_form_template = 'admin/add_movie.html'
    fieldsets = (
        (None, {
            'fields': ('name', 'description', 'main_image', 'gallery', 'trailer', 'type')
        }),
        ('SEO блок', {
            'classes': ('collapse',),
            'fields': ('url_seo', 'title_seo', 'keywords_seo', 'description_seo')
        }),
    )

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        return form


admin.site.register(Movie, MovieAdmin)
