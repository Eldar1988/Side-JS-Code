from django.db import models


class CallBack(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=30)
    text = models.TextField(null=True, blank=True)
    service = models.CharField(null=True, blank=True, max_length=255)
    complete = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
