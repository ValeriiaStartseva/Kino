from django import forms
from django.forms import inlineformset_factory
from .models import Post, GalleryImage, Gallery


class PostForm(forms.ModelForm):
    main_image = forms.ModelChoiceField(queryset=GalleryImage.objects.all(), required=True, widget=forms.HiddenInput())
    gallery_form = forms.ModelMultipleChoiceField(queryset=GalleryImage.objects.all(), required=False, widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Post
        fields = [
            'name', 'description', 'main_image', 'gallery_form', 'link', 'type', 'published_date', 'status',
            'url_seo', 'title_seo', 'keywords_seo', 'description_seo'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Назва'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Опис'}),
            'main_image': forms.Select(attrs={'class': 'form-control'}),
            'gallery_form': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'link': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Посилання на відео'}),
            'type': forms.Select(choices=Post.TYPE),
            'published_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'url_seo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'URL'}),
            'title_seo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'keywords_seo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Keywords'}),
            'description_seo': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
            'status': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields['gallery_form'].queryset = GalleryImage.objects.filter(gallery=self.instance.gallery)


GalleryImageFormSet = inlineformset_factory(Gallery, GalleryImage, fields=('alt_text', 'image'), extra=1)
