from django.shortcuts import render
from django.http import HttpResponse

from categories.models import Category

# Create your views here.

def create_category(request, name):
    Category.objects.create(name=name)
    return HttpResponse('Categoría creada')

def list_categories(request):
    all_categories = Category.objects.all()
    context = {
        'categories':all_categories
    }
    return render(request, 'categories/list_categories.html', context=context)