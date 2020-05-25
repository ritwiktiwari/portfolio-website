from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Blog
# Create your views here.


def index(request):
    blogs = Blog.objects.order_by('-pub_date').filter(is_published=True)
    paginator = Paginator(blogs, 9)
    page = request.GET.get('page')
    paged_blogs = paginator.get_page(page)
    context = {
        'blogs': paged_blogs,
    }
    return render(request, 'blog/blog.html', context)


def post(request, blog_id):
    blog_post = get_object_or_404(Blog, pk=blog_id)
    context = {
        'post': blog_post,
    }
    return render(request, 'blog/post.html', context)
