from django import forms
from django.forms import inlineformset_factory, modelformset_factory
from .models import Page, GalleryImage, Gallery, MainPage, Contacts


class PageForm(forms.ModelForm):
    main_image = forms.ModelChoiceField(queryset=GalleryImage.objects.all(), required=True, widget=forms.HiddenInput())
    gallery_form = forms.ModelMultipleChoiceField(queryset=GalleryImage.objects.all(), required=False, widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Page
        fields = [
            'name', 'description', 'main_image', 'gallery_form', 'status',
            'url_seo', 'title_seo', 'keywords_seo', 'description_seo'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Назва'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Опис'}),
            'main_image': forms.Select(attrs={'class': 'form-control'}),
            'gallery_form': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'url_seo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'URL'}),
            'title_seo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'keywords_seo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Keywords'}),
            'description_seo': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
            'status': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields['gallery_form'].queryset = GalleryImage.objects.filter(gallery=self.instance.gallery)


GalleryImageFormSet = inlineformset_factory(Gallery, GalleryImage, fields=('alt_text', 'image'), extra=1)


class MainPageForm(forms.ModelForm):
    class Meta:
        model = MainPage
        fields = ('phone', 'seo_text_main_page', 'status',
                  'url_seo', 'title_seo', 'keywords_seo', 'description_seo')


class ContactForm(forms.ModelForm):
    logo = forms.ModelChoiceField(queryset=GalleryImage.objects.all(), required=True, widget=forms.HiddenInput())
    created_at = forms.DateTimeField(widget=forms.TextInput(attrs={'readonly': 'readonly'}), required=False)

    class Meta:
        model = Contacts
        fields = [
            'cinema_name', 'adress_cinema_contacts', 'numbers_contacts', 'email_cinema_contacts', 'coordinates_long',
            'coordinates_lat', 'logo', 'status',
            'url_seo', 'title_seo', 'keywords_seo', 'description_seo'
        ]

        widgets = {
            'cinema_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Назва кінотеатру'}),
            'adress_cinema_contacts': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Адреса'}),
            'numbers_contacts': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Телефони'}),
            'email_cinema_contacts': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Електронна пошта'}),
            'coordinates_long': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Координати, довгота'}),
            'coordinates_lat': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Координати, широта'}),
            'logo': forms.Select(attrs={'class': 'form-control'}),
            'url_seo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'URL'}),
            'title_seo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'keywords_seo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Keywords'}),
            'description_seo': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
            'status': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }


ContactFormSet = modelformset_factory(Contacts, form=ContactForm, extra=1)
