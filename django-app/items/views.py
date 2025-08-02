#from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from .models import Item

def index(request):
    if request.method == "POST":
        name = request.POST.get("item")
        if name:
            Item.objects.create(name=name)
            return redirect('/')
    items = Item.objects.all()
    return render(request, "index.html", {"items": items})

