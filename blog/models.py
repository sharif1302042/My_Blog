from django.contrib.auth.models import User
from django.db import models


class AuthorManager(models.Manager):
    pass

class Author(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    full_name = models.CharField(max_length=50, null=True, blank=True)
    total_post = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = AuthorManager()

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Author List'

    def __str__(self):
        if self.full_name:
            return self.full_name
        return self.username

class PostManager(models.Manager):
    pass

class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='author')
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = PostManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'All Post List'

