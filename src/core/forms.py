from django import forms
from .models import GalleryImage, Gallery, SEOMixin


class GalleryImageForm(forms.ModelForm):
    class Meta:
        model = GalleryImage
        fields = ['alt_text', 'image', 'gallery']
        labels = {
            'alt_text': 'Alt-text',
            'image': 'Картинка',
            'gallery': 'Галерея',
        }
        widgets = {
            'alt_text': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'alt-text'}),
            'image': forms.FileInput(attrs={'class': 'form-control-file', 'id': 'imageInput', 'accept': 'image/*'}),
            'gallery': forms.Select(attrs={'class': 'form-control'}),
        }


GalleryImageFormSet = forms.inlineformset_factory(Gallery, GalleryImage, fields=['alt_text', 'image'], extra=10,
                                                  can_delete=True)


class SEOMixinForm(forms.ModelForm):
    class Meta:
        model = SEOMixin
        fields = ['url_seo', 'title_seo', 'keywords_seo', 'description_seo']
