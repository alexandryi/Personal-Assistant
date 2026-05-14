from django.db import models
from django.contrib.auth.models import User
import re


class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=100)

    email = models.EmailField()

    phone = models.CharField(max_length=20)

    address = models.CharField(max_length=255, blank=True)

    birthday = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name


class Phone(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name="phones")
    number = models.CharField(max_length=10)

    def clean(self):
        if not re.match(r'^\d{10}$', self.number):
            raise ValueError("Phone must be 10 digits")

    def __str__(self):
        return self.number