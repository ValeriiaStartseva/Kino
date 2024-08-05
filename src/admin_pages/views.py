from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.urls import reverse
from src.core.forms import GalleryImageFormSet
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Page, MainPage, SEOMixin, Contacts
from .forms import PageForm, GalleryImageFormSet, MainPageForm, ContactsFormSet
from django.db import transaction
from src.core.models import GalleryImage, Gallery
import logging
from src.core.forms import SEOMixinForm

logger = logging.getLogger(__name__)


@transaction.atomic
def add_page(request):
    if request.method == 'POST':
        form = PageForm(request.POST, request.FILES)
        formset = GalleryImageFormSet(request.POST, request.FILES)

        if form.is_valid() and formset.is_valid():
            page = form.save(commit=False)

            # Зберігаємо головне зображення
            main_image_id = form.cleaned_data['main_image']
            if main_image_id:
                try:
                    main_image = GalleryImage.objects.get(pk=main_image_id.id)
                    page.main_image = main_image
                except GalleryImage.DoesNotExist:
                    logger.error('Main image does not exist')
                    messages.error(request, 'Картинка не існує.')
                    return render(request, 'admin/pages/add_page.html', {'form': form, 'formset': formset})

            gallery = Gallery.objects.create()
            page.gallery = gallery
            page.save()

            formset.instance = gallery
            formset.save(commit=True)

            messages.success(request, 'Сторінку успішно додано.')
            return redirect('pages_list')
        else:
            messages.error(request, 'Форма або набір форм недійсні.')
    else:
        form = PageForm()
        formset = GalleryImageFormSet()

    return render(request, 'admin/pages/add_page.html', {'form': form, 'formset': formset})


# view for get template for success page
def page_success(request):
    return render(request, 'admin/pages/page_success.html')


# view for getting list of all pages
def get_page_list(request):
    if request.method == 'GET':
        page_list = Page.objects.all()

        pages_data = []
        for page in page_list:
            page_data = {
                'id': page.id,
                'name': page.name,
            }
            pages_data.append(page_data)

        return JsonResponse({'pages_list': pages_data})
    return JsonResponse({'error': 'Invalid request method'}, status=400)


def page_list_view(request):
    pages = Page.objects.all()
    return render(request, 'admin/pages/pages_list.html', {'pages': pages})


@transaction.atomic
def edit_page(request, page_id):
    page = get_object_or_404(Page, id=page_id)
    gallery = page.gallery

    if request.method == 'POST':
        form = PageForm(request.POST, request.FILES, instance=page)
        formset = GalleryImageFormSet(request.POST, request.FILES, instance=gallery)

        if form.is_valid() and formset.is_valid():
            page = form.save(commit=False)

            # Зберігаємо головне зображення
            new_main_image_id = form.cleaned_data.get('main_image')
            if new_main_image_id:
                try:
                    new_main_image = GalleryImage.objects.get(pk=new_main_image_id.id)
                    if page.main_image != new_main_image:
                        page.main_image = new_main_image
                except GalleryImage.DoesNotExist:
                    messages.error(request, 'Картинка не існує.')
                    return render(request, 'admin/pages/edit_page.html',
                                  {'form': form, 'formset': formset, 'page': page, 'gallery': gallery})
            else:
                # Якщо нове зображення не вибране, залишаємо старе
                page.main_image = page.main_image

            # Перевірка та збереження галереї
            if not gallery:
                gallery = Gallery.objects.create()
                page.gallery = gallery

            page.save()
            formset.instance = gallery
            formset.save()

            messages.success(request, 'Сторінку успішно оновлено.')
            return redirect('all_page_list')
        else:
            messages.error(request, 'Форма або набір форм недійсні.')
    else:
        form = PageForm(instance=page)
        formset = GalleryImageFormSet(instance=gallery)

    return render(request, 'admin/pages/edit_page.html', {'form': form, 'formset': formset, 'page': page})


# view for delete page from DB
def delete_page(request, page_id):
    page = get_object_or_404(Page, id=page_id)

    if request.method == 'POST':
        page.delete()
        return redirect('page_list')

    return render(request, 'admin/pages/confirm_delete_page.html', {'page': page})


def main_page(request):
    main_page_instance = MainPage.objects.first()

    if request.method == 'POST':
        form = MainPageForm(request.POST, request.FILES, instance=main_page_instance)

        if form.is_valid():
            main_page = form.save(commit=False)
            main_page.save()
            messages.success(request, 'Сторінка успішно збережена.')
            return redirect('pages_list')
        else:
            messages.error(request, 'Форма недійсна.')
    else:
        form = MainPageForm(instance=main_page_instance)

    return render(request, 'admin/main_page/main_page_admin.html', {'form': form})




@transaction.atomic
def contacts_view(request):
    seo_instance, created = SEOMixin.objects.get_or_create(id=1)

    if request.method == 'POST':
        logger.debug('Handling POST request')
        seo_form = SEOMixinForm(request.POST, instance=seo_instance)
        contact_formset = ContactsFormSet(request.POST, request.FILES, instance=seo_instance)

        if seo_form.is_valid() and contact_formset.is_valid():
            seo = seo_form.save()

            try:
                # Save the contacts formset
                instances = contact_formset.save(commit=False)
                for instance in instances:
                    instance.seo = seo  # Link the SEO instance to each contact
                    instance.save()
                for instance in contact_formset.deleted_objects:
                    instance.delete()
                contact_formset.save_m2m()

                messages.success(request, 'Контакти успішно оновлено')
                return redirect('pages_list')
            except Exception as e:
                logger.error('Error saving forms: %s', e)
                messages.error(request, 'Сталася помилка при збереженні контактів.')
        else:
            logger.warning('Form or formset invalid')
            logger.debug('SEO form errors: %s', seo_form.errors)
            logger.debug('Contact formset errors: %s', contact_formset.errors)
            logger.debug('SEO form cleaned data: %s', seo_form.cleaned_data)
            logger.debug('Contact formset cleaned data: %s', contact_formset.cleaned_data)
            messages.error(request, 'Форма або набір форм недійсні.')
    else:
        logger.debug('Handling GET request')
        seo_form = SEOMixinForm(instance=seo_instance)
        contact_formset = ContactsFormSet(instance=seo_instance)

    logger.debug('Rendering template with SEO form and contact formset')
    return render(request, 'admin/contacts/add_contacts.html', {
        'seo_form': seo_form,
        'contact_formset': contact_formset,
    })


def pages_list(request):
    context = {
        'pages_list': [
            {'name': 'Головна сторінка', 'edit_url': reverse('all_page_list')},
            {'name': 'Всі сторінки', 'edit_url': reverse('main_page')},
            {'name': 'Сторінка контактів', 'edit_url': reverse('add_contacts')}
        ]
    }
    return render(request, 'admin/pages.html', context)
