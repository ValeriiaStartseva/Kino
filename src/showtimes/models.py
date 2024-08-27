from django.db import models
from src.cinemas.models import Hall
from src.movies.models import Movie
from src.users.models import User


class ShowTime(models.Model):
    TYPE_CHOICES = (
        ('IMAX', 'IMAX'),
        ('2D', '2D'),
        ('3D', '3D'),
    )

    hall_id = models.ForeignKey(Hall, on_delete=models.CASCADE)
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    show_time = models.DateTimeField(db_index=True)
    movie_type = models.CharField(max_length=4, choices=TYPE_CHOICES, default='3D')
    price = models.IntegerField(default=0)  # Ціна квитка

    def __str__(self):
        return str(self.show_time)


class Ticket(models.Model):
    show_time_id = models.ForeignKey(ShowTime, on_delete=models.CASCADE)
    row = models.IntegerField()
    seat = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # Зв'язок з користувачем

    def __str__(self):
        return f"Ticket {self.id} - ShowTime {self.show_time_id} - Row {self.row} - Seat {self.seat}"

