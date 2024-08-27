from src.core.forms import GalleryImageFormSet
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import MainPageBanners, MainPageNewsBanners, BackgroundBanner
from .forms import MainPageBannersForm, MainPageNewsBannersForm, BackgroundBannerForm, BannerImageFormSet_main, MainPageBanners, BannerImageFormSet_news
from django.db import transaction
from django.urls import reverse
import logging

# Set up logging
logger = logging.getLogger(__name__)


@transaction.atomic
def main_banners(request):
    logger.info("Виклик функції main_banners.")
    banner_instance = MainPageBanners.objects.first()

    if banner_instance:
        logger.info(f"Знайдено екземпляр MainPageBanners з ID: {banner_instance.id}")
    else:
        logger.warning("Не знайдено жодного екземпляру MainPageBanners. Буде створений новий.")

    if request.method == 'POST':
        logger.info("Отримано POST запит на збереження банера.")

        form = MainPageBannersForm(request.POST, request.FILES, instance=banner_instance)
        formset = BannerImageFormSet_main(request.POST, request.FILES, instance=banner_instance)
        print(request.POST)
        print(request.FILES)
        if form.is_valid():
            logger.info("Основна форма MainPageBannersForm дійсна.")
        else:
            logger.error(f"Помилки в основній формі: {form.errors}")

        if formset.is_valid():
            logger.info("Формсет BannerImageFormSet_main дійсний.")
        else:
            logger.error(f"Помилки у формсеті: {formset.errors}")

        if form.is_valid() and formset.is_valid():
            main_banner = form.save()
            logger.info(f"Банер MainPageBanners збережено з ID: {main_banner.id}")

            formset.instance = main_banner
            formset.save()
            logger.info(f"Формсет збережено для банера з ID: {main_banner.id}")

            messages.success(request, 'Банер успішно збережено.')
            logger.info("Повідомлення про успішне збереження банера відправлено користувачу.")
            return redirect('banner_list')
        else:
            logger.error("Форма або формсет недійсні. Збереження не виконано.")
            messages.error(request, 'Форма або набір форм недійсні.')

    else:
        logger.info("Отримано GET запит для відображення форми редагування банера.")
        form = MainPageBannersForm(instance=banner_instance)
        formset = BannerImageFormSet_main(instance=banner_instance)

    logger.info("Відображення шаблону редагування банера.")
    return render(request, 'admin/main_page_banner.html', {'form': form, 'formset': formset})


@transaction.atomic
def news_banners(request):
    logger.info("Виклик функції news_banners.")
    banner_instance = MainPageNewsBanners.objects.first()

    if banner_instance:
        logger.info(f"Знайдено екземпляр MainPageBanners з ID: {banner_instance.id}")
    else:
        logger.warning("Не знайдено жодного екземпляру MainPageBanners. Буде створений новий.")

    if request.method == 'POST':
        logger.info("Отримано POST запит на збереження банера.")

        form = MainPageNewsBannersForm(request.POST, request.FILES, instance=banner_instance)
        formset = BannerImageFormSet_news(request.POST, request.FILES, instance=banner_instance)
        print(request.POST)
        print(request.FILES)
        if form.is_valid():
            logger.info("Основна форма MainPageBannersForm дійсна.")
        else:
            logger.error(f"Помилки в основній формі: {form.errors}")

        if formset.is_valid():
            logger.info("Формсет BannerImageFormSet_main дійсний.")
        else:
            logger.error(f"Помилки у формсеті: {formset.errors}")

        if form.is_valid() and formset.is_valid():
            news_banner = form.save()
            logger.info(f"Банер MainPageBanners збережено з ID: {news_banner.id}")

            formset.instance = news_banner
            formset.save()
            logger.info(f"Формсет збережено для банера з ID: {news_banner.id}")

            messages.success(request, 'Банер успішно збережено.')
            logger.info("Повідомлення про успішне збереження банера відправлено користувачу.")
            return redirect('banner_list')
        else:
            logger.error("Форма або формсет недійсні. Збереження не виконано.")
            messages.error(request, 'Форма або набір форм недійсні.')

    else:
        logger.info("Отримано GET запит для відображення форми редагування банера.")
        form = MainPageNewsBannersForm(instance=banner_instance)
        formset = BannerImageFormSet_news(instance=banner_instance)

    logger.info("Відображення шаблону редагування банера.")
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
