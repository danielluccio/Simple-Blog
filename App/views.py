from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Posts
from .forms import PostForm
from django.urls import reverse
from django.shortcuts import get_object_or_404


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
            form.save()
            return HttpResponseRedirect(reverse('post_list'))
        
    form = PostForm()
    return render(request, 'post_create.html', {'form': form})

def post_details(request, id):
    template_name = 'post_details.html'
    post = Posts.objects.get(id=id)
    context = {
        'post': post
    }

    return render(request, template_name, context)


def post_update(request, id):
    template_name = 'post_update.html'
    post = get_object_or_404(Posts, id=id)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)
    if form.is_valid():
        form.save()

        return HttpResponseRedirect(reverse(post_list))
    
    return render(request, template_name, {'form': form})

def post_delete(request, id):
    post = get_object_or_404(Posts, id=id)
    post.delete()
    return HttpResponseRedirect(reverse('post_list'))
