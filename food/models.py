from django.db import models
from django.utils.html import mark_safe

class Breakfast(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=50, null=True, blank=True)
    price = models.FloatField()
    del_price = models.IntegerField(null=True, blank=True)
    ball = models.IntegerField()
    review = models.IntegerField()

    def __str__(self) -> str:
        return self.name
    def image_tag(self):
        return mark_safe('<img src="/mediafile/%s" width="100" height="100" />' % (self.image))

    image_tag.short_description = 'Image'

class Lunch(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=50, null=True, blank=True)
    price = models.FloatField()
    del_price = models.IntegerField(null=True, blank=True)
    ball = models.IntegerField()
    review = models.IntegerField()

    def __str__(self) -> str:
        return self.name
    def image_tag(self):
        return mark_safe('<img src="/mediafile/%s" width="100" height="100" />' % (self.image))

    image_tag.short_description = 'Image'

class Dinner(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=50, null=True, blank=True)
    price = models.FloatField()
    del_price = models.IntegerField(null=True, blank=True)
    ball = models.IntegerField()
    review = models.IntegerField()

    def __str__(self) -> str:
        return self.name
    def image_tag(self):
        return mark_safe('<img src="/mediafile/%s" width="100" height="100" />' % (self.image))

    image_tag.short_description = 'Image'

class Desert(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=50, null=True, blank=True)
    price = models.FloatField()
    del_price = models.IntegerField(null=True, blank=True)
    ball = models.IntegerField()
    review = models.IntegerField()

    def __str__(self) -> str:
        return self.name
    def image_tag(self):
        return mark_safe('<img src="/mediafile/%s" width="100" height="100" />' % (self.image))

    image_tag.short_description = 'Image'