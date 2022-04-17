from django.db import models
from django.contrib.auth.models import User
from blog.utils import unique_slug_generator
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.



class Subject(models.Model):
    name = models.CharField(max_length = 50)
    slug = models.SlugField(null = True , blank = True , unique = True)

    @property
    def title(self):
        return self.name

    def __str__(self):
        return self.title

    def save(self , *args , **kwargs ):
        self.slug = unique_slug_generator(self)
        super(Subject , self).save(*args , **kwargs)

class Course(models.Model):
    subject = models.ForeignKey(Subject , on_delete=models.CASCADE)
    instructor = models.ForeignKey(User , on_delete=models.CASCADE)
    title = models.CharField(max_length = 50)
    slug  = models.SlugField(null = True , blank = True , unique = True)
    course_img = models.ImageField(upload_to='')
    description = RichTextUploadingField()
    created = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default = False)

    def __str__(self):
        return self.title

    def save(self , *args , **kwargs ):
        self.slug = unique_slug_generator(self)
        super(Course , self).save(*args , **kwargs)


class Enrolments(models.Model):
    course = models.OneToOneField(Course , on_delete=models.CASCADE)
    student = models.ForeignKey(User , on_delete=models.CASCADE)

    def __str__(self):
        return self.student.username





class Module(models.Model):
    course = models.ForeignKey(Course , on_delete=models.CASCADE)
    title = models.CharField(max_length = 50)
    content = RichTextUploadingField()

    def __str__(self):
        return self.title
