from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from sellers.models import Sellers

# Create your views here.

def create_seller(request, name):
    Sellers.objects.create(name=name)
    return HttpResponse('Vendedor creado')

def list_sellers(request):
    all_sellers = Sellers.objects.all()
    context = {
        'sellers':all_sellers
    }
    return render(request, 'sellers/list_sellers.html', context=context)