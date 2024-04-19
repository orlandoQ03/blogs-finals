from django.shortcuts import render, HttpResponse, redirect
from .models import BlogPost

# Create your views here.

def blog_index(request):
    posts = BlogPost.objects.all()
    return render(request, "blog_index.html", {"posts": posts})

def blog_create(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        post = BlogPost(title=title, content=content)

        # save if text is not blank.
        if (title != "" and content != ""):
            post.save()
            return redirect("blog_index")

    return render(request, "blog_create.html")

def home(request):
    return render(request, "home.html")

def blogpost(request):
    return render(request, "blogpost.html")
