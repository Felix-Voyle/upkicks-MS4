from django.db import models


class Brand(models.Model):
    """Brand Model"""
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=False, blank=False)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    """Product Model"""
    brand = models.ForeignKey('Brand', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    release_date = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
