from django.db import models

# Create your models here.

class Book(models.Model):
    book_title = models.CharField(max_length=200)
    book_author = models.CharField(max_length=100)
    book_published = models.DateField("data published", default='')
    book_pages = models.PositiveSmallIntegerField()
    book_type = models.CharField(max_length=100)
    book_picturename = models.CharField(max_length=200, default='')

    # def __str__(self):
    #     return self.book_title

