from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.shortcuts import render
from providers.models import Provider
from providers.forms import ProviderForm


def list_providers(request):
    providers = Provider.objects.filter(is_active = True)
    context = {
        'providers':providers,
    }
    return render(request, 'providers/list-providers.html', context=context)

def providers_create(request):
    if request.method == 'GET':
        context = {
            'form': ProviderForm()
        }
        return render(request, 'providers/create-providers.html', context=context)

    elif request.method == 'POST':
        form = ProviderForm(request.POST)
        if form.is_valid():
            Provider.objects.create(
                name=form.cleaned_data['name'],
                address=form.cleaned_data['address'],
                phone_number=form.cleaned_data['phone_number'],
                email=form.cleaned_data['email'],
                condition=form.cleaned_data['condition'],
            )
            context = {
                'message': 'Proveedor creado exitosamente'
            }        
        else: 
            context = {
                'form_errors': form.errors,
            }            
        return render(request, 'providers/create-providers.html', context=context)

def providers_update(request, pk):
    provider = Provider.objects.get(id=pk)

    if request.method == 'GET':
        context = {
            'form': ProviderForm(
                initial={
                    'name':provider.name,
                    'address':provider.address,
                    'phone_number':provider.phone_number,
                    'email':provider.email,
                    'condition':provider.condition,
                }
            )
        }
        return render(request, 'providers/update-provider.html', context=context)

    elif request.method == 'POST':
        form = ProviderForm(request.POST)
        if form.is_valid():
            provider.name = form.cleaned_data['name'],
            provider.address=form.cleaned_data['address'],
            provider.phone_number = form.cleaned_data['phone_number'],
            provider.email = form.cleaned_data['email'],
            provider.condition = form.cleaned_data['condition'],
            provider.save()
            context = {
                'message': 'Proveedor actualizado exitosamente'
            }        
        else: 
            context = {
                'form_errors': form.errors,
            }            
        return render(request, 'providers/update-providers.html', context=context)

class ProvidersListView(ListView):
    model = Provider
    template_name = 'providers/list-providers.html'
    queryset = Provider.objects.filter(is_active = True)

class ProviderCreateView(CreateView):
    model = Provider
    template_name = 'providers/create-providers.html'
    fields = '__all__'
    success_url = '/providers/list-providers/'

class ProviderDeleteView(DeleteView):
    model = Provider
    template_name = 'providers/delete-provider.html'
    success_url = '/providers/list-providers/'

class ProviderUpdateView(UpdateView):
    pass
