from django.shortcuts import render, redirect, get_object_or_404
from .models import BlogPost
from django.contrib import messages

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
        if (title and content):
            post.save()
            return redirect("blog_index")
        else:
            messages.error(request, "Please fill in all fields.")
    return render(request, "blog_create.html")

def blog_delete(request, id):
    post = get_object_or_404(BlogPost, id=id)
    if request.method == 'POST':
        post.delete()
        return redirect('blog_index')
    return render(request, 'blog_delete.html', {'post': post})

def home(request):
    return render(request, "home.html")

def blogpost(request):
    return render(request, "blogpost.html")

# TODO
#     Implement CRUD: Create [done], Read [done], Update, Delete[done]
#     Add more styles to the blog
#     add commenting feature
#     fix the post view
#     ????
#     profit