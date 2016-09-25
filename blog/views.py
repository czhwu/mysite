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

# class ArticleView(DetailView):
#     model = 'Article'