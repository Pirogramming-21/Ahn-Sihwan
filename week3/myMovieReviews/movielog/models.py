from django.db import models

# Create your models here.

class Review(models.Model):
    title = models.CharField(max_length=100)
    release_year = models.IntegerField()
    genre = models.CharField(max_length=100)
    rating = models.IntegerField()
    director = models.CharField(max_length=100)
    main_actor = models.CharField(max_length=100)
    running_time = models.IntegerField()
    review_content = models.TextField()
    poster = models.ImageField(upload_to='images/', blank=True, null=True)