from audioop import reverse
from tabnanny import verbose
from django.db import models
from django.urls import reverse

# Create your models here.


class Dress(models.Model):
    title = models.CharField(max_length=100, null=True)
    slug = models.SlugField(max_length=225, unique=True, db_index=True)
    photo = models.ImageField(upload_to='photos/%y/%m/%d', null=True)
    price = models.IntegerField(default=0)
    text = models.TextField(null=True)
    category_id = models.ForeignKey('Categories', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Одежда'
        verbose_name_plural = 'Одежда'
        ordering = ['title']


class Categories(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=225, unique=True, db_index=True)
    text = models.TextField(null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={"cat_slug": self.slug})

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'
        ordering = ['id']