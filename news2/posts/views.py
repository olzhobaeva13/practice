from django.shortcuts import render
from django.views import View
from .models import Post

def posts_list_view(request):
    posts = Post.objects.all()
    return render(request, 'posts/post_list.html', context={'posts': posts})
    

class PostView(View):
    pass