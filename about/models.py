from django.db import models
from cloudinary.models import CloudinaryField


# Class based models.
class About(models.Model):
    title = models.CharField(max_length=100, default='About FightVault')
    profile_image = CloudinaryField('image', default='placeholder')
    mission = models.TextField(blank=True)
    values = models.TextField(blank=True)
    goals = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
