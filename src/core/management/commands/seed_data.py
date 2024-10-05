import random
from django.core.management.base import BaseCommand
from django.utils import timezone
from faker import Faker
from src.movies.models import Movie
from src.cinemas.models import Cinema, Hall
from src.admin_pages.models import Page
from src.users.models import User
from src.showtimes.models import ShowTime


class Command(BaseCommand):
    help = 'Generates fake data and saves it directly to the database'

    def handle(self, *args, **kwargs):
        self.fake = Faker()

        # Створюємо фільми, кінотеатри та зали
        self._create_movies()
        self._create_cinemas()
        self._create_halls()

        # Тепер створюємо сеанси
        self._create_showtimes()

        # Додаємо додаткові моделі
        self._create_users()
        self._create_pages()

    def _create_movies(self):
        self.movies = []
        for _ in range(5):
            movie = Movie.objects.create(
                name=self.fake.text(max_nb_chars=12),
                description=self.fake.text(),
                trailer=self.fake.url(),
                type=self.fake.random_element(elements=('IMAX', '2D', '3D')),
                url_seo=self.fake.url(),
                title_seo=self.fake.text(max_nb_chars=20),
                keywords_seo=self.fake.text(max_nb_chars=20),
                description_seo=self.fake.text(),
            )
            self.movies.append(movie)
            self.stdout.write(self.style.SUCCESS(f'Movie "{movie.name}" created.'))

    def _create_cinemas(self):
        self.cinemas = []
        for _ in range(3):
            cinema = Cinema.objects.create(
                name=self.fake.company()[:10],
                description=self.fake.catch_phrase()[:50],
                city=self.fake.city()[:12],
                url_seo=self.fake.url(),
                title_seo=self.fake.text(max_nb_chars=20),
                keywords_seo=self.fake.text(max_nb_chars=20),
                description_seo=self.fake.text(),
            )
            self.cinemas.append(cinema)
            self.stdout.write(self.style.SUCCESS(f'Cinema "{cinema.name}" created.'))

    def _create_halls(self):
        self.halls = []
        for cinema in self.cinemas:
            for _ in range(2):  # Створюємо по два зали на кожен кінотеатр
                hall = Hall.objects.create(
                    name=self.fake.text(max_nb_chars=20),
                    description=self.fake.text(),
                    schema_json=self.fake.json(),
                    cinema_hall=cinema,
                    url_seo=self.fake.url(),
                    title_seo=self.fake.text(max_nb_chars=20),
                    keywords_seo=self.fake.text(max_nb_chars=20),
                    description_seo=self.fake.text(),
                )
                self.halls.append(hall)
                self.stdout.write(self.style.SUCCESS(f'Hall "{hall.name}" created in cinema "{cinema.name}".'))

    def _create_showtimes(self):
        if not self.movies or not self.halls:
            self.stdout.write(self.style.WARNING("Not enough data to create showtimes."))
            return

        for _ in range(100):
            movie = random.choice(self.movies)
            hall = random.choice(self.halls)

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
            self.stdout.write(self.style.SUCCESS(f'Showtime created for movie "{movie.name}" in hall "{hall.name}" at {show_time}, Price: {price}.'))

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
            Page.objects.create(
                name=self.fake.text(max_nb_chars=12),
                description=self.fake.text(),
                created_at=self.fake.date_time_this_year().isoformat(),
                status=self.fake.boolean(),
                url_seo=self.fake.url(),
                title_seo=self.fake.text(max_nb_chars=20),
                keywords_seo=self.fake.text(max_nb_chars=20),
                description_seo=self.fake.text(),
            )

