import random
from django.core.management.base import BaseCommand
from django.utils import timezone
from faker import Faker
from src.movies.models import Movie
from src.cinemas.models import Hall
from src.showtimes.models import ShowTime


class Command(BaseCommand):
    help = 'Generates showtimes for existing movies and halls'

    def handle(self, *args, **kwargs):
        self.fake = Faker()

        self._create_showtimes()

    def _create_showtimes(self):
        movies = Movie.objects.all()  # Отримуємо всі існуючі фільми
        halls = Hall.objects.all()  # Отримуємо всі існуючі зали

        if not movies.exists() or not halls.exists():
            self.stdout.write(self.style.WARNING("Not enough data to create showtimes."))
            return

        for movie in movies:  # Для кожного фільму
            for _ in range(5):  # Створюємо 5 сеансів (можна змінити кількість)
                hall = random.choice(halls)  # Випадково вибираємо зал

                show_time = timezone.make_aware(
                    self.fake.date_time_between(start_date='now', end_date='+30d'),
                    timezone.get_current_timezone()
                )

                price = random.randint(60, 150)  # Випадкова ціна на квитки

                ShowTime.objects.create(
                    hall_id=hall,  # Використовуємо правильне поле
                    movie_id=movie,  # Використовуємо правильне поле
                    show_time=show_time,
                    price=price,
                    movie_type=random.choice(['IMAX', '2D', '3D'])  # Випадковий тип фільму
                )

                self.stdout.write(
                    self.style.SUCCESS(f"Showtime created for movie '{movie.name}': {show_time}, Price: {price}"))
