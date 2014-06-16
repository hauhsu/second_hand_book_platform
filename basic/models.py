from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=128)
    price = models.FloatField()
    owner = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='book_images', blank=True)
    shelf_date = models.DateField(auto_now_add=True)


    def _unicode_(self):
        return self.name
