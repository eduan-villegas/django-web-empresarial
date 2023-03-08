from django.shortcuts import render,get_object_or_404
from .models import Post,Category

# Create your views here.

def Blog(request):
    posts=Post.objects.all()
    contex={"posts":posts}
    return render(request,"blog/blog.html",contex)

def category(request,category_id):
    category=get_object_or_404(Category,id=category_id)
    posts=Post.objects.filter(categories=category)
    context={"category":category,"posts":posts}
    return render(request,'blog/category.html',context)