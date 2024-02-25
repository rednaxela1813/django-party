from os import name
from tabnanny import verbose
from django.contrib.auth.models import AbstractUser
import uuid
from django.db import models
from django.conf import settings


class CustomUser(AbstractUser):
    pass


class Party(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    party_date = models.DateField()
    party_time = models.TimeField()
    venue = models.CharField(max_length=100)
    invitation = models.TextField()
    organizer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        ordering = ['party_date']
        verbose_name_plural = 'parties'


    def __str__(self):
        return f"{self.venue}, {self.party_date}"
    

class Gift(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    gift = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    link = models.URLField(max_length=200, blank=True, null=True)
    party = models.ForeignKey(Party, on_delete=models.CASCADE)


    def __str__(self):
        return self.gift    
    


class Guest(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, blank=True, null=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=100)
    attending = models.BooleanField(default=False)
    party = models.ForeignKey(Party, on_delete=models.CASCADE)
    # gift = models.ForeignKey(Gift, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        unique_together = ['first_name', 'last_name', 'party']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
