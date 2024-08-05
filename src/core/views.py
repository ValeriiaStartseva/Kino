from datetime import date
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import GalleryImageForm, GalleryImageFormSet
from .models import GalleryImage, Gallery
from django.http import JsonResponse
from src.movies.models import Movie


# вью для сторінки завантаження картинок в БД
def upload_image(request):
    if request.method == 'POST':
        form = GalleryImageForm(request.POST, request.FILES)

        if form.is_valid():
            instance = form.save()
            messages.success(request, "Зображення успішно завантажено.")
            return JsonResponse({'id': instance.id, 'alt_text': instance.alt_text})
        else:
            errors = form.errors.as_json()
            messages.error(request, "Зображення не завантажено.")
            return JsonResponse({'errors': errors}, status=400)
    else:
        form = GalleryImageForm()

    return render(request, 'admin/upload_image.html', {'form': form})


# вью для отримання картинок з БД у JSON форматі
def get_gallery_images(request):
    if request.method == 'GET':
        gallery_images = GalleryImage.objects.filter(gallery_id__isnull=True)

        images_data = []
        for image in gallery_images:
            image_data = {
                'id': image.id,
                'alt_text': image.alt_text,
                'image_url': image.image.url if image.image else None
            }
            images_data.append(image_data)

        return JsonResponse({'gallery_images': images_data})

    return JsonResponse({'error': 'Invalid request method'}, status=400)


def gallery_view(request, gallery_id):
    print(f"Fetching gallery with ID: {gallery_id}")
    gallery = get_object_or_404(Gallery, id=gallery_id)
    images = GalleryImage.objects.filter(gallery=gallery)
    print(f"Gallery ID: {gallery.id}, Number of Images: {images.count()}")

    return render(request, 'admin/elements/gallery_img_elements/gallery_carousel_edit.html', {
        'gallery': gallery,
        'images': images,
    })

# статичні функції для відображення на сторінках, потім приберуться
def home_page(request):
    today = date.today()
    movies = [
        {
            'title': 'Інтерстелар',
            'poster_url': '/static/images/movie_posters/inter_poster.png',
        },
        {
            'title': 'Каскадер',
            'poster_url': '/static/images/movie_posters/fall_guy_poster.jpeg',
        },
        {
            'title': 'Прибуття',
            'poster_url': '/static/images/movie_posters/arrival_vertical.jpeg',
        },
    ]

    soon_movies = [
        {
            'title': 'Барбі',
            'poster_url': '/static/images/movie_posters/barbi.jpeg',
        },
        {
            'title': 'Бетмен',
            'poster_url': '/static/images/movie_posters/batman.png',
        },
        {
            'title': 'Дюна',
            'poster_url': '/static/images/movie_posters/duna.jpeg',
        },
        {
            'title': 'Годзілла',
            'poster_url': '/static/images/movie_posters/godzilla.jpeg',
        },
        {
            'title': 'Острів проклятих',
            'poster_url': '/static/images/movie_posters/island_di.jpeg',
        },
        {
            'title': 'Матриця',
            'poster_url': '/static/images/movie_posters/matrix.png',
        },
    ]
    carousel_big_banner = [
        {
            'caption': 'Інтерстеллар',
            'poster_url': '/static/images/movie_banners/inter.jpeg',
            'url': '#'
        },
        {
            'title': 'Каскадер',
            'poster_url': '/static/images/movie_banners/gall_guy.jpeg',
            'url': '#'
        },
        {
            'title': 'Прибуття',
            'poster_url': '/static/images/movie_banners/arrival.jpeg',
            'url': '#'
        },

    ]
    carousel_news = [
        {
            'caption': 'Новина',
            'poster_url': '/static/images/movie_banners/news.jpeg',
            'url': '#'
        },
        {
            'title': 'Акція',
            'poster_url': '/static/images/movie_banners/prom.jpeg',
            'url': '#'
        },

    ]

    context = {'movies': movies, 'today': today, 'soon_movies': soon_movies, 'carousel_big_banner': carousel_big_banner,
               'carousel_news': carousel_news}

    return render(request, 'pages/home_page.html', context)


def contact(request):
    cinemas = [
        {
            'cinema_name': 'Супутник',
            'cinema_name_contacts': 'Супутник',
            'adress_cinema_contacts': '',
            'numbers_contacts': '',
            'email_cinema_contacts': '',

            'coordinates': {
                'lng': '30.4579113',
                'lat': '50.4381375',
            },
            'logo_url': '/static/images/site_icons/suputnik_logo.png'
        },
        {
            'cinema_name': 'Кіноман',
            'adress_cinema_contacts': 'Київ, вул. Вадима Гетьмана, 6. Блок С',
            'numbers_contacts': '+3 (067) 449-25-92',
            'email_cinema_contacts': 'info-cosmopolite@kinoman.ua',
            'coordinates': {
                'lng': '30.4412593',
                'lat': '50.4505637',
            },
            'logo_url': ''
        },
        {
            'cinema_name': 'Мультиплекс',
            'cinema_name_contacts': 'Кіноман',
            'adress_cinema_contacts': 'Київ, вул. Вадима Гетьмана, 6. Блок С',
            'numbers_contacts': 'Бронювання квитків: +3 (067) 449-25-92',
            'email_cinema_contacts': 'info-cosmopolite@kinoman.ua',
            'coordinates': {
                'lng': '30.3614336',
                'lat': '50.4505346',
            },
            'logo_url': ''
        }
    ]

    return render(request, 'pages/contacts.html', {'cinemas': cinemas})


def news_and_adv(request):
    return render(request, 'pages/news.html')


def mob_app(request):
    return render(request, 'pages/mob-app.html')


def cinema_rooms(request):
    return render(request, 'pages/cinema_rooms.html')



