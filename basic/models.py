from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    name = models.CharField(max_length=128)
    price = models.FloatField()
    owner = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='book_images', blank=True)
    shelf_date = models.DateField(auto_now_add=True)


    def _unicode_(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __unicode__(self):
        return self.user.username
