from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from sells.models import Sell

def list_sells(request):
    sells = Sell.objects.all()
    context = {
        'sells': sells,
    }
    return render(request, 'sells/list_sells.html', context=context)

def create_sell(request):
    Sell.objects.create(client='Franco', product='Mochila Up', payment_method='Card')
    return HttpResponse('Sell created')

