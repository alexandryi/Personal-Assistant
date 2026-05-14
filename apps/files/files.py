from django.db import models
from django.contrib.auth.models import User


class UserFile(models.Model):
    CATEGORY_CHOICES = [
        ('image', 'Images'),
        ('doc', 'Documents'),
        ('video', 'Videos'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads/')
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)