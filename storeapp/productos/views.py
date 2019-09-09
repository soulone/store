from django.template import loader
from django.shortcuts import render
from .models import Producto
from django.utils import timezone
from django.http import HttpResponse
from django.http import Http404

def index(request):
    productos = Producto.objects.all()
    return render(request, 'productos/index.html',{'productos':productos})

