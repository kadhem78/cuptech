from django.shortcuts import render , redirect
from django.urls import reverse
from .models import Post
from .forms import PostForm
# Create your views here.

def home(request):
    posts = Post.objects.filter(pablished = True)
    context = {
    'posts' : posts
    }
    return render(request , 'index.html' , context)


def all_posts(request):
    posts = Post.objects.all()
    context = {
    'posts' : posts
    }
    return render(request , '' , context)

def post_details(request , slug):
    post = Post.objects.get(slug=slug)
    context = {
    'post':post
    }
    return render(request , 'single.html' , context)


def manage(request):
    my_posts = Post.objects.filter(author = request.user  )
    context = {
    'my_posts' : my_posts
    }
    return render(request , 'manage/manage.html' , context)

def create_post(request):
    if request.method == 'POST' :
        form = PostForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit = False)
            new_form.author = request.user
            new_form.save()
            return redirect(reverse('manage'))
    else:
        form = PostForm()
    context = {
    'form' : form
    }
    return render(request , 'manage/createpost.html' , context)

def update_post(request , slug):
    post = Post.objects.get(slug = slug)
    if request.method == 'POST':
        form = PostForm(request.POST , request.FILES , instance=post)
        if form.is_valid():
            print('valid')
            new_form = form.save(commit = False)
            new_form.author = request.user
            new_form.save()
            return redirect(reverse('manage'))
    else:
        form = PostForm(instance=post)
    context = {
    'form' : form
    }
    return render(request , 'manage/updatepost.html' , context)



def delete_post(request , slug):
    Post.objects.get(slug = slug).delete()
    return redirect(reverse('manage'))


def categorie_posts(request , slug):
    pass
