from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class MPAA(models.Model):
    type = models.CharField(max_length=10)
    label = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.type} - {self.label}"

class Movie(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    img_path = models.CharField(max_length=255)
    duration = models.IntegerField()
    genre = models.ManyToManyField(Genre)
    language = models.CharField(max_length=100)
    mpaa_rating = models.ForeignKey(MPAA, on_delete=models.CASCADE)
    user_rating = models.CharField(max_length=10)

    def __str__(self):
        return self.name

