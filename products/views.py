from django.shortcuts import render
from products.models import Products
from django.http import HttpResponse

# Create your views here.

def create_product(request):
    new_product = Products.objects.create(name='Mochila Up', price=5417.99, category='Bolsos')
    print(new_product)
    return HttpResponse('Se creó el nuevo producto')

def list_products(request):
    all_products = Products.objects.all()
    context = {
        'products':all_products,
    }
    return render(request, 'products/list_products.html', context=context)