from django.contrib.auth.decorators import login_required
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

@login_required
def list_categories(request):
    if 'search' in request.GET:
        search = request.GET['search']
        categories = Category.objects.filter(name__contains=search)
    else:
        categories = Category.objects.all()
    context = {
        'categories':categories
    }
    return render(request, 'categories/list_categories.html', context=context)

def searchCategory(request):
    return render(request, 'categories/search_category.html')

def search(request):
    if request.GET['categories']:

        categories = request.GET['categories']
    respuesta = f'Está buscando la categoría: {request.GET["categories"]}'
    return HttpResponse(respuesta)


