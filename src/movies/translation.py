# translation.py
from modeltranslation.translator import TranslationOptions, register
from .models import Movie


@register(Movie)
class MovieTranslationOptions(TranslationOptions):
    fields = ('name', 'description')



