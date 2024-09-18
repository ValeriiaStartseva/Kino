from .models import Cinema, Hall
from django import forms
from django.forms import inlineformset_factory
from src.core.models import GalleryImage, Gallery
from modeltranslation.forms import TranslationModelForm


class CinemaForm(forms.ModelForm):
    main_image = forms.ModelChoiceField(queryset=GalleryImage.objects.all(), required=True, widget=forms.HiddenInput())
    gallery_form = forms.ModelMultipleChoiceField(queryset=GalleryImage.objects.all(), required=False,
                                                  widget=forms.CheckboxSelectMultiple)
    logo = forms.ModelChoiceField(queryset=GalleryImage.objects.all(), required=True, widget=forms.HiddenInput())

    class Meta:
        model = Cinema
        fields = [
            'name_uk', 'description_uk',
            'name_en', 'description_en',
            'city', 'gallery_form', 'main_image', 'logo',
            'url_seo', 'title_seo', 'keywords_seo', 'description_seo'
        ]
        widgets = {
            'name_uk': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cinema name (UK)'}),
            'name_en': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cinema name (EN)'}),
            'description_uk': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description (UK)'}),
            'description_en': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description (EN)'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}),
            'main_image': forms.Select(attrs={'class': 'form-control'}),
            'logo': forms.Select(attrs={'class': 'form-control'}),
            'gallery_form': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'url_seo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'URL'}),
            'title_seo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'keywords_seo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Keywords'}),
            'description_seo': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields['gallery_form'].queryset = GalleryImage.objects.filter(gallery=self.instance.gallery)


class HallForm(forms.ModelForm):
    main_image = forms.ModelChoiceField(queryset=GalleryImage.objects.all(), required=True, widget=forms.HiddenInput())
    gallery_form = forms.ModelMultipleChoiceField(queryset=GalleryImage.objects.all(), required=False, widget=forms.CheckboxSelectMultiple)
    schema_picture = forms.ModelChoiceField(queryset=GalleryImage.objects.all(), required=True, widget=forms.HiddenInput())
    created_at = forms.DateTimeField(widget=forms.TextInput(attrs={'readonly': 'readonly'}), required=False)

    class Meta:
        model = Hall
        fields = [
            'name_uk', 'description_uk',
            'name_en', 'description_en',
            'schema_json', 'gallery_form', 'main_image', 'schema_picture',
            'url_seo', 'title_seo', 'keywords_seo', 'description_seo'
        ]

        widgets = {
            'name_uk': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Hall name (UK)'}),
            'name_en': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Hall name (EN)'}),
            'description_uk': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description (UK)'}),
            'description_en': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description (EN)'}),
            'schema_json': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'hall schema JSON'}),
            'main_image': forms.Select(attrs={'class': 'form-control'}),
            'schema_picture': forms.Select(attrs={'class': 'form-control'}),
            'gallery_form': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'url_seo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'URL'}),
            'title_seo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'keywords_seo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Keywords'}),
            'description_seo': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields['gallery_form'].queryset = GalleryImage.objects.filter(gallery=self.instance.gallery)
            self.fields['created_at'].initial = self.instance.created_at


GalleryImageFormSet = inlineformset_factory(Gallery, GalleryImage, fields=('alt_text', 'image'), extra=1)
