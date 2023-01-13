from django.urls import path
from categories.views import create_category, list_categories, searchCategory, search
from categories import views


urlpatterns = [
    path('create-category/', create_category),
    path('list-categories/', list_categories),
    path('searchCategory/', views.searchCategory, name='BusquedaCategoria'),
    path('search/', views.search),

]