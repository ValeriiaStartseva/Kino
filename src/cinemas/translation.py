from modeltranslation.translator import register, TranslationOptions
from .models import Cinema, Hall


@register(Cinema)
class CinemaTranslationOptions(TranslationOptions):
    fields = ('name', 'description')


@register(Hall)
class HallTranslationOptions(TranslationOptions):
    fields = ('name', 'description')
