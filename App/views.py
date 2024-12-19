from django.shortcuts import render
from .models import Posts


def post_list(request):
    template_name = 'post_list.html'
    posts = Posts.objects.all()
    context = {
        'posts': posts
    }
    return render(request, template_name, context)


