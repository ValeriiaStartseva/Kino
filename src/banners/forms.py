from django import forms
from .models import MainPageBanners, MainPageNewsBanners, BackgroundBanner
from django.forms import inlineformset_factory
from src.core.models import Gallery, GalleryImage


class MainPageBannersForm(forms.ModelForm):
    gallery_form = forms.ModelMultipleChoiceField(queryset=GalleryImage.objects.all(), required=False,
                                                  widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = MainPageBanners
        fields = [
            'rotation_speed', 'gallery_form', 'status',
        ]
        widgets = {
            'rotation_speed': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Швидкість'}),
            'gallery_form': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'status': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields['gallery_form'].queryset = GalleryImage.objects.filter(gallery=self.instance.gallery)


GalleryImageFormSet = inlineformset_factory(Gallery, GalleryImage, fields=('alt_text', 'image'), extra=1)


class MainPageNewsBannersForm(forms.ModelForm):
    gallery_form = forms.ModelMultipleChoiceField(queryset=GalleryImage.objects.all(), required=False,
                                                  widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = MainPageNewsBanners
        fields = [
            'rotation_speed', 'gallery_form', 'status',
        ]
        widgets = {
            'rotation_speed': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Швидкість'}),
            'gallery_form': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'status': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields['gallery_form'].queryset = GalleryImage.objects.filter(gallery=self.instance.gallery)


class BackgroundBannerForm(forms.ModelForm):
    class Meta:
        model = BackgroundBanner
        fields = ['back', 'background_color', 'background_image']

    def __init__(self, *args, **kwargs):
        super(BackgroundBannerForm, self).__init__(*args, **kwargs)
        self.fields['background_color'].widget = forms.TextInput(attrs={'type': 'color'})
        self.fields['background_color'].required = False
        self.fields['background_image'].required = False

        instance = kwargs.get('instance')
        if instance:
            self.fields['background_color'].initial = instance.background_color
            self.fields['background_image'].initial = instance.background_image
            self.fields['back'].initial = instance.back
