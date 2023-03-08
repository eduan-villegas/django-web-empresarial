from django.shortcuts import render

# Create your views here.


def Home(request):
    return render(request,"core/home.html")


def About(request):
    return render(request,"core/about.html")


def Store(request):
    return render(request,"core/store.html")


def Contact(request):
    return render(request,"core/contact.html")



