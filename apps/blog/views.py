from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Blog

# Create your views here.


class BlogListView(ListView):
    '''
    博客类视图
    '''
    model = Blog
    template_name   = 'blogs.html'
    context_object_name  = 'blogs'
    paginate_by = 10


class BlogDetailView(DetailView):
    '''
    博客详情
    '''
    model = Blog
    template_name = "blog_detail.html"
    context_object_name = "blog"
    pk_url_kwarg = 'blog_id'


