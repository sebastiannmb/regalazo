from django.urls import path

from sells.views import list_sells, create_sell

urlpatterns = [
    path('create-sell/', create_sell),
    path('list-sells/', list_sells),
]