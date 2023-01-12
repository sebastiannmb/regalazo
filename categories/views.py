from django.shortcuts import render
from django.http import HttpResponse

from categories.models import Category
from categories.forms import CategoryForm

# Create your views here.

def create_category(request):
    if request.method == 'GET':
        context = {
            'form': CategoryForm()
        }
        return render(request, 'categories/create_category.html', context={})

    elif request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            #Creamos la categoria
            Category.objects.create(
                name=form.cleaned_data['name'],
            )
            context = {
                'message': 'Categoría creada exitosamente'
            }
            return render(request, 'categories/create_category.html', context=context)
        
        else: 
            context = {
                'form_errors': form.errors,
            }
            
        return render(request, 'categories/create_category.html', context={})

def list_categories(request):
    all_categories = Category.objects.all()
    context = {
        'categories':all_categories
    }
    return render(request, 'categories/list_categories.html', context=context)

