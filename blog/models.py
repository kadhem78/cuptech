from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from .utils import unique_slug_generator
# Create your models here.



class Categorie(models.Model):
    name = models.CharField(max_length = 20)
    slug = models.SlugField(max_length= 25 , null = True , blank = True , unique = True )

    def __str__(self):
        return self.name
    @property
    def title(self):
        return self.name

    def save(self , *args , **kwargs):
        self.slug = unique_slug_generator(self)
        super(Categorie , self).save(*args , **kwargs)

def imageupload(instance, filename):
    image_name , extention = filename.split('.')
    return 'posts/{0}/images/{1}.{2}'.format(instance.title, instance.title , extention)


class Post(models.Model):
    author = models.ForeignKey(User , on_delete = models.CASCADE)
    categorie = models.ForeignKey(Categorie , on_delete = models.CASCADE)
    header_img = models.ImageField(upload_to = imageupload)
    title = models.CharField(max_length = 200)
    slug = models.SlugField(max_length= 250 , null = True , blank = True , unique = True)
    content = RichTextUploadingField()
    created = models.DateTimeField(auto_now = True)
    updated = models.DateTimeField(auto_now_add = True)
    pablished = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def save(self , *args , **kwargs):
        self.slug = unique_slug_generator(self)
        super(Post , self).save(*args , **kwargs)
