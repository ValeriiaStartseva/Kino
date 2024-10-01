import os
import random
from django.core.files import File
from django.core.management.base import BaseCommand
from django.utils import timezone
from faker import Faker
from src.core.models import Gallery, GalleryImage
from src.movies.models import Movie
from src.cinemas.models import Cinema, Hall
from src.admin_pages.models import Page
from src.promotion.models import Post
from src.users.models import User
from src.showtimes.models import ShowTime


class Command(BaseCommand):
    help = 'Generates fake data and saves it directly to the database'

    def handle(self, *args, **kwargs):
        self.fake = Faker()

        images_path = '/KinoCMS/gallery'

        image_files = self._get_image_files(images_path)
        if not image_files:
            return

        self.gallery_image_ids = self._create_gallery_images(image_files, images_path)
        if not self.gallery_image_ids:
            return

        self._create_movies()
        self._create_cinemas()
        self._create_halls()
        self._create_users()
        self._create_posts()
        self._create_pages()
        self._create_showtimes()

    def _get_image_files(self, images_path):
        image_files = [f for f in os.listdir(images_path) if os.path.isfile(os.path.join(images_path, f))]

        if len(image_files) < 20:
            self.stdout.write(self.style.ERROR('Not enough image files found in the specified directory.'))
            return None

        return image_files

    def _create_gallery_images(self, image_files, images_path):
        gallery_image_ids = []
        for image_file in image_files:
            image_full_path = os.path.join(images_path, image_file)

            # Get the file name without extension to use as alt-text
            alt_text = os.path.splitext(image_file)[0]

            with open(image_full_path, 'rb') as f:
                gallery_image = GalleryImage(
                    alt_text=alt_text[:20],
                )
                gallery_image.image.save(image_file, File(f), save=True)
                gallery_image_ids.append(gallery_image.id)

            self.stdout.write(self.style.SUCCESS(f'Image "{image_file}" added to GalleryImage with alt-text "{alt_text}".'))

        if len(gallery_image_ids) < 15:
            self.stdout.write(self.style.ERROR('Not enough images available to assign unique main images.'))
            return None

        return gallery_image_ids

    def _assign_gallery_images(self, gallery, image_count):
        selected_image_ids = self.gallery_image_ids[:image_count]
        self.gallery_image_ids = self.gallery_image_ids[image_count:]
        for img_id in selected_image_ids:
            GalleryImage.objects.filter(pk=img_id).update(gallery=gallery)

    def _create_movies(self):
        for _ in range(5):
            gallery = Gallery.objects.create()
            self._assign_gallery_images(gallery, 3)

            main_image_id = self.gallery_image_ids.pop(0)

            Movie.objects.create(
                name=self.fake.text(max_nb_chars=12),
                description=self.fake.text(),
                trailer=self.fake.url(),
                type=self.fake.random_element(elements=('IMAX', '2D', '3D')),
                gallery=gallery,
                main_image=GalleryImage.objects.get(pk=main_image_id),
                url_seo=self.fake.url(),
                title_seo=self.fake.text(max_nb_chars=20),
                keywords_seo=self.fake.text(max_nb_chars=20),
                description_seo=self.fake.text(),
            )

    def _create_cinemas(self):
        self.cinemas = []
        for _ in range(3):
            gallery = Gallery.objects.create()
            self._assign_gallery_images(gallery, 3)

            main_image_id = self.gallery_image_ids.pop(0)
            logo_image_id = self.gallery_image_ids.pop(0)

            cinema = Cinema.objects.create(
                name=self.fake.company()[:10],
                title=self.fake.catch_phrase()[:50],
                city=self.fake.city()[:12],
                gallery=gallery,
                main_image=GalleryImage.objects.get(pk=main_image_id),
                logo=GalleryImage.objects.get(pk=logo_image_id),
                url_seo=self.fake.url(),
                title_seo=self.fake.text(max_nb_chars=20),
                keywords_seo=self.fake.text(max_nb_chars=20),
                description_seo=self.fake.text(),
            )
            self.cinemas.append(cinema)

    def _create_halls(self):
        for cinema in self.cinemas:
            gallery = Gallery.objects.create()

            if len(self.gallery_image_ids) >= 3:
                self._assign_gallery_images(gallery, 3)
            else:
                self.stdout.write(self.style.WARNING('Not enough images to assign to gallery for Hall. Skipping.'))
                continue

            if len(self.gallery_image_ids) > 0:
                main_image_id = self.gallery_image_ids.pop(0)
            else:
                self.stdout.write(self.style.WARNING('Not enough images left for main_image. Skipping.'))
                continue

            if len(self.gallery_image_ids) > 0:
                schema_picture_id = self.gallery_image_ids.pop(0)
            else:
                self.stdout.write(self.style.WARNING('Not enough images left for schema_picture. Skipping.'))
                continue

            Hall.objects.create(
                name=self.fake.text(max_nb_chars=20),
                description=self.fake.text(),
                schema_json=self.fake.json(),
                schema_picture=GalleryImage.objects.get(pk=schema_picture_id),
                gallery=gallery,
                main_image=GalleryImage.objects.get(pk=main_image_id),
                cinema_hall=cinema,
                url_seo=self.fake.url(),
                title_seo=self.fake.text(max_nb_chars=20),
                keywords_seo=self.fake.text(max_nb_chars=20),
                description_seo=self.fake.text(),
            )

    def _create_users(self):
        self.users = []
        for _ in range(5):
            user = User.objects.create(
                name=self.fake.first_name(),
                last_name=self.fake.last_name(),
                nickname=self.fake.user_name()[:10],
                email=self.fake.email(),
                address=self.fake.address()[:12],
                num_card=self.fake.credit_card_number()[:12],
                language=self.fake.random_element(elements=('ru', 'ua')),
                gender=self.fake.random_element(elements=('M', 'F')),
                phone=str(self.fake.phone_number()),
                date_birthday=self.fake.date_of_birth(),
                city=self.fake.city()[:12],
            )
            self.users.append(user)
            self.stdout.write(self.style.SUCCESS(f'User "{user.email}" added to User model.'))

    def _create_pages(self):
        self.pages = []
        for _ in range(3):
            gallery = Gallery.objects.create()
            self._assign_gallery_images(gallery, 3)

            main_image_id = self.gallery_image_ids.pop(0)

            page = Page.objects.create(
                name=self.fake.text(max_nb_chars=12),
                description=self.fake.text(),
                created_at=self.fake.date_time_this_year().isoformat(),
                status=self.fake.boolean(),
                gallery=gallery,
                main_image=GalleryImage.objects.get(pk=main_image_id),
                url_seo=self.fake.url(),
                title_seo=self.fake.text(max_nb_chars=20),
                keywords_seo=self.fake.text(max_nb_chars=20),
                description_seo=self.fake.text(),
            )
            self.pages.append(page)

    def _create_showtimes(self):
        movies = Movie.objects.all()
        halls = Hall.objects.all()

        if not movies.exists() or not halls.exists():
            self.stdout.write(self.style.WARNING("Not enough data to create showtimes."))
            return

        for _ in range(100):
            movie = random.choice(movies)
            hall = random.choice(halls)

            show_time = timezone.make_aware(
                self.fake.date_time_between(start_date='now', end_date='+30d'),
                timezone.get_current_timezone()
            )

            price = random.randint(60, 150)

            ShowTime.objects.create(
                hall_id=hall,
                movie_id=movie,
                show_time=show_time,
                price=price,
                movie_type=random.choice(['IMAX', '2D', '3D'])
            )
            self.stdout.write(self.style.SUCCESS(f"Showtime created: {show_time}, Price: {price}"))
