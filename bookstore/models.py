from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100,unique=True)

    def __str__(self) :
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    isbn = models.CharField(max_length=13, unique=True)
    genre = models.CharField(max_length=50)
    publication_year = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    is_restored = models.BooleanField(default=False)

    def __str__(self) :
        return self.title
