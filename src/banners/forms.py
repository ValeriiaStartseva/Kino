from django import forms
from .models import MainPageBanners, MainPageNewsBanners, BackgroundBanner, BannerImage
from django.forms import inlineformset_factory


BannerImageFormSet_main = inlineformset_factory(
    MainPageBanners,
    BannerImage,
    fields=('gallery_image', 'url'),
    extra=0,
    widgets={
        'gallery_image': forms.Select(attrs={'class': 'form-control'}),
        'url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Посилання на сторінку'}),
    }
)

BannerImageFormSet_news = inlineformset_factory(
    MainPageNewsBanners,
    BannerImage,
    fields=('gallery_image', 'url'),
    extra=0,
    widgets={
        'gallery_image': forms.Select(attrs={'class': 'form-control'}),
        'url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Посилання на сторінку'}),
    }
)


class BannerImageForm(forms.ModelForm):
    class Meta:
        model = BannerImage
        fields = ['gallery_image', 'url']
        widgets = {
            'gallery_image': forms.HiddenInput(),
        }


class MainPageBannersForm(forms.ModelForm):
    class Meta:
        model = MainPageBanners
        fields = [
            'rotation_speed', 'status',
        ]
        widgets = {
            'rotation_speed': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Швидкість'}),
            'status': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class MainPageNewsBannersForm(forms.ModelForm):
    class Meta:
        model = MainPageNewsBanners
        fields = [
            'rotation_speed', 'status',
        ]
        widgets = {
            'rotation_speed': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Швидкість'}),
            'status': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


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
