# movies/management/commands/load_movies.py

import json
from django.core.management.base import BaseCommand
from movies.models import Movie, Genre, MPAA

class Command(BaseCommand):
    help = 'Load movies from JSON file'

    def handle(self, *args, **kwargs):
        with open('movies.json') as f:
            movies = json.load(f)

            for item in movies:
                mpaa_data = item['mpaaRating']
                mpaa, _ = MPAA.objects.get_or_create(type=mpaa_data['type'], label=mpaa_data['label'])

                movie = Movie.objects.create(
                    name=item['name'],
                    description=item['description'],
                    img_path=item['imgPath'],
                    duration=item['duration'],
                    language=item['language'],
                    mpaa_rating=mpaa,
                    user_rating=item['userRating']
                )

                for genre_name in item['genre']:
                    genre, _ = Genre.objects.get_or_create(name=genre_name)
                    movie.genre.add(genre)

                movie.save()
