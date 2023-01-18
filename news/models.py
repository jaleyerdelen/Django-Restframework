from django.db import models

class Journalist(models.Model):
    name = models.CharField(max_length=120)
    surname = models.CharField(max_length=120)
    biography = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} {self.surname}"

class Article(models.Model):
    author = models.ForeignKey(Journalist, on_delete=models.CASCADE, related_name="articles")
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
