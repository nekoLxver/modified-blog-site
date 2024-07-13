from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

# Create your models here.


class Post(models.Model):

    cases = [
        ('PB', "Published"),
        ("DR", "Draft"),
    ]

    slug = models.CharField(max_length=250, unique_for_date='created')
    title = models.CharField(max_length=250)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=2, choices=cases, default='DR')
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']
        indexes = [
            models.Index(fields=['-created'])
        ]

    def __str__(self):
        return f"{self.title[0:30]}... - {self.author}"

    def get_absolute_url(self):
        return reverse("blog:details", args=[
            self.created.year,
            self.created.month,
            self.created.day,
            self.slug,
        ])
