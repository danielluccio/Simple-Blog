from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Posts
from .forms import PostForm
from django.urls import reverse


def post_list(request):
    template_name = 'post_list.html'
    posts = Posts.objects.all()
    context = {
        'posts': posts
    }
    return render(request, template_name, context)

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            return HttpResponseRedirect(reverse('post_list'))
        
    posts = PostForm()
    return render(request, 'post_create', {'form': form})

def post_details(request, id):
    template_name = 'post_details.html'
    post = Posts.objects.get(id=id)
    context = {
        'post': post
    }

    return render(request, template_name, context)
