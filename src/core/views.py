import json

from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.template.loader import render_to_string

from .forms import GalleryImageForm
from .models import GalleryImage, Gallery
from django.http import JsonResponse
from src.movies.models import Movie
from ..admin_pages.models import Page
from ..banners.models import MainPageBanners, MainPageNewsBanners
from ..cinemas.models import Cinema, Hall
from ..showtimes.models import ShowTime
from datetime import date, timedelta
from django.core.paginator import Paginator
from django.shortcuts import render
from src.promotion.models import Post
from django.db.models import Q
from src.showtimes.models import Ticket
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


def home_page(request):
    today = date.today()
    tomorrow = today + timedelta(days=1)
    carousel_big_banner = MainPageBanners.objects.filter(status=True).prefetch_related('banner_images')
    carousel_news = MainPageNewsBanners.objects.filter(status=True).prefetch_related('news_images')

    # today's movies
    today_showtimes = ShowTime.objects.filter(show_time__date=today)
    movies_dict = {}
    for showtime in today_showtimes:
        movie_id = showtime.movie_id.id
        if movie_id not in movies_dict:
            movies_dict[movie_id] = {
                'title': showtime.movie_id.name,
                'poster_url': showtime.movie_id.main_image.image.url,
                'slug': showtime.movie_id.slug,  # Додаємо slug
                'showtime': showtime,
            }
    movies = list(movies_dict.values())

    # soon movies
    future_showtimes = ShowTime.objects.filter(show_time__date__gte=tomorrow)
    soon_movies_dict = {}
    for showtime in future_showtimes:
        movie_id = showtime.movie_id.id
        if movie_id not in soon_movies_dict:
            soon_movies_dict[movie_id] = {
                'title': showtime.movie_id.name,
                'poster_url': showtime.movie_id.main_image.image.url,
                'show_time': showtime.show_time,
                'slug': showtime.movie_id.slug,  # Додаємо slug
                'showtime': showtime,   # Додаємо сеанси
            }
    soon_movies = list(soon_movies_dict.values())

    context = {
        'movies': movies,
        'today': today,
        'soon_movies': soon_movies,
        'carousel_big_banner': carousel_big_banner,
        'carousel_news': carousel_news,
    }

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

    return render(request, 'pages/contacts_cinema.html', {'cinemas': cinemas})


# def movie_detail(request, slug):
#     movie = Movie.objects.get(slug=slug)
#     cinemas = Cinema.objects.filter(halls__showtime__movie_id=movie.id).distinct()
#     showtimes = ShowTime.objects.filter(movie_id=movie.id)
#
#     context = {
#         'movie': movie,
#         'cinemas': cinemas,
#         'showtimes': showtimes,
#     }
#     return render(request, 'pages/movie_page.html', context)

def movie_detail(request, slug):
    movie = Movie.objects.get(slug=slug)
    cinemas = Cinema.objects.filter(halls__showtime__movie_id=movie.id).distinct()

    selected_cinema = request.GET.get('cinema')
    selected_format = request.GET.getlist('format')

    showtimes = ShowTime.objects.filter(movie_id=movie.id)

    # Apply filters if selected
    if selected_cinema:
        showtimes = showtimes.filter(hall_id__cinema_hall_id=selected_cinema)

    if selected_format:
        query = Q()
        for format in selected_format:
            query |= Q(movie_type__icontains=format)
        showtimes = showtimes.filter(query)

    context = {
        'movie': movie,
        'cinemas': cinemas,
        'showtimes': showtimes,
        'selected_cinema': selected_cinema,
        'selected_format': selected_format,
    }
    return render(request, 'pages/movie_page.html', context)


def cinema_detail(request, slug):
    cinema = get_object_or_404(Cinema, slug=slug)
    showtimes = ShowTime.objects.filter(hall_id__cinema_hall=cinema)
    pages = Page.objects.filter(status=True)

    context = {
        'cinema': cinema,
        'showtimes': showtimes,
        'pages': pages,
    }
    return render(request, 'pages/cinema_page.html', context)


def hall_detail(request, slug):
    hall = get_object_or_404(Hall, slug=slug)
    showtimes = ShowTime.objects.filter(hall_id=hall)

    context = {
        'hall': hall,
        'showtimes': showtimes,
    }
    return render(request, 'pages/hall_page.html', context)


