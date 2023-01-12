from django.urls import path
from categories.views import create_category, list_categories

urlpatterns = [
    path('create-category/', create_category),
    path('list-categories/', list_categories),

]