from django.db import models

# Create your models here.

class Review(models.Model):
    GENRE_CHOICES = [
        ('Action', '액션'),
        ('Comedy', '코미디'),
        ('Drama', '드라마'),
        ('Sci-Fi', '공상과학'),
        ('Romance', '로맨스'),
        ('Thriller', '스릴러'),
        ('Horror', '공포'),
        ('Animation', '애니메이션'),
        ('Crime', '범죄'),
        ('Fantasy', '판타지'),
        ('Family', '가족'),
        ('Adventure', '모험'),
        ('War', '전쟁'),
        ('Music', '음악'),
        ('Documentary', '다큐멘터리'),
        ('Etc', '기타'),
    ]

    title = models.CharField(max_length=100)
    release_year = models.IntegerField()
    genre = models.CharField(max_length=50, choices=GENRE_CHOICES)
    rating = models.IntegerField()
    director = models.CharField(max_length=100)
    main_actor = models.CharField(max_length=100)
    running_time = models.IntegerField()
    review_content = models.TextField()
    poster = models.ImageField(upload_to='images/', blank=True, null=True)