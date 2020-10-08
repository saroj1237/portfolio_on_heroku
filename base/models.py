from django.db import models
from portfolio.utils import unique_slug_generator, random_string_generator
from django.db.models.signals import pre_save

class Post(models.Model):
    headline = models.CharField(max_length=200)
    sub_headline = models.CharField(max_length= 200,null = True, blank = True)
    thumbnail = models.ImageField(null = True, blank= True,upload_to='media',default = '/images/saroj.jpg')
    body = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.headline

def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug= unique_slug_generator(instance)

pre_save.connect(slug_generator,sender=Post)