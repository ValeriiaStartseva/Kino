from django import forms
from .models import GalleryImage, Gallery, SEOMixin


class GalleryImageForm(forms.ModelForm):
    class Meta:
        model = GalleryImage
        fields = ['alt_text', 'image', 'gallery']
        labels = {
            'alt_text': 'Alt-text',
            'image': 'img',
            'gallery': 'gallery',
        }
        widgets = {
            'alt_text': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'alt-text'}),
            'image': forms.FileInput(attrs={'class': 'form-control-file', 'id': 'imageInput', 'accept': 'image/*'}),
            'gallery': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(GalleryImageForm, self).__init__(*args, **kwargs)
        self.fields['alt_text'].required = False


GalleryImageFormSet = forms.inlineformset_factory(Gallery, GalleryImage, fields=['alt_text', 'image'], extra=10,
                                                  can_delete=True)


class SEOMixinForm(forms.ModelForm):
    class Meta:
        model = SEOMixin
        fields = ['url_seo', 'title_seo', 'keywords_seo', 'description_seo']


class SearchForm(forms.Form):
    query = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control form-control-sm',
        'placeholder': 'Search...',
        'aria-label': 'Search'
    }))
