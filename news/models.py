from django.db import models

class Article(models.Model):
    author = models.CharField(max_length=150)
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=200)
    text = models.TextField()
    city = models.CharField(max_length=120)
    published = models.DateField()
    active = models.BooleanField(default=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title 
