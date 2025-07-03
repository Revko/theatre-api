from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = None

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


class Actor(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)

class Genre(models.Model):
    name = models.CharField(max_length=64)

class Play(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    actors = models.ManyToManyField(Actor)
    genres = models.ManyToManyField(Genre)

class TheatreHall(models.Model):
    name = models.CharField(max_length=64)
    rows = models.PositiveIntegerField()
    seats_in_row = models.PositiveIntegerField()

class Performance(models.Model):
    play = models.ForeignKey(Play, on_delete=models.CASCADE)
    theatre_hall = models.ForeignKey(TheatreHall, on_delete=models.CASCADE)
    show_time = models.DateTimeField()

class Reservation(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Ticket(models.Model):
    performance = models.ForeignKey(Performance, on_delete=models.CASCADE)
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    row = models.PositiveIntegerField()
    seat = models.PositiveIntegerField()

    class Meta:
        unique_together = ("performance", "row", "seat")