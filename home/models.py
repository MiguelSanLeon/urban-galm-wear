from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=80, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    message = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.name
