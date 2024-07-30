from django.contrib import admin
from .models import Page
from .forms import PageForm


class PageAdmin(admin.ModelAdmin):
    form = PageForm
    list_display = ('name', 'description', 'main_image', 'gallery', 'status')
    # change_form_template = 'admin/add_page.html'
    fieldsets = (
        (None, {
            'fields': ('name', 'description', 'main_image', 'gallery', 'status')
        }),
        ('SEO блок', {
            'classes': ('collapse',),
            'fields': ('url_seo', 'title_seo', 'keywords_seo', 'description_seo')
        }),
    )

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        return form


admin.site.register(Page, PageAdmin)
