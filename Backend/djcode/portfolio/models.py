from django.db import models


class Portfolio(models.Model):
    title = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    image_url = models.URLField()
    text = models.TextField()
    slug = models.SlugField(unique=True)
    site_url = models.URLField()
    order = models.PositiveSmallIntegerField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('order',)
