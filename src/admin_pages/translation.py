from modeltranslation.translator import register, TranslationOptions
from .models import Page


@register(Page)
class NewsTranslationOptions(TranslationOptions):
    fields = ('name', 'description')
