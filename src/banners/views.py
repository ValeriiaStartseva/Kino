from src.core.forms import GalleryImageFormSet
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import MainPageBanners, Gallery, MainPageNewsBanners, BackgroundBanner
from .forms import MainPageBannersForm, GalleryImageFormSet, MainPageNewsBannersForm, BackgroundBannerForm
from django.db import transaction
from django.urls import reverse
import logging

# Set up logging
logger = logging.getLogger(__name__)

@transaction.atomic
def main_banners(request):
    banner_instance = MainPageBanners.objects.first()

    if request.method == 'POST':
        form = MainPageBannersForm(request.POST, request.FILES, instance=banner_instance)
        formset = GalleryImageFormSet(request.POST, request.FILES,
                                      instance=banner_instance.gallery if banner_instance else None)

        if form.is_valid() and formset.is_valid():
            main_banner = form.save(commit=False)

            if not banner_instance:
                gallery = Gallery.objects.create()
                main_banner.gallery = gallery

            main_banner.save()

            formset.instance = main_banner.gallery
            formset.save(commit=True)

            messages.success(request, 'Банер успішно збережено.')
            return redirect('main_page_banner')
        else:
            messages.error(request, 'Форма або набір форм недійсні.')
    else:
        form = MainPageBannersForm(instance=banner_instance)
        formset = GalleryImageFormSet(instance=banner_instance.gallery if banner_instance else None)

    return render(request, 'admin/main_page_banner.html', {'form': form, 'formset': formset})

@transaction.atomic
def news_banners(request):
    banner_instance = MainPageNewsBanners.objects.first()

    if request.method == 'POST':
        form = MainPageNewsBannersForm(request.POST, request.FILES, instance=banner_instance)
        formset = GalleryImageFormSet(request.POST, request.FILES,
                                      instance=banner_instance.gallery if banner_instance else None)

        if form.is_valid() and formset.is_valid():
            news_banner = form.save(commit=False)

            if not banner_instance:
                gallery = Gallery.objects.create()
                news_banner.gallery = gallery

            news_banner.save()

            formset.instance = news_banner.gallery
            formset.save(commit=True)

            messages.success(request, 'Банер успішно збережено.')
            return redirect('main_page_news_banner')
        else:
            messages.error(request, 'Форма або набір форм недійсні.')
    else:
        form = MainPageNewsBannersForm(instance=banner_instance)
        formset = GalleryImageFormSet(instance=banner_instance.gallery if banner_instance else None)

    return render(request, 'admin/news_banner.html', {'form': form, 'formset': formset})


@transaction.atomic
def back_banners(request):
    banner_instance = BackgroundBanner.objects.first()
    logger.info("Retrieved banner instance: %s", banner_instance)

    if request.method == 'POST':
        logger.info("POST request received with data: %s", request.POST)
        form = BackgroundBannerForm(request.POST, request.FILES, instance=banner_instance)

        if form.is_valid():
            logger.info("Form is valid")
            back_banner = form.save(commit=False)

            # If CSS option is selected, ensure image is not saved
            if request.POST.get('background_type') == 'css_background':  # CSS option
                back_banner.back = 'css'
                back_banner.background_image = None
                logger.info("Selected CSS background, setting back to 'css' and background_image to None")
            else:
                back_banner.back = 'photo'
                back_banner.background_color = None
                logger.info("Selected photo background, setting back to 'photo' and background_color to None")

            back_banner.save()
            logger.info("Back banner saved: %s", back_banner)

            messages.success(request, 'Банер успішно збережено.')
            return redirect('back_banner')
        else:
            logger.error("Form is invalid: %s", form.errors)
            messages.error(request, 'Форма недійсна.')
    else:
        logger.info("GET request received")
        form = BackgroundBannerForm(instance=banner_instance)

    return render(request, 'admin/back_banner.html', {'form': form, 'banner_instance': banner_instance})


def banner_list(request):
    context = {
        'banner_list': [
            {'name': 'Банера на головній сторінці', 'edit_url': reverse('main_page_banner')},
            {'name': 'Банер на задньому фоні', 'edit_url': reverse('back_banner')},
            {'name': 'Банер новин та акцій на головній сторінці', 'edit_url': reverse('main_page_news_banner')}
        ]
    }
    return render(request, 'admin/banners.html', context)
