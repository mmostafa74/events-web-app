from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Event(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="event")
    title = models.CharField(max_length=250)
    description = models.TextField()
    date = models.DateField()
    slug = models.SlugField(max_length=250, unique_for_date="created")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("-date",)

    def __str__(self):
        return self.title
