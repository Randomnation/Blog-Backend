from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(max_length=65)
    description = models.TextField(max_length=155)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Categories'


class Post(models.Model):
    title = models.CharField(max_length=200)
    categories = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    text = models.TextField(max_length=500)
    owner = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE, null=True)
    created_date = models.DateTimeField(auto_now=True)
    modified_date = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.title
