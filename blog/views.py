from django.shortcuts import render
from .models import *
from django.views.generic import ListView, DetailView


# # Create your views here.
# class IndexView(ListView):
#     context_object_name = 'post_list'
#     model = 'Post'
def index(request):
    post_list = Post.objects.order_by('-pub_date')
    context = {'post_list': post_list, }
    return render(request, 'blog/index.html', context)


def detail(request, post_id):
    post = Post.objects.get(pk=post_id)
    context = {'post': post}

    return render(request, 'blog/detail.html', context)


def marqueen(request):
    post_list = Post.objects.order_by('-pub_date')
    context = {'post_list': post_list}
    return render(request, 'blog/marqueen.html', context)
