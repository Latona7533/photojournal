from django.db import models
from django.contrib.auth.models import User

GENRES = [
    ('GM', 'Games'),
    ('MC', 'Music'),
]

class BlogManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(genre='GM')

class Blog(models.Model):
    genre = models.CharField(choices=GENRES, default='MC', max_length=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='static/imgs')
    title = models.CharField(max_length=15, blank=True, null=True)
    likes = models.ManyToManyField(User, related_name='post_like')
    description = models.TextField(max_length=100)
    creation = models.DateTimeField(auto_now=True)
    slug = models.SlugField(null=True, blank=True)
    objects = models.Manager()
    game = BlogManager()

    def number_of_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.description


class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    text = models.TextField(max_length=100)
    creation = models.DateTimeField(auto_now=True)















