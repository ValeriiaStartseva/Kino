from django import forms
from django.forms import inlineformset_factory
from .models import Movie, GalleryImage, Gallery


class MovieForm(forms.ModelForm):
    main_image = forms.ModelChoiceField(queryset=GalleryImage.objects.all(), required=True, widget=forms.HiddenInput())
    gallery_form = forms.ModelMultipleChoiceField(queryset=GalleryImage.objects.all(), required=False, widget=forms.CheckboxSelectMultiple)
    type = forms.MultipleChoiceField(choices=Movie.TYPE_CHOICES, widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Movie
        fields = [
            'name', 'description', 'main_image', 'gallery_form', 'trailer', 'type',
            'url_seo', 'title_seo', 'keywords_seo', 'description_seo'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Назва фільму'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Опис'}),
            'main_image': forms.Select(attrs={'class': 'form-control'}),
            'gallery_form': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'trailer': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Посилання на відео в YouTube'}),
            'type': forms.CheckboxSelectMultiple(attrs={'class': 'form-check-input'}),
            'url_seo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'URL'}),
            'title_seo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'keywords_seo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Keywords'}),
            'description_seo': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields['gallery_form'].queryset = GalleryImage.objects.filter(gallery=self.instance.gallery)


GalleryImageFormSet = inlineformset_factory(Gallery, GalleryImage, fields=('alt_text', 'image'), extra=1)
