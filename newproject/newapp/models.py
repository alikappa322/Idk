from django.db import models

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    year = models.IntegerField()


class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    years = models.IntegerField()
    publish_date = models.DateField()
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE)
    count = models.IntegerField(default=0)

