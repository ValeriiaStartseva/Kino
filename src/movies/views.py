from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from src.core.forms import GalleryImageFormSet
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Movie, Gallery, GalleryImage
from .forms import MovieForm, GalleryImageFormSet
from django.db import transaction
from django.contrib.auth.decorators import login_required
from django.utils import translation


@login_required
@transaction.atomic
def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        formset = GalleryImageFormSet(request.POST, request.FILES)

        if form.is_valid() and formset.is_valid():
            movie = form.save(commit=False)

            # save main img
            main_image_id = form.cleaned_data['main_image']
            if main_image_id:
                try:
                    main_image = GalleryImage.objects.get(pk=main_image_id.id)
                    movie.main_image = main_image
                except GalleryImage.DoesNotExist:
                    messages.error(request, 'Image does not exist.')
                    return render(request, 'admin/add_movie.html', {'form': form, 'formset': formset})

            gallery = Gallery.objects.create()
            movie.gallery = gallery
            movie.save()

            formset.instance = gallery
            formset.save(commit=True)

            messages.success(request, 'Movie successfully added!')
            return redirect('movie_list')
        else:
            messages.error(request, 'Form or formset is invalid.')
    else:
        form = MovieForm()
        formset = GalleryImageFormSet()

    return render(request, 'admin/add_movie.html', {'form': form, 'formset': formset})


# # view for get template for success movie page
# @login_required
# def movie_success(request):
#     return render(request, 'admin/movie_success.html')


# view for getting list of all movies
@login_required
def get_movie_list(request):
    if request.method == 'GET':
        movie_list = Movie.objects.all()

        movies_data = []
        for movie in movie_list:
            movie_data = {
                'id': movie.id,
                'name': movie.name,
            }
            movies_data.append(movie_data)

        return JsonResponse({'movies_list': movies_data})
    return JsonResponse({'error': 'Invalid request method'}, status=400)

@login_required
def movie_list_view(request):
    movies = Movie.objects.all()
    return render(request, 'admin/movies_list.html', {'movies': movies})

@login_required
@transaction.atomic
def edit_movie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    gallery = movie.gallery

    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES, instance=movie)
        formset = GalleryImageFormSet(request.POST, request.FILES, instance=gallery)

        if form.is_valid() and formset.is_valid():
            movie = form.save(commit=False)

            # save main img
            new_main_image_id = form.cleaned_data.get('main_image')
            if new_main_image_id:
                try:
                    new_main_image = GalleryImage.objects.get(pk=new_main_image_id.id)
                    if movie.main_image != new_main_image:
                        movie.main_image = new_main_image
                except GalleryImage.DoesNotExist:
                    messages.error(request, 'Image not found')
                    return render(request, 'admin/edit_movie.html',
                                  {'form': form, 'formset': formset, 'movie': movie, 'gallery': gallery})
            else:
                movie.main_image = movie.main_image

            if not gallery:
                gallery = Gallery.objects.create()
                movie.gallery = gallery

            movie.save()
            formset.instance = gallery
            formset.save()

            messages.success(request, 'Movie edited')
            return redirect('movie_list')
        else:
            messages.error(request, 'Form or formset not valid')
    else:
        form = MovieForm(instance=movie)
        formset = GalleryImageFormSet(instance=gallery)

    return render(request, 'admin/edit_movie.html', {'form': form, 'formset': formset,
                                                     'movie': movie})


# view for delete movie from DB
@login_required
def delete_movie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)

    if request.method == 'POST':
        movie.delete()
        return redirect('movie_list')

    return render(request, 'admin/confirm_delete.html', {'movie': movie})

