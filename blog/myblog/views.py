from django.shortcuts import render, HttpResponse
from .models import BlogPost

# Create your views here.
def home(request):
    return render(request, "home.html")

def blogpost(request):
    return render(request, "blogpost.html")

def blog_index(request):
    blog_posts = BlogPost.objects.all()
    return render(request, "blog_index.html", {"blog_posts": blog_posts})

def blog_create(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        BlogPost.objects.create(title=title, content=content)
        return HttpResponse("Blog post created")
    return render(request, "blog_create.html")