from django.shortcuts import render, redirect
from django.contrib import messages
from .models import MainPageNewsBanners, BackgroundBanner
from .forms import MainPageBannersForm, MainPageNewsBannersForm, BackgroundBannerForm, BannerImageFormSet_main, MainPageBanners, BannerImageFormSet_news
from django.db import transaction
from django.urls import reverse


@transaction.atomic
def main_banners(request):

    banner_instance = MainPageBanners.objects.first()

    if request.method == 'POST':

        form = MainPageBannersForm(request.POST, request.FILES, instance=banner_instance)
        formset = BannerImageFormSet_main(request.POST, request.FILES, instance=banner_instance)

        if form.is_valid() and formset.is_valid():
            main_banner = form.save()

            formset.instance = main_banner
            formset.save()

            messages.success(request, 'Banners updated.')

            return redirect('banner_list')
        else:
            messages.error(request, 'Form or formset is invalid.')

    else:

        form = MainPageBannersForm(instance=banner_instance)
        formset = BannerImageFormSet_main(instance=banner_instance)

    return render(request, 'admin/main_page_banner.html', {'form': form, 'formset': formset})


@transaction.atomic
def news_banners(request):

    banner_instance = MainPageNewsBanners.objects.first()

    if request.method == 'POST':

        form = MainPageNewsBannersForm(request.POST, request.FILES, instance=banner_instance)
        formset = BannerImageFormSet_news(request.POST, request.FILES, instance=banner_instance)

        if form.is_valid() and formset.is_valid():
            news_banner = form.save()

            formset.instance = news_banner
            formset.save()

            messages.success(request, 'Banners added successfully!')

            return redirect('banner_list')
        else:

            messages.error(request, 'Form or formset is invalid.')

    else:

        form = MainPageNewsBannersForm(instance=banner_instance)
        formset = BannerImageFormSet_news(instance=banner_instance)

    return render(request, 'admin/news_banner.html', {'form': form, 'formset': formset})


@transaction.atomic
def back_banners(request):
    banner_instance = BackgroundBanner.objects.first()

    if request.method == 'POST':

        form = BackgroundBannerForm(request.POST, request.FILES, instance=banner_instance)

        if form.is_valid():
            back_banner = form.save(commit=False)

            # If CSS option is selected, ensure image is not saved
            if request.POST.get('background_type') == 'css_background':  # CSS option
                back_banner.back = 'css'
                back_banner.background_image = None

            else:
                back_banner.back = 'photo'
                back_banner.background_color = None

            back_banner.save()

            return redirect('banner_list')
        else:

            messages.error(request, 'Form is not valid.')
    else:

        form = BackgroundBannerForm(instance=banner_instance)

    return render(request, 'admin/back_banner.html', {'form': form, 'banner_instance': banner_instance})


def banner_list(request):
    context = {
        'banner_list': [
            {'name': 'Banners on a main page', 'edit_url': reverse('main_page_banner')},
            {'name': 'Background banner', 'edit_url': reverse('back_banner')},
            {'name': 'Banner for posts on a main page', 'edit_url': reverse('main_page_news_banner')}
        ]
    }
    return render(request, 'admin/banners.html', context)
