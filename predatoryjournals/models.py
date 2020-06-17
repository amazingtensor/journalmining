# Django models stored in DB
# Define object properties and methods (class is blueprint for objects)
from django.conf import settings
from django.db import models
from django.utils import timezone


class Listing(models.Model):
    # LISTING_ATTRIBUTES = [
    #    ('GEN', 'Generally predatory'),
    #    ('HIJ', 'Hijacked'),
    # ]

    # contributor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    journaltitle = models.CharField(max_length=200)
    url = models.URLField(max_length=200, default="?")
    added_date = models.DateTimeField(default=timezone.now)
    # modified_date = models.DateTimeField(blank=True, null=True)
    # attribute = models.CharField(max_length=3, choices=LISTING_ATTRIBUTES)

    def publish(self):
        self.added_date = timezone.now()
        self.save()

    # returns string representation of the object
    def __str__(self):
        return self.journaltitle
