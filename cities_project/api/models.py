from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}'

class City(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'

class PhotoLink(models.Model):
    product = models.ForeignKey(Product, related_name='photo_links', on_delete=models.CASCADE)
    photo_link = models.CharField(max_length=2000)
    city = models.ForeignKey(City, related_name='photo_links', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.product, self.photo_link}'
