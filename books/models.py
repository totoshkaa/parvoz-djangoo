from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length = 255)
    description = models.TextField()
    isbn = models.CharField(max_length=13)
    cover_pic = models.ImageField(upload_to="book_pics")

    def __str__(self):
        return self.title
