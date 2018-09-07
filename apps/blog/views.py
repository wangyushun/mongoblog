from django.shortcuts import render, redirect, reverse
from django.views.generic import ListView, DetailView
from django.views import View

from .models import Blog
from .forms import BlogForm

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


def blog_add(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=True)
            blog.save()
            return redirect(reverse('blog_list'))
    else:
        form = BlogForm()

    content = {}
    content['form_title'] = '添加博客'
    content['submit_text'] = '提交'
    content['action_url'] = reverse('blog_add')
    content['form'] = form
    return render(request, 'form.html', content)


class AddBlogView(View):
    pass