def billboard(request):
    today = date.today()
    showtimes = ShowTime.objects.filter(show_time__date=today).select_related('movie_id').order_by('movie_id')

    # Використовуємо множину для уникнення дублікатів
    seen_movies = set()
    movies = []
    for showtime in showtimes:
        if showtime.movie_id not in seen_movies:
            movies.append(showtime.movie_id)
            seen_movies.add(showtime.movie_id)

    context = {
        'movies': movies,
    }
    return render(request, 'pages/billboard.html', context)


def coming_soon(request):
    tomorrow = date.today() + timedelta(days=1)
    showtimes = ShowTime.objects.filter(show_time__gte=tomorrow).select_related('movie_id').order_by('movie_id',
                                                                                                     'show_time')

    seen_movies = set()
    movies = []
    for showtime in showtimes:
        if showtime.movie_id not in seen_movies:
            showtime.movie_id.first_showtime = showtime.show_time
            movies.append(showtime.movie_id)
            seen_movies.add(showtime.movie_id)

    context = {
        'movies': movies,
    }
    return render(request, 'pages/coming_soon_page.html', context)



def page_detail(request, slug):
    page = get_object_or_404(Page, slug=slug)
    return render(request, 'pages/page_detail.html', {'page': page})


def promotions(request):
    posts = Post.objects.filter(type='prom', status=True).order_by('-published_date')
    paginator = Paginator(posts, 6)  # по 6 постів на сторінку

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'pages/promotions.html', {'posts': page_obj})


def news(request):
    posts = Post.objects.filter(type='news', status=True).order_by('-published_date')
    paginator = Paginator(posts, 6)  # по 6 постів на сторінку

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'pages/news.html', {'posts': page_obj})


def promotion_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, status=True)
    return render(request, 'pages/prom_page.html', {'post': post})


def news_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, status=True)
    return render(request, 'pages/news_page.html', {'post': post})


from datetime import datetime, timedelta
from django.db.models import Q
from django.shortcuts import render


def timetable_view(request):
    selected_cinema = request.GET.get('cinema')
    selected_date = request.GET.get('date')
    selected_formats = request.GET.getlist('format')
    selected_hall = request.GET.get('hall')

    # Отримати всі сеанси за наступні 7 днів
    today = datetime.today().date()
    end_date = today + timedelta(days=7)
    showtimes = ShowTime.objects.filter(show_time__date__range=[today, end_date])

    # Застосування фільтрів, якщо вони обрані
    if selected_cinema:
        showtimes = showtimes.filter(hall_id__cinema_hall_id=selected_cinema)

    if selected_date:
        showtimes = showtimes.filter(show_time__date=selected_date)

    if selected_formats:
        query = Q()
        for format in selected_formats:
            query |= Q(movie_type__icontains=format)
        showtimes = showtimes.filter(query)

    if selected_hall:
        showtimes = showtimes.filter(hall_id_id=selected_hall)

    # Групування сеансів за датою
    showtimes_by_date = {}
    for showtime in showtimes:
        date = showtime.show_time.date()
        if date not in showtimes_by_date:
            showtimes_by_date[date] = []
        showtimes_by_date[date].append(showtime)

    context = {
        'cinemas': Cinema.objects.all(),
        'halls': Hall.objects.all(),
        'showtimes': [{'date': date, 'sessions': sessions} for date, sessions in showtimes_by_date.items()],
        'selected_cinema': selected_cinema,
        'selected_date': selected_date,
        'selected_formats': selected_formats,
        'selected_hall': selected_hall,
    }

    return render(request, 'pages/timetable.html', context)


from django.shortcuts import render, get_object_or_404, redirect
from src.showtimes.models import ShowTime
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

def booking_view(request, showtime_id):
    showtime = get_object_or_404(ShowTime, id=showtime_id)
    booked_tickets = Ticket.objects.filter(show_time_id=showtime)

    hall_schema = showtime.hall_id.schema_json

    # Оновлюємо статус місць у JSON
    for row in hall_schema['rows']:
        for seat in row['seats']:
            if booked_tickets.filter(row=row['row_number'], seat=seat['seat_number']).exists():
                seat['status'] = 'reserved'

    if request.method == 'POST' and request.user.is_authenticated:
        selected_seats = request.POST.getlist('selected_seats')

        for seat in selected_seats:
            row, seat_number = seat.split(',')
            Ticket.objects.create(
                show_time_id=showtime,
                row=int(row),
                seat=int(seat_number),
                user=request.user
            )
        return redirect('booking', showtime_id=showtime_id)  # Перезавантаження сторінки після бронювання

    context = {
        'showtime': showtime,
        'hall_schema': hall_schema,
    }

    return render(request, 'pages/book_ticket.html', context)




