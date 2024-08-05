from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from src.core.forms import GalleryImageFormSet
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Post
from .forms import PostForm, GalleryImageFormSet
from django.db import transaction
from src.core.models import GalleryImage, Gallery
import logging

logger = logging.getLogger(__name__)


@transaction.atomic
def add_post(request):
    logger.debug('Request method: %s', request.method)
    if request.method == 'POST':
        logger.debug('POST data: %s', request.POST)
        logger.debug('FILES data: %s', request.FILES)

        form = PostForm(request.POST, request.FILES)
        formset = GalleryImageFormSet(request.POST, request.FILES)

        if form.is_valid():
            logger.debug('PageForm is valid')
        else:
            logger.debug('PageForm errors: %s', form.errors)

        if formset.is_valid():
            logger.debug('GalleryImageFormSet is valid')
        else:
            logger.debug('GalleryImageFormSet errors: %s', formset.errors)

        if form.is_valid() and formset.is_valid():
            page = form.save(commit=False)
            logger.debug('Page form saved with commit=False')

            # Зберігаємо головне зображення
            main_image_id = form.cleaned_data['main_image']
            logger.debug('Main image id: %s', main_image_id)
            if main_image_id:
                try:
                    main_image = GalleryImage.objects.get(pk=main_image_id.id)
                    logger.debug('Main image object: %s', main_image)
                    page.main_image = main_image
                except GalleryImage.DoesNotExist:
                    logger.error('Main image does not exist')
                    messages.error(request, 'Картинка не існує.')
                    return render(request, 'admin/add_post.html', {'form': form, 'formset': formset})

            gallery = Gallery.objects.create()
            logger.debug('Gallery object created: %s', gallery)
            page.gallery = gallery
            page.save()
            logger.debug('Page object saved: %s', page)

            formset.instance = gallery
            formset.save(commit=True)
            logger.debug('GalleryImageFormSet saved')

            messages.success(request, 'Сторінку успішно додано.')
            return redirect('post_list')
        else:
            messages.error(request, 'Форма або набір форм недійсні.')
    else:
        form = PostForm()
        formset = GalleryImageFormSet()

    logger.debug('Rendering add_page template')
    return render(request, 'admin/add_post.html', {'form': form, 'formset': formset})


def post_success(request):
    return render(request, 'admin/post_success.html')


def get_post_list(request):
    if request.method == 'GET':
        post_list = Post.objects.all()

        posts_data = []
        for post in post_list:
            page_data = {
                'id': post.id,
                'name': post.name,
            }
            posts_data.append(page_data)

        return JsonResponse({'pages_list': posts_data})
    return JsonResponse({'error': 'Invalid request method'}, status=400)


def post_list_view(request):
    posts = Post.objects.all()
    return render(request, 'admin/posts_list.html', {'posts': posts})


@transaction.atomic
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    gallery = post.gallery

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        formset = GalleryImageFormSet(request.POST, request.FILES, instance=gallery)

        if form.is_valid() and formset.is_valid():
            post = form.save(commit=False)

            # Зберігаємо головне зображення
            new_main_image_id = form.cleaned_data.get('main_image')
            if new_main_image_id:
                try:
                    new_main_image = GalleryImage.objects.get(pk=new_main_image_id.id)
                    if post.main_image != new_main_image:
                        post.main_image = new_main_image
                except GalleryImage.DoesNotExist:
                    messages.error(request, 'Картинка не існує.')
                    return render(request, 'admin/edit_post.html',
                                  {'form': form, 'formset': formset, 'post': post, 'gallery': gallery})
            else:
                # Якщо нове зображення не вибране, залишаємо старе
                post.main_image = post.main_image

            # Перевірка та збереження галереї
            if not gallery:
                gallery = Gallery.objects.create()
                post.gallery = gallery

            post.save()
            formset.instance = gallery
            formset.save()

            messages.success(request, 'Пост успішно оновлено.')
            return redirect('post_list')
        else:
            messages.error(request, 'Форма або набір форм недійсні.')
    else:
        form = PostForm(instance=post)
        formset = GalleryImageFormSet(instance=gallery)

    return render(request, 'admin/edit_post.html', {'form': form, 'formset': formset, 'post': post, 'gallery': gallery})


# view for delete post from DB
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        post.delete()
        return redirect('post_list')

    return render(request, 'admin/confirm_delete_post.html', {'post': post})


