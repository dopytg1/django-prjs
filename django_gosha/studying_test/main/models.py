from django.db import models

# Create your models here.


class Task(models.Model):
    title = models.CharField("название", max_length=50)
    task = models.TextField("описание")

    def __str__(self):
        return self.title
        