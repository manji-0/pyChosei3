from django.db import models
from django.utils import timezone
import hashlib

class Event(models.Model):
    id = models.IntegerField(primary_key=True)
    owner = models.ForeignKey('auth.User')
    title = models.CharField(max_length=50)
    description = models.TextField()
    createdDate = models.DateTimeField(default=timezone.now)
    eventDate = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        sourceText = str(self.title) + str(self.id)
        hashed = hashlib.sha224(sourceText.encode())
        return "/events/%i" % hashed.hexdigest()


class Plan(models.Model):
    id = models.IntegerField(primary_key=True)
    eventID = models.IntegerField()
    name = models.CharFileld(max_length=16)
    owner = models.ForeignKey('auth.User')
    createdDate = models.DateTimeField(default=timezone.now)
    data = models.TextField() # for JSON String

    def __str__(self):
        return self.name

