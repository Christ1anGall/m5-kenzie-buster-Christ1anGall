from django.db import models
from django.utils import timezone


class ratingChoices(models.TextChoices):
    G = "G"
    PG = "PG"
    PG13 = "PG-13"
    R = "R"
    NC17 = "NC-17"


class Movie(models.Model):
    title = models.CharField(max_length=127, null=False)
    duration = models.CharField(max_length=10, null=True, default=None)
    rating = models.CharField(
        max_length=20,
        default=ratingChoices.G,
        choices=ratingChoices.choices,
    )
    synopsis = models.TextField(null=True, default=None)
    added_by = models.EmailField()

    buyed_by = models.ManyToManyField(
        "users.User", through="movies.MovieOrder", related_name="buyedMovies"
    )


class MovieOrder(models.Model):
    buyed_at = models.DateTimeField(editable=False, auto_now_add=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, null=False)

    movie = models.ForeignKey(
        "movies.Movie", on_delete=models.CASCADE, related_name="OrderMovie"
    )

    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="OrderUser"
    )
