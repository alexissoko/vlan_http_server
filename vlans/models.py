from django.db import models
from django.contrib.auth.models import User
# import PhoneNumberField

# Create your models here.
class Vlan(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    location = models.CharField(max_length=100, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__ (self):
        return "Vlan: " + self.name
