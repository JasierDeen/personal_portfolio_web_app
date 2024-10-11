from django.shortcuts import render
from .models import Blog
def all_blog(request):
    blogs = Blog.objects.order_by("-created_at")[:5]
    return render(request, 'blog/all_blogs.html', {'blogs': blogs})