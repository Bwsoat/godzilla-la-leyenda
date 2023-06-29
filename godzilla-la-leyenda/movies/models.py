from django.db import models


class Movie(models.Model):
    title_movie = models.CharField(max_length=100)
    poster = models.ImageField('Imagen', upload_to='posters/', max_length=255)
    description_text = models.CharField(max_length=300)
    duration = models.CharField(max_length=50)
    download = models.CharField(max_length=150)


    def  __str__(self):
        return self.title_movie