from django.db import models


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
