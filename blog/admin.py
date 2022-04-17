from django.contrib import admin
from .models import Post , Categorie
# Register your models here.

@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    pass

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    list_filter = ('categorie' , 'author' , 'created' , 'pablished')
