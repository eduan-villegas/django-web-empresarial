from django.shortcuts import render
from .models import Service
# Create your views here.

def Services(request):
    services=Service.objects.all()
    contex={"services":services}
    return render(request,"services/services.html",contex)