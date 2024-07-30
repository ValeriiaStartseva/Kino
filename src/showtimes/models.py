from django.db import models
from src.cinemas.models import Hall
from src.movies.models import Movie


class ShowTime(models.Model):
    hall_id = models.ForeignKey(Hall, on_delete=models.CASCADE)
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    show_time = models.DateTimeField(db_index=True)

    def __str__(self):
        return str(self.show_time)


class Ticket(models.Model):
    show_time_id = models.ForeignKey(ShowTime, on_delete=models.CASCADE)
    price = models.IntegerField()
    row = models.IntegerField()
    seat = models.IntegerField()

    def __str__(self):
        return str(self.id)
