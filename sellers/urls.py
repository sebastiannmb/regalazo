from django.urls import path

from sellers.views import create_seller, list_sellers

urlpatterns = [
    path('create-seller/', create_seller),
    path('list-sellers/', list_sellers),
]