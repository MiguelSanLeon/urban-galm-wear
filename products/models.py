from django.db import models
from profiles.models import UserProfile


class Category (models.Model):
    """ This model holds the category data """

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=128)
    friendly_name = models.CharField(max_length=128, null=True, blank=True)
    description = models.CharField(max_length=128, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


def custom_image_upload_to(instance, filename):
    return filename

class Product(models.Model):
    """ This model holds the product data """
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    description = models.TextField()
    has_sizes = models.BooleanField(default=True, null=True, blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    sku = models.CharField(max_length=128, null=True, blank=True)
    carbon_footprint = models.DecimalField(max_digits=6, decimal_places=2,
                                           null=True, blank=True)
    rating = models.DecimalField(max_digits=6, decimal_places=2,
                                 null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(upload_to=custom_image_upload_to, null=True, blank=True)
    user_wishlist = models.ManyToManyField(UserProfile, related_name='wishlist_products', blank=True)

    def __str__(self):
        return self.name