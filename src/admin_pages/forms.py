from django import forms
from django.forms import inlineformset_factory
from .models import Page, GalleryImage, Gallery, MainPage, Contacts, SEOMixin


class PageForm(forms.ModelForm):
    main_image = forms.ModelChoiceField(queryset=GalleryImage.objects.all(), required=True, widget=forms.HiddenInput())
    gallery_form = forms.ModelMultipleChoiceField(queryset=GalleryImage.objects.all(), required=False,
                                                  widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Page
        fields = [
            'name_uk', 'description_uk',
            'name_en', 'description_en',
            'main_image', 'gallery_form', 'status',
            'url_seo', 'title_seo', 'keywords_seo', 'description_seo'
        ]
        widgets = {
            'name_uk': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Page name (UK)'}),
            'name_en': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Page name (EN)'}),
            'description_uk': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description (UK)'}),
            'description_en': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description (EN)'}),
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

        widgets = {
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}),
            'seo_text_main_page': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'SEO Text'}),
            'url_seo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'URL'}),
            'title_seo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'keywords_seo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Keywords'}),
            'description_seo': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),
            'status': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class ContactsForm(forms.ModelForm):
    logo = forms.ModelChoiceField(queryset=GalleryImage.objects.all(), required=True,
                                  widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Contacts
        fields = [
            'cinema_name', 'adress_cinema_contacts', 'numbers_contacts', 'email_cinema_contacts', 'coordinates_long',
            'coordinates_lat', 'logo', 'status',
        ]

        widgets = {
            'cinema_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cinema name'}),
            'adress_cinema_contacts': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Adress'}),
            'numbers_contacts': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phones'}),
            'email_cinema_contacts': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'email'}),
            'coordinates_long': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Coordinates, long'}),
            'coordinates_lat': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Coordinates, lat'}),
            'logo': forms.Select(attrs={'class': 'form-control'}),
        }


ContactsFormSet = forms.inlineformset_factory(SEOMixin, Contacts, form=ContactsForm, extra=0)
