from django.urls import path
from providers.views import ProvidersListView, ProviderCreateView, ProviderDeleteView, ProviderUpdateView

urlpatterns = [
    path('list-providers/', ProvidersListView.as_view(), name='list-providers'),
    path('create-providers/', ProviderCreateView.as_view(), name='create-providers'),
    path('update-provider/<int:pk>/', ProviderUpdateView.as_view(), name='update-provider'),
    path('delete-provider/<int:pk>/', ProviderDeleteView.as_view(), name='delete-provider'),
]
