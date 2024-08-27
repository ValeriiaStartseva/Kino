import json
import os
from django.core.management.base import BaseCommand
from faker import Faker
from src.core.models import Gallery, GalleryImage
from src.movies.models import Movie
from src.cinemas.models import Cinema, Hall
from src.admin_pages.models import Page
from src.promotion.models import Post
from src.users.models import User
from src.showtimes.models import ShowTime
from django.core.files import File
from django.core.exceptions import ObjectDoesNotExist
import random
from django.utils import timezone


class Command(BaseCommand):
    help = 'Generates fake data and saves it to a JSON file'

    def handle(self, *args, **kwargs):
        fake = Faker()

        images_path = '/Users/valeriiastartseva/Desktop/kino_cms_gallery'  # path for img

        image_files = [f for f in os.listdir(images_path) if os.path.isfile(os.path.join(images_path, f))]

        if len(image_files) < 20:
            self.stdout.write(self.style.ERROR('Not enough image files found in the specified directory. Minimum 20 required.'))
            return

        # GalleryImage
        gallery_image_ids = []
        for image_file in image_files:
            image_full_path = os.path.join(images_path, image_file)

            with open(image_full_path, 'rb') as f:
                gallery_image = GalleryImage(
                    alt_text=fake.text(max_nb_chars=20),
                )
                gallery_image.image.save(image_file, File(f), save=True)
                gallery_image_ids.append(gallery_image.id)

            self.stdout.write(self.style.SUCCESS(f'Image "{image_file}" added to GalleryImage.'))

        self.stdout.write(self.style.SUCCESS('All images have been added to GalleryImage.'))

        # Перевіряємо, чи є достатньо зображень для усіх записів
        if len(gallery_image_ids) < 15:
            self.stdout.write(self.style.ERROR('Not enough images available to assign unique main images.'))
            return

        # Функція для додавання зображень в галерею
        def assign_gallery_images(gallery, image_count):
            selected_image_ids = gallery_image_ids[:image_count]
            gallery_image_ids[:] = gallery_image_ids[image_count:]
            for img_id in selected_image_ids:
                GalleryImage.objects.filter(pk=img_id).update(gallery=gallery)

        # Movie
        for _ in range(5):
            gallery = Gallery.objects.create()
            assign_gallery_images(gallery, 3)

            main_image_id = gallery_image_ids.pop(0)

            Movie.objects.create(
                name=fake.text(max_nb_chars=12),
                description=fake.text(),
                trailer=fake.url(),
                type=fake.random_element(elements=('IMAX', '2D', '3D')),
                gallery=gallery,
                main_image=GalleryImage.objects.get(pk=main_image_id),  # Використовуємо унікальне зображення
                url_seo=fake.url(),
                title_seo=fake.text(max_nb_chars=20),
                keywords_seo=fake.text(max_nb_chars=20),
                description_seo=fake.text(),
            )

        # Створюємо фейкові дані для моделі Cinema
        cinemas = []
        for _ in range(3):
            gallery = Gallery.objects.create()
            assign_gallery_images(gallery, 3)  # Прив'язуємо три зображення до галереї

            main_image_id = gallery_image_ids.pop(0)
            logo_image_id = gallery_image_ids.pop(0)

            cinema = Cinema.objects.create(
                name=fake.company()[:10],
                title=fake.catch_phrase()[:50],
                city=fake.city()[:12],
                gallery=gallery,
                main_image=GalleryImage.objects.get(pk=main_image_id),
                logo=GalleryImage.objects.get(pk=logo_image_id),
                url_seo=fake.url(),
                title_seo=fake.text(max_nb_chars=20),
                keywords_seo=fake.text(max_nb_chars=20),
                description_seo=fake.text(),
            )
            cinemas.append(cinema)

        # Hall
        for cinema in cinemas:
            gallery = Gallery.objects.create()

            if len(gallery_image_ids) >= 3:
                assign_gallery_images(gallery, 3)
            else:
                self.stdout.write(self.style.WARNING('Not enough images to assign to gallery for Hall. Skipping.'))
                continue

            if len(gallery_image_ids) > 0:
                main_image_id = gallery_image_ids.pop(0)
            else:
                self.stdout.write(self.style.WARNING('Not enough images left for main_image. Skipping.'))
                continue

            if len(gallery_image_ids) > 0:
                schema_picture_id = gallery_image_ids.pop(0)
            else:
                self.stdout.write(self.style.WARNING('Not enough images left for schema_picture. Skipping.'))
                continue

            Hall.objects.create(
                name=fake.text(max_nb_chars=20),
                description=fake.text(),
                schema_json=fake.json(),
                schema_picture=GalleryImage.objects.get(pk=schema_picture_id),
                gallery=gallery,
                main_image=GalleryImage.objects.get(pk=main_image_id),
                cinema_hall=cinema,
                url_seo=fake.url(),
                title_seo=fake.text(max_nb_chars=20),
                keywords_seo=fake.text(max_nb_chars=20),
                description_seo=fake.text(),
            )

        # User
        users = []
        for _ in range(5):
            user = User.objects.create(
                name=fake.first_name(),
                last_name=fake.last_name(),
                nickname=fake.user_name()[:10],
                email=fake.email(),
                address=fake.address()[:12],
                num_card=fake.credit_card_number()[:12],
                language=fake.random_element(elements=('ru', 'ua')),
                gender=fake.random_element(elements=('M', 'F')),
                phone=str(fake.phone_number()),
                date_birthday=fake.date_of_birth(),
                city=fake.city()[:12],
            )
            users.append({
                'name': user.name,
                'last_name': user.last_name,
                'nickname': user.nickname,
                'email': user.email,
                'address': user.address,
                'num_card': user.num_card,
                'language': user.language,
                'gender': user.gender,
                'phone': str(user.phone),
                'date_birthday': user.date_birthday.isoformat(),
                'city': user.city,
            })
            self.stdout.write(self.style.SUCCESS(f'User "{user.email}" added to User model.'))

        # Post
        posts = []
        for _ in range(3):
            gallery = Gallery.objects.create()
            assign_gallery_images(gallery, 3)

            main_image_id = gallery_image_ids.pop(0)

            post = Post.objects.create(
                name=fake.text(max_nb_chars=40),
                published_date=fake.date_this_year().isoformat(),
                description=fake.text(),
                status=fake.boolean(),
                link=fake.url(),
                type=fake.random_element(elements=('news', 'prom')),
                gallery=gallery,
                main_image=GalleryImage.objects.get(pk=main_image_id),
                url_seo=fake.url(),
                title_seo=fake.text(max_nb_chars=20),
                keywords_seo=fake.text(max_nb_chars=20),
                description_seo=fake.text(),
            )
            posts.append(post)

        # Page
        pages = []
        for _ in range(3):
            gallery = Gallery.objects.create()
            assign_gallery_images(gallery, 3)

            main_image_id = gallery_image_ids.pop(0)

            page = Page.objects.create(
                name=fake.text(max_nb_chars=12),
                description=fake.text(),
                created_at=fake.date_time_this_year().isoformat(),
                status=fake.boolean(),
                gallery=gallery,
                main_image=GalleryImage.objects.get(pk=main_image_id),
                url_seo=fake.url(),
                title_seo=fake.text(max_nb_chars=20),
                keywords_seo=fake.text(max_nb_chars=20),
                description_seo=fake.text(),
            )
            pages.append(page)

        # ShowTime
        movies = Movie.objects.all()
        halls = Hall.objects.all()

        if not movies.exists() or not halls.exists():
            print("Недостатньо даних для створення сеансів.")
        else:
            for _ in range(100):  # Збільшуємо кількість згенерованих сеансів
                movie = random.choice(movies)
                hall = random.choice(halls)

                # Створюємо дату з урахуванням часової зони, яку повертає Django
                show_time = timezone.make_aware(fake.date_time_between(start_date='now', end_date='+30d'),
                                                timezone.get_current_timezone())

                # Генеруємо випадкову ціну в діапазоні від 60 до 150
                price = random.randint(60, 150)

                # Зберігаємо новий запис ShowTime з ціною
                ShowTime.objects.create(
                    hall_id=hall,
                    movie_id=movie,
                    show_time=show_time,
                    price=price
                )
                print(f"Створено сеанс: {show_time}, ціна: {price}")

        # Перевірка на наявність моделей перед записом в JSON
        try:
            movies = [movie.name for movie in Movie.objects.all()]
        except ObjectDoesNotExist:
            movies = []

        try:
            cinemas = [cinema.name for cinema in Cinema.objects.all()]
        except ObjectDoesNotExist:
            cinemas = []

        try:
            halls = [hall.name for hall in Hall.objects.all()]
        except ObjectDoesNotExist:
            halls = []

        try:
            posts_data = [post.name for post in Post.objects.all()]
        except ObjectDoesNotExist:
            posts_data = []

        try:
            pages_data = [page.name for page in Page.objects.all()]
        except ObjectDoesNotExist:
            pages_data = []

        data = {
            'movies': movies,
            'cinemas': cinemas,
            'halls': halls,
            'users': users,
            'posts': posts_data,
            'pages': pages_data,
        }

        with open('fake_data.json', 'w') as f:
            json.dump(data, f, indent=4)

        self.stdout.write(self.style.SUCCESS('Data generated and saved to fake_data.json'))
