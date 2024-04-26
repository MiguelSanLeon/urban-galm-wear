from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField

class UserProfile(models.Model):
    """
    User profiel that helps keeping user
    delivery information and order history
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(max_length=20, null=False, blank=True)
    default_street_address1 = models.CharField(max_length=80, null=False, blank=True)
    default_street_address2 = models.CharField(max_length=80, null=True, blank=True)
    default_town_or_city = models.CharField(max_length=50, null=False, blank=True)
    default_county = models.CharField(max_length=80, null=True, blank=True)
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_country = CountryField(blank_label='Country', null=False, blank=True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
    #Existing users: just save the profile
    instance.userprofile.save()

    # Check if the user is a superuser
    if instance.is_superuser:
        # Assign specific default values for superusers
        instance.userprofile.default_phone_number = "0000000000"
        instance.userprofile.default_street_address1 = "main street 1"
        instance.userprofile.default_street_address2 = "main main"
        instance.userprofile.default_town_or_city = "Gotham"
        instance.userprofile.default_county = "Pearl"
        instance.userprofile.default_postcode = "A63T5T6"
        instance.userprofile.default_country = "US"

        # Save the profile again to apply the changes
        instance.userprofile.save()
        