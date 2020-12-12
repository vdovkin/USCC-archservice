from django.db import models
from django.core.exceptions import ValidationError

from datetime import datetime


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100, blank=True)
    profession = models.CharField(max_length=100, blank=True)
    message = models.TextField()
    contact_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name + self.message[:30]
