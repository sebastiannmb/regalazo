from django.urls import path
from providers.views import providers_update, ProvidersListView, ProviderCreateView, ProviderDeleteView

urlpatterns = [
    path('list-providers/', ProvidersListView.as_view(), name='list-providers'),
    path('create-providers/', ProviderCreateView.as_view(), name='create-providers'),
    path('update-provider/<int:pk>/', providers_update, name='update-provider'),
    path('delete-provider/<int:pk>/', ProviderDeleteView.as_view(), name='delete-provider'),
]
