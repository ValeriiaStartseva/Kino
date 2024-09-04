from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from src.core.forms import GalleryImageFormSet
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Post
from .forms import PostForm, GalleryImageFormSet
from django.db import transaction
from src.core.models import GalleryImage, Gallery

@login_required
@transaction.atomic
def add_post(request):

    if request.method == 'POST':

        form = PostForm(request.POST, request.FILES)
        formset = GalleryImageFormSet(request.POST, request.FILES)

        if form.is_valid() and formset.is_valid():

            page = form.save(commit=False)

            # save main img
            main_image_id = form.cleaned_data['main_image']

            if main_image_id:
                try:
                    main_image = GalleryImage.objects.get(pk=main_image_id.id)

                    page.main_image = main_image
                except GalleryImage.DoesNotExist:

                    messages.error(request, 'Image not found')
                    return render(request, 'admin/add_post.html', {'form': form, 'formset': formset})

            gallery = Gallery.objects.create()

            page.gallery = gallery
            page.save()

            formset.instance = gallery
            formset.save(commit=True)


            messages.success(request, 'Page added successfully')
            return redirect('post_list')
        else:
            messages.error(request, 'Form or formset is not valid')
    else:
        form = PostForm()
        formset = GalleryImageFormSet()

    return render(request, 'admin/add_post.html', {'form': form, 'formset': formset})

@login_required
def post_success(request):
    return render(request, 'admin/post_success.html')

@login_required
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

@login_required
def post_list_view(request):
    posts = Post.objects.all()
    return render(request, 'admin/posts_list.html', {'posts': posts})

@login_required
@transaction.atomic
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    gallery = post.gallery

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        formset = GalleryImageFormSet(request.POST, request.FILES, instance=gallery)

        if form.is_valid() and formset.is_valid():
            post = form.save(commit=False)

            # save main img
            new_main_image_id = form.cleaned_data.get('main_image')
            if new_main_image_id:
                try:
                    new_main_image = GalleryImage.objects.get(pk=new_main_image_id.id)
                    if post.main_image != new_main_image:
                        post.main_image = new_main_image
                except GalleryImage.DoesNotExist:
                    messages.error(request, 'Image does not exist')
                    return render(request, 'admin/edit_post.html',
                                  {'form': form, 'formset': formset, 'post': post, 'gallery': gallery})
            else:

                post.main_image = post.main_image

            if not gallery:
                gallery = Gallery.objects.create()
                post.gallery = gallery

            post.save()
            formset.instance = gallery
            formset.save()

            messages.success(request, 'Post added successfully.')
            return redirect('post_list')
        else:
            messages.error(request, 'Form and formset are not valid.')
    else:
        form = PostForm(instance=post)
        formset = GalleryImageFormSet(instance=gallery)

    return render(request, 'admin/edit_post.html',
                  {'form': form, 'formset': formset, 'post': post, 'gallery': gallery})


# view for delete post from DB
@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        post.delete()
        return redirect('post_list')

    return render(request, 'admin/confirm_delete_post.html', {'post': post})


